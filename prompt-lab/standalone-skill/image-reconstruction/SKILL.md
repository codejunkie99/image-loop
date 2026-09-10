---
name: image-reconstruction
description: Analyze image references into named visual elements and reconstruction JSON, then compile prompts for recreating, remixing, or selectively editing them. Use when the user wants to understand a reference, reuse its visual decisions, or preserve specific parts during an edit.
---

# Image reconstruction

Turn a reference into decisions the user can see and an agent can reuse: named elements, their relationships, explicit changes, a rendering prompt, and checks against the result.

Use this workflow for the user's requested scope. A simple image comment can supply enough information for a local edit. A detailed map and JSON are useful for reconstruction, multiple selectable elements, reference combinations, or a handoff. Do not require another approval for a clear, already authorized edit.

## Choose the control that fits the decision

| User need | Start with | First check |
| --- | --- | --- |
| New image from an idea | Purpose, canvas, objects, attributes, relationships, appearance, and intentional freedom | Main idea and reading order |
| Close reconstruction | Actual clean reference plus named inventory | Silhouettes, proportions, identity, and relationships |
| Obvious local change | Native comment or region selection with change / preserve / allow | Intended change and protected details |
| Many reusable choices or a handoff | Visual map and reconstruction JSON | Correct element targeting and compatible constraints |
| Difficult placement or pose | Sketch, legend, and separate finish instructions | Geometry, overlap, negative space, and physical action |
| Multiple references | Actual inputs with allowed roles and exclusions | Correct feature from the correct source |

Use comments, maps, and sketches together when helpful. Record a native comment against a stable element ID when the decision must survive into later work. Do not make the user fill out a detailed map for an obvious edit.

## Inspect the actual image

View each supplied image before describing it. Record source IDs `A`, `B`, and so on, the clean source version, and dimensions from file metadata when available. A path written in a prompt does not attach that image to a generator.

Separate three kinds of information:

- **Observed:** visible objects, readable text, shapes, positions, and overlaps.
- **Inferred:** likely materials, lighting direction, or visual style. Mark these as estimates.
- **Unknown:** exact font, original prompt, hidden geometry, source layers, or production settings that the pixels cannot establish.

For a new idea without a reference, use a user brief rather than claiming an extraction. State the purpose, canvas, contents, relationships, appearance, and observable success criteria. Do not invent a missing reference.

## Show the visual map

Inventory every meaningful visible element at a declared level of detail: subjects, objects, text, backgrounds, reflections, shadows, connectors, and useful empty space. Group microtexture or repeated minor detail when separate control would not help. Give independently editable elements stable IDs such as `A-05` and plain names such as `walnut cap`.

Record each element's approximate bounds, visible description, appearance, exact or uncertain text, relationships, and relevant occlusion. Use `[x, y, width, height]`, normalized from the clean image's top-left corner. Label estimated boxes honestly.

Show the clean image with a readable inventory and element previews. When interactive controls are available, let the user select the same element by clicking its region, choosing its name, or stating its ID. Keep overlays out of the image supplied to the generator.

A rectangular source crop may contain neighboring pixels. Call it a **bounding crop**. It is not a transparent layer, segmentation mask, or recovery of hidden content. Only claim those outputs after creating and checking them with appropriate tools.

For a native comment or region selection, resolve the target and use the same contract: **target → change → preserve → allow**. A comment pin does not guarantee unchanged pixels outside the selected area.

The included [VELLUM map](visual-map.html) provides 15 named elements over a luxury product photograph. It reuses the original map's selection, bounding-crop previews, keep/change/remove controls, property locks, reference roles, full/edit prompt compilation, and JSON export. It prepares instructions while preserving the displayed source pixels; it does not generate the requested edit.

For another image, prepare valid JSON first, then use **Import reconstruction JSON** and **Attach its clean source**. Check that the boxes and names match the actual image. The page performs no automatic image analysis. Keep exported JSON with its source assets, or update its paths before using the Python compiler; a browser file selection supplies a filename, not a durable absolute path.

The restored map's compiler and package links are checked programmatically. Browser interaction verification was unavailable in the authoring environment. Verify the controls in the receiving environment before relying on the UI for production work.

## Supply geometry through a sketch

Use the native drawing feature where available or attach an ordinary drawing image. Do not assume a toolbar exists in every client. Match the sketch's aspect ratio to the target; block in silhouettes, relative sizes, horizon or floor, overlap, pose, and useful empty space.

Supply a short legend assigning each mark to an object or relationship. Separate guide colors, construction lines, arrows, and labels from elements that should appear in the final artwork. Assign the drawing the layout role and describe materials, light, texture, and finish separately. State which proportions must remain and whether extra objects are allowed.

For an action, specify visible physical cues such as torso orientation, foot contact, gaze, and hand placement. Inspect geometry before surface polish. If the model places a window on the wrong wall, change the drawing or spatial rule before adding realism adjectives. An image-to-sketch result does not establish that the reverse transformation preserves the original design.

## Store observations and choices separately

Use [the reconstruction schema](references/reconstruction.schema.json). Read [the field guide](references/field-guide.md) when preparing JSON, assigning reference roles, or applying selected edits.

The JSON holds source records, scene observations, groups, elements, relationships, requested selections, invariants, unknowns, and criteria. It is an interchange format for the agent and interface. Its coordinates, weights, and locks are not special model API controls.

Preserve the original observations when the user requests a change. A walnut cap stays walnut in the source inventory; a requested metal finish belongs in `selections`. Record the geometry, text, and neighboring parts that must remain, plus physical consequences that may change, such as reflections.

Keep three concepts distinct: the reconstruction record describes the source, the selection record stores requested changes, and the rendering request tells the generator what to do now. A complete storage record can be large; compile only the relevant instructions for a local edit and respect the tool's actual input limits. Do not silently remove selected requirements to shorten a prompt.

Only store genuine constraints as locks. Do not turn your aesthetic suggestions into user requirements. Keep IDs stable across an edit; recheck them after changing the source version.

Assign every selected reference a role. One image may supply product identity, another layout, and another material. State which source wins when they conflict and which details should be ignored. Supply the actual selected images in the recorded order.

After an edit, review the compiler's `review_flags`. These identify baseline scene descriptions, invariants, and criteria that may conflict with the requested change. Reconcile them before scoring the result. An omitted or unexamined check is not a pass.

## Compile and generate

From the extracted skill folder, validate and compile with Python 3:

```sh
python3 scripts/reconstruct.py validate examples/vellum.reconstruction.json
python3 scripts/reconstruct.py compile examples/vellum.reconstruction.json --format json --output compiled.json
```

The output separates `rendering_prompt`, `attachments`, requested output, criteria, and warnings. Resolve relative attachment paths against the input JSON file's directory. Send the rendering prompt and actual image attachments to an available image-generation tool. Use only supported tool settings; record unavailable model or seed information as `not exposed`.

For a local edit, use `--mode edit` with a selected clean target and explicit changes. This keeps the rendering instruction focused while the full inventory remains available as evidence.

Inspect the compiled prompt for contradictions a structural validator cannot detect. Do not paste the full storage JSON into the image prompt as magic syntax. Explain quality through visible decisions: material behavior, coherent light, typography, composition, and finish appropriate to the intended use.

Save the exact submitted prompt, actual inputs, output, and review. Use the available image tool for generation; the bundled compiler does not generate images or require API credentials. If generation is unavailable or outside the request, return a prepared prompt and label it untested.

## Check and repair

Define hard requirements before generating. Check them individually as pass, fail, uncertain, or not evaluated. Inspect required objects before judging their dependent attributes or relationships. Aesthetic appeal cannot compensate for wrong text, a missing product, or an incorrect annotation.

Compare both the intended change and the protected regions. Inspect identity, geometry, labels, material texture, light, reflections, object counts, and crop as relevant. Check actual file properties when dimensions, transparency, or format matter.

Repair the largest diagnosed failure from the best accepted clean version. Isolate an uncertain change; combine compatible clear changes when their effects can be judged together. Allow physically necessary consequences. Every generation can introduce drift, so recheck preservation after each repair.

Stop when the requested checks pass, the agreed budget ends, or another tool is needed. Use deterministic typography, charting, compositing, or vector tools when the job requires exact geometry, editable artwork, or preserved pixels. Do not promise arbitrary images or pixel-identical reconstructions from a prompt.

For authorized parallel variants or comparisons, read [the experiment loop](references/experiment-loop.md). Keep the target and checks common, vary declared inputs, and record every attempt. Agents broaden the search; their use alone does not establish better image quality.

## The included worked example

The [VELLUM inventory](examples/vellum.reconstruction.json) was built by inspecting the included [source photograph](assets/vellum-source.png). Bounds are estimates; the inventory groups microscopic detail rather than claiming to recover every pixel.

The [exact compiled prompt](examples/vellum-reconstruction-prompt.txt) and source photograph produced the included [reconstruction result](assets/vellum-reconstruction.png). The [run record](examples/vellum-run.json) records the actual input, tool, and review. Composition, product identity, and readable label text remained close; wood grain, paper texture, stone veins, and reflections changed. This is one image-assisted study, with no claim that JSON caused the fidelity or improved the original photograph.

The full prompt library is separate from this skill. The small synthetic JSON fixture is included only for the compiler's internal checks.

```sh
python3 scripts/reconstruct.py self-check
```

Deliver the clean result, exact prompt, actual inputs, map or selection record, reconstruction JSON, and concise remaining limitations as appropriate to the user's task.
