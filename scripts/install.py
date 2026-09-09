#!/usr/bin/env python3
"""Copy the skill set into a host directory; no overwrite without --replace."""
import argparse
import shutil
from pathlib import Path

NAMES = ('image-loop', 'image-edit-map', 'reverse-engineer')


def install(source_root, destination, replace=False):
    destination = Path(destination).expanduser()
    for name in NAMES:
        src = (source_root/name).resolve()
        dst = (destination/name).resolve()
        if src == dst or src in dst.parents or dst in src.parents:
            raise ValueError('Source and destination overlap; choose a separate skills directory.')
    existing = [destination/name for name in NAMES if (destination/name).exists() or (destination/name).is_symlink()]
    if existing and not replace:
        raise FileExistsError('Existing skills: '+', '.join(p.name for p in existing)+'. Use another directory or explicitly pass --replace.')
    # Preflight all sources before changing any destination.
    for name in NAMES:
        if not (source_root/name/'SKILL.md').is_file():
            raise FileNotFoundError(source_root/name/'SKILL.md')
    destination.mkdir(parents=True, exist_ok=True)
    for name in NAMES:
        dst = destination/name
        if dst.is_symlink():
            dst.unlink()
        elif dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(source_root/name, dst, ignore=shutil.ignore_patterns('__pycache__','*.pyc','.private'))
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--to', required=True, type=Path, help='E.g. ~/.codex/skills or ~/.claude/skills')
    parser.add_argument('--replace', action='store_true')
    args = parser.parse_args()
    try:
        dest = install(Path(__file__).resolve().parents[1]/'skills',args.to,args.replace)
    except (OSError, ValueError) as exc:
        parser.exit(1,str(exc)+'\n')
    print('Installed '+', '.join(NAMES)+' into '+str(dest))


if __name__ == '__main__':
    main()
