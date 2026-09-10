# Prompt Lab

The complete image-prompting collection: articles, submitted prompts, source images, results, repair records, reconstruction tools, and visual aids.

## Start here

- **[Latest illustrated article](image-prompting-article-with-prompts-and-results.md)** — the full methodology, premium examples, prompts, and results. [Browser edition](image-prompting-article-with-prompts-and-results.html).
- **[Prompt library](article-package/prompt-library.md)** — 44 selected studies and 49 additional experiment records, with original prompts and limitations. [Searchable browser edition](article-package/prompt-library.html) · [JSON](article-package/prompt-library.json) · [95 saved prompt files](article-package/prompts/).
- **[50-page visual guide](article-package/visual-guide.pdf)** — methods and all 44 selected studies, with images and prompt excerpts.
- **[Reconstruction skill](../skills/image-reconstruction/SKILL.md)** — the current VELLUM example, reconstruction JSON, schema, compiler, and editable map. [Download the portable skill](image-reconstruction-premium-skill.zip).
- **[Visual map](../skills/image-reconstruction/visual-map.html)** — select named elements, record edits and preservation rules, and export prompts or JSON.
- **[12 visual aids](table-images/)** — blue, light-mode graphics at 3200 pixels wide. [Copy/download gallery](table-images/index.html) · [PNG archive](article-table-images.zip).
- **[Article with image tables](image-prompting-article-with-prompts-and-results-tables-as-images.md)** — ready to reuse in Markdown.

The two newer companion studies, including the VELLUM reconstruction and updated UGC portrait, are in the latest article and [premium article assets](premium-article-assets/). They are separate from the original 44-study catalog.

## Open the interactive tools

GitHub displays Markdown and images, but does not execute committed HTML pages. Download or clone the repository, then run this from its root:

```sh
python3 -m http.server 8000
```

Open **http://localhost:8000/prompt-lab/** for the hub, prompt search, galleries, and visual maps. Reading, selecting elements, and compiling prompts do not call a generation service. Actual generation requires an image-capable agent and attached image files.

## Full collection

- [20 premium applications and their review gallery](premium-examples/index.html)
- [Expanded guide and 24 guide adaptations](image-prompting-guide-v2.md)
- [Full master prompt](master-image-prompt.md) and [compact master prompt](master-image-prompt-v2.md)
- [Research](research-notes-v2.md) and [earlier research notes](research-notes.md)
- [Experiment manifest](expanded-experiments/manifest.json), [records](expanded-experiments/records/), and [first experiment log](experiment-log.md)
- [Original 50-element map](visual-map.html) and [original reconstruction skill](image-reconstruction-skill/SKILL.md)
- [Earlier article](article-package/article.md) and [original guide](image-prompting-guide.md), retained as historical context

## What this evidence supports

The studies document prompts, inputs, observed outputs, and repairs. Some records repeat selected studies; these are not 93 independent trials. The image tool did not expose its executing model, variant, seed, or quality setting, so the results do not establish a model-version benchmark, a general success rate, or an advantage from adding agents. Planned comparison branches are labeled as unrendered.

Maps use approximate boxes and rectangular previews, not recovered image layers or segmentation masks. The source stays separate from overlays. Native drawing and image comments were documented; the recorded drawing-input studies used uploaded images.

## Publication checks

Personal paths were converted to portable references where the matching asset was available. Unavailable machine-local locations are explicitly omitted. Image files retain their original bytes. PDF metadata was replaced without changing its 50 pages or visible text. Historical verification records describe their original editions; [publication-verification.json](publication-verification.json) records checks on this repository copy.

The repository retains source credits and links. The MIT license covers the repository's original code; it does not override rights in credited third-party reference material.
