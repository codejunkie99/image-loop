#!/usr/bin/env python3
"""Check the published collection, local links, media, archives, and privacy.

Optional --private-term arguments stay local and are never written to the report.
Requires Pillow and pypdf; JavaScript syntax checks use Node when available.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from PIL import Image
from pypdf import PdfReader

TEXT = {'.md', '.txt', '.json', '.html', '.css', '.js', '.mjs', '.py', '.svg', '.yml', '.yaml'}
IMAGES = {'.png', '.jpg', '.jpeg', '.webp'}
LOCAL_PATH = re.compile(r'/(?:Users|home)/[^/\s]+/|/var/(?:folders)/')


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.scripts = [], set(), []
        self.current_script = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for name in ('href', 'src', 'poster'):
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == 'script' and not attrs.get('src') and attrs.get('type', '') in ('', 'module', 'text/javascript'):
            self.current_script = []

    def handle_data(self, value):
        if self.current_script is not None:
            self.current_script.append(value)

    def handle_endtag(self, tag):
        if tag == 'script' and self.current_script is not None:
            self.scripts.append(''.join(self.current_script))
            self.current_script = None


def verify(repo, private_terms=()):
    lab = repo / 'prompt-lab'
    errors, pages, scripts = [], {}, []
    counts = {'files': 0, 'json_files': 0, 'images': 0, 'pdf_pages': 0,
              'archives': 0, 'local_links': 0, 'javascript_blocks': 0}
    private = [re.compile(re.escape(term), re.I) for term in private_terms if term]

    def private_content(text):
        value = unquote(text)
        return bool(LOCAL_PATH.search(value) or any(p.search(value) for p in private))

    def fail(path, reason):
        # Report paths and categories, never matching private text.
        errors.append({'file': path.relative_to(repo).as_posix(), 'check': reason})

    files = [p for p in repo.rglob('*') if p.is_file() and not any(
        part in {'.git', '__pycache__', '.venv', '.codebase-memory'} for part in p.relative_to(repo).parts)]
    for p in files:
        counts['files'] += 1
        if p.stat().st_size >= 100 * 1024 * 1024:
            fail(p, 'exceeds GitHub regular-file limit')
        if any(pattern.search(p.relative_to(repo).as_posix()) for pattern in private):
            fail(p, 'private identifier in filename')
        suffix = p.suffix.lower()
        if suffix in TEXT:
            text = p.read_text()
            if private_content(text):
                fail(p, 'private identifier or machine-specific path')
            if suffix == '.json':
                try:
                    json.loads(text)
                    counts['json_files'] += 1
                except ValueError:
                    fail(p, 'invalid JSON')
            if suffix == '.html':
                page = Page()
                page.feed(text)
                pages[p] = page
                scripts.extend((p, script) for script in page.scripts)
        elif suffix in IMAGES:
            with Image.open(p) as im:
                if private_content(str(im.info) + str(dict(im.getexif()))):
                    fail(p, 'private image metadata')
                im.load()
            counts['images'] += 1
        elif suffix == '.pdf':
            pdf = PdfReader(p)
            counts['pdf_pages'] += len(pdf.pages)
            if private_content(str(pdf.metadata)):
                fail(p, 'private PDF metadata')
            for page in pdf.pages:
                if private_content(page.extract_text() or ''):
                    fail(p, 'private PDF text')
                for annotation in page.get('/Annots', []):
                    if private_content(str(annotation.get_object().get('/A', {}))):
                        fail(p, 'private PDF link')
        elif suffix == '.zip':
            counts['archives'] += 1
            with zipfile.ZipFile(p) as archive:
                if archive.testzip():
                    fail(p, 'damaged ZIP member')
                for item in archive.infolist():
                    if private_content(item.filename):
                        fail(p, 'private ZIP filename')
                    if Path(item.filename).suffix.lower() in TEXT:
                        if private_content(archive.read(item).decode()):
                            fail(p, 'private ZIP text member')

    def check_link(owner, value):
        if not value or value.startswith(('#', 'data:', 'blob:', 'javascript:', 'mailto:')):
            return
        link = urlsplit(value)
        if link.scheme or link.netloc:
            return
        target = (owner.parent / unquote(link.path)).resolve()
        counts['local_links'] += 1
        if not target.exists():
            fail(owner, 'missing link: ' + value)
        elif link.fragment and target in pages and unquote(link.fragment) not in pages[target].ids:
            fail(owner, 'missing HTML anchor: ' + value)

    for p, page in pages.items():
        for link in page.links:
            check_link(p, link)
    for p in files:
        if p.suffix == '.md':
            # Literal examples inside fenced code blocks are not navigation.
            text = re.sub(r'```.*?```', '', p.read_text(), flags=re.S)
            for link in re.findall(r'\]\(([^)\n]+)\)', text):
                check_link(p, link.strip('<>'))

    catalog_path = lab / 'article-package/prompt-library.json'
    catalog = json.loads(catalog_path.read_text())
    assert len(catalog['cases']) == 44
    assert len(catalog['trial_records']) == 49
    for case in catalog['cases']:
        check_link(catalog_path, case['image'])
    for record in catalog['cases'] + catalog['trial_records']:
        prompt_path = catalog_path.parent / record['prompt_file']
        if prompt_path.read_text().strip() != record['prompt'].strip():
            fail(prompt_path, 'prompt differs from the library record')
    prompt_files = list((lab / 'article-package/prompts').rglob('*.txt'))
    assert len(prompt_files) == 95
    counts.update(selected_studies=44, additional_records=49, saved_prompt_files=95,
                  library_prompts_matched=93)
    tables = sorted((lab / 'table-images').glob('*.png'))
    assert len(tables) == 12
    for table in tables:
        with Image.open(table) as im:
            assert im.width == 3200
    counts['table_graphics'] = len(tables)
    assert len(PdfReader(lab / 'article-package/visual-guide.pdf').pages) == 50

    node = shutil.which('node')
    if node:
        with tempfile.TemporaryDirectory(prefix='prompt-lab-check-') as directory:
            for i, (owner, script) in enumerate(scripts):
                temp = Path(directory) / f'inline-{i}.mjs'
                temp.write_text(script)
                result = subprocess.run([node, '--check', str(temp)], capture_output=True, text=True)
                if result.returncode:
                    fail(owner, f'JavaScript syntax block {i}')
                counts['javascript_blocks'] += 1
    return {'status': 'pass' if not errors else 'fail', 'checks': counts,
            'privacy': 'checked text, filenames, image/PDF metadata, PDF text, and ZIP members',
            'javascript_syntax': 'checked' if node else 'not checked: Node unavailable',
            'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--private-term', action='append', default=[])
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    report = verify(Path(__file__).resolve().parents[1], args.private_term)
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report['status'] == 'pass' else 1)


if __name__ == '__main__':
    main()
