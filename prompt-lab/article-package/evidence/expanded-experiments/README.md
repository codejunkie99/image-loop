# Expanded image-prompting experiments

This folder retains the generated examples behind the expanded guide, including failures. The [official prompting guide](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5) contains 24 illustrated prompt steps under the counting rule used here. All 24 are represented by adaptations: the subjects are sometimes changed to make the same technique more demanding. These are not literal reproductions of OpenAI's examples or a controlled comparison against its published images.

## Find an experiment

| Guide steps or question | Folder |
|---|---|
| G01 and G03–G09: original generation, campaigns, logos, history, comics, UI, science and slides | `generation-coverage/` |
| G02: process infographic, expanded as the five-tier Rain Engine; plain prose versus labeled sections | [language protocol](language/protocol.md) |
| G10–G17: localization, style, wardrobe, compositing, transparency, sketch rendering, deletion and insertion | [edit records](edit-coverage/records.json), [observations](edit-coverage/review.md) |
| G18–G24: campaign iteration, character continuity, room editing, greeting card and merchandise | `continuity/` |
| Same railway scene with person-only, dog-only or both references | [reference-matrix records](reference-matrix/records.json) |
| Plain versus embellished vocabulary | `vocabulary/` |
| Reconstruction prompt without and with the image reference | `reconstruction/` |
| Visual element mapping and a selected-element edit | `mapping/` |

G22 also retains the two sequential edit stages, E22A and E22B, alongside the combined edit. Extra filenames ending in `repaired` or `repair` are separate follow-ups, not replacements for failed originals. The [alpha repair record](edit-coverage/g14-alpha-repair.json) documents a second retained failure: both shampoo attempts are opaque RGB files with painted checkerboards.

## What is and is not matched

The language comparison uses the same visual sentences, with headings added in one condition, and two samples per condition. The three reference arms use an identical fixed descriptive scene body, but the actual images and attachment declarations change. The kitchen comparison starts from one source and targets the same final colors; the sequential path uses two calls instead of one. These are small exploratory comparisons with their confounds recorded, not estimates of a universal improvement percentage. Neutral filenames support review before revealing conditions; operator reviews are not blind.

## Reproduce the procedure

1. Read the applicable saved prompt, reference-role list, checks and observations. Keep the original output available for comparison.
2. Use the listed source images in the recorded order. Keep the fixed brief unchanged when testing one variable; log any different attachment declaration or setting.
3. Generate a new candidate without overwriting an old one. Record the actual tool, model if exposed, seed if exposed, settings, file dimensions and file hash.
4. Inspect every criterion as pass, fail or uncertain. Inspect the saved file's alpha channel when transparency is required; a checkerboard preview is not evidence.
5. Record targeted repairs as new attempts and recheck preserved regions. Keep failed and ambiguous outcomes visible.

All image calls here used the available built-in generator. Its backend/model, seed and quality were not exposed, so these results cannot be claimed as verified GPT Image 2.5 measurements or reproduced pixel for pixel by selecting that name. Published OpenAI output images are reference material, not our generated results.

Native ChatGPT Sketch and image Comments are documented workflows, not executed native-feature tests in this run. Sketch-to-render **was** tested by supplying a drawing to the available image generator. Unverified Safari annotation interaction is excluded from the evidence; the local visual mapping demonstration is a separate artifact.
