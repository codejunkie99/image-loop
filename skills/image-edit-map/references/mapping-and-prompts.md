# Mapping and prompt recipes

## Build the address system

Use image IDs `A`, `B`, etc. and section IDs `A:S1`, `A:S2`. Split by semantic function and geometry: headline area, hero photo, diagram, footer. Do not force a 3×3 grid over a meaningful composition. One image can have one section if it is simple.

Assign stable element IDs `A:1`, `A:2`, etc. Display them as `A:#1`. Numbers identify elements; named sections organize them. Reading order is a useful initial numbering order. Use plain names: “main headline,” “blue bottle,” “return arrow,” “background gradient.” Include backgrounds and empty space if they are meaningful edit targets.

Map every meaningful editable object, text block, connector, or visual group. For dense pictures, create an overview of groups followed by section close-ups for individual elements; do not cover the image with unreadable badges. Do not pretend every grain of texture or hidden object can be extracted. Include excluded or ambiguous regions in the legend.

Record a map manifest using the reverse-engineering schema's images, sections, elements, and relationships fields; other categories can be empty for a map-only request. Each element has a section, bounding box, arrow target, name, kind, and editable properties. Bounding boxes use normalized `[x, y, width, height]` within the **original clean image**, top-left origin, range 0–1. Arrow targets use `[x, y]`. Record whether coordinates were measured or estimated. Detailed masks are optional; a rectangle is not a segmentation mask.

The review canvas may add a clearly separate outer margin for badges. Keep source scale/aspect ratio and crop unchanged when possible. Store any display scaling and offset separately; never apply review-canvas coordinates to the source image. Use high-contrast numbered badges plus arrows, not color alone. Keep badges off text, faces, logos, and fine details. Route arrows so their tips unambiguously identify targets. Annotation arrows must look distinct from diagram arrows and must not alter diagram meaning.

Use this legend format:

| ID | Section | Element | Location | Can change | Locked |
| --- | --- | --- | --- | --- | --- |
| A:#1 | Heading | Main headline | Top left | Text, font, color, position | Exact wording |

After rendering, inspect the map: every badge/arrow must match the manifest, no duplicate numbers, no invented elements, and no materially changed artwork. If a generative annotation pass distorts the source, do not use its geometry as ground truth. Retry a clearer mapping view or disclose the limitation; use a deterministic overlay only if permitted. Never call a generative annotation copy pixel-identical without comparison.

## First image prompt: annotation pass

Populate the manifest first. Never ask the renderer to invent its own numbering independently.

```text
Create an ANNOTATED REVIEW COPY of the supplied image.
The image is a reference for discussing edits. Do not redesign it.

Clean source: [image identifier and attached image].
Sections: [section IDs, plain names, normalized bounds].
Element manifest: [ID, name, bounds, arrow target for each visible element].

Overlay numbered badges and thin leader arrows using exactly the supplied IDs.
Each arrow tip must land on its named element. Label major sections unobtrusively.
Keep original words, layout, object geometry, colors, and diagram connections.
Place badges away from important details; use an outer review margin if needed.
Keep annotations visually distinct from connectors already in the artwork.
For dense sections produce an overview and separate detail views with the SAME IDs.
Do not insert the legend's descriptive prose into the artwork.
This copy is for review only. The clean original remains the editing source.
```

Ask the user to select by ID after showing the map and legend. Example: “Which numbers should change, and what should happen to each?” If the edit list was already supplied, use it without repeating the question.

## Edit instruction

```text
Clean source/version: [A, v0; actual attached clean source]
Reference roles: [B = typography only; C = composition only]
Target: [A:#3, name, section, source-coordinate region]
Operation: [replace text / recolor / move / restack / regrade / change medium]
Change: [specific property and requested value]
Text verbatim, if relevant: [exact copy with explicit line breaks]
Preserve on target: [all other properties that matter]
Preserve outside target: [named protected elements/regions]
Canvas/export: [agreed dimensions, aspect ratio, crop/pad policy]
Check success: [visible acceptance criteria]
Do not render map badges, review labels, or annotation arrows.
```

Resolve IDs into descriptions and coordinates; the model cannot understand `#3` alone. Attach the clean source, not just its filename or an old conversation reference unavailable to the tool. Use one change per iteration when exploring an uncertain direction; apply a clearly specified compatible batch together when the user requested it.

## Reference mixing

```text
A is the clean target: preserve its content and arrangement.
B supplies typography only: [letterform characteristics, weight, spacing].
C supplies palette only: [named colors and roles].
Do not copy B's words, subject, layout, logo, or background.
Do not copy C's lighting or grading unless separately requested.
```

## Interaction example (illustrative, not a measured result)

Person: “I like this image but the title feels wrong.”
Assistant: “Should the words change, or just how the letters look? What must stay exactly as it is?”
Assistant: Inspects and creates review map: `A:#1 headline`, `A:#2 product`, `A:#3 background`.
Person: “Make #1 less bold, keep the words. Lock #2.”
Assistant: Edits headline weight using clean image A; protects product, wording, color, and canvas; compares the saved result and reports any drift.
