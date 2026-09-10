# Reconstruction JSON field guide

The JSON separates three things that a long prompt usually mixes: **what is visible**, **what the person chooses to change**, and **how the result will be checked**. It is an editable specification, not a recovered creation history.

## Minimum working process

For a simple local edit, native image comments or a supported region selector can replace the map UI. A comment such as “make this arrow magenta; keep its path and everything else” already supplies a target and delta. Preserve that intent, add only a necessary physical allowance, then inspect the actual result. Comments and mapping are optional interfaces to the same contract, not competing model syntaxes. Use JSON when the inventory or state needs to be reused.

1. Inspect the clean image and available metadata. Record its source ID, version, dimensions and use in `source_images`.
2. Establish meaningful groups and a complete inventory at a declared granularity. Give elements stable IDs, names and visible bounds.
3. Record observed appearance, inferred explanations and unknowns. Map relationships and exact/uncertain text separately.
4. Show the image map and named element tray. Let the person select changes by ID; write those changes in `selections`.
5. Define hard checks and soft preferences, validate the JSON, then compile a prompt and attachment checklist.
6. Generate with an available image tool, inspect the actual output, and revise the specification only for an identified reason.

For a simple request the JSON can have empty groups, relations and unknowns. Do not fabricate data to make a field look comprehensive. `source_images` can be empty for a new image described entirely in `scene`. For structured new-image planning, give the intended canvas a target record with `path: null`; its geometry is `user_supplied`, not measured.

## The interface contract

| Field | Meaning |
| --- | --- |
| `schema_version` | Exactly `1.0.0`; reject unsupported versions instead of guessing. |
| `document_id`, `revision` | Identify a specification and its current revision. Increment revision after selections or map geometry change. |
| `provenance` | `image_analysis`, `user_brief`, or `synthetic_example`, with an honest note. |
| `intent` | Task, intended use, requested output and exactness target. Strict geometry needs a stated tolerance; pixel equality needs deterministic editing and comparison. |
| `coverage` | Granularity, omissions, ambiguous regions and whether the visible inventory is partial. |
| `source_images` | One target canvas, optional references/analysis images, measured or unknown dimensions, source version and role selections. |
| `scene` | Evidence objects for composition, view, lighting, medium, palette, grading or other global observations. |
| `groups` | Named control groups with source-relative bounds. `A-G01` can contain further groups or elements. Groups are not recovered layers. |
| `elements` | Individually addressable objects, subjects, text, connectors, backgrounds, empty regions, effects and repeated details. IDs look like `A-01`. |
| `relations` | Explicit endpoints and spatial or semantic relationships, with evidence status. A diagram arrow is its own element; `points_to` records what it means. |
| `selections` | Requested keep/remove/replace/restyle/move actions. Source observations remain unchanged. |
| `invariants` | What must survive, and whether it came from the user or the reconstruction brief. |
| `unknowns` | What cannot be recovered, why, and whether to leave it unspecified, ask if needed or approximate with disclosure. |
| `criteria` | Hard requirements and weighted soft preferences in separate arrays. |
| `review_flags` | Optional derived record after edits: revision, omitted baseline scene fields, potentially affected invariant/criterion IDs and notes. The mapper exports it; the compiler also computes it. |

The compiler builds the scene from the target canvas's elements. It does not copy every reference image's subject into the output. If a reference supplies a new object, create the intended object on the target canvas and assign that reference's content or identity role explicitly. For a text-only reconstruction, leave the target's `selected_for_use: false` while retaining its observed inventory. For an image-assisted reconstruction, set it true and attach the clean file.

## Coordinates and stable identity

`bbox` is `[x, y, width, height]`, normalized from the top-left of the **clean source image**. `x` increases rightward; `y` increases downward. Values lie in 0–1 and the right/bottom edges must not exceed 1. A missing or unlocatable box is `null` with `geometry_basis: "unknown"`.

For a W×H source, a displayed crop can start at `floor(x×W), floor(y×H)` and end at `ceil((x+width)×W), ceil((y+height)×H)`, clamped to the image bounds. This conversion computes a rectangle; it does not turn estimated object boundaries into a measured segmentation. Letterboxing, browser resizing and annotation margins need their own display transform. Never write their screen coordinates back into the source boxes.

Use bounds for the visible portion of partly occluded or off-frame elements. Record occluders and unknown hidden content. A group box describes its control region, and its children retain original source coordinates rather than coordinates relative to the group.

`destination_bbox` uses the intended output canvas's normalized coordinates. Moving a group keeps its relative internal arrangement; the compiler scales its children accordingly. A group and its child cannot both receive separate move instructions in one revision, because the coordinate frame would be ambiguous. Move the group first, accept/remap that version, then move its child if needed.

Keep an ID when its element moves, changes color or changes wording. Retire it when the element is deleted; use a new ID for a newly introduced independent element. A replacement can retain the selected slot's ID with its source history recorded by revision. Regenerating a substantially different scene requires checking every saved ID against the new source version.

Keep an element's intrinsic description separate from positional relationships. “A narrow cylindrical lamp” can survive a move; “a lamp above the right planter” becomes stale when the lamp moves above the middle planter. Store the latter in `relations` and inspect retained prose after movement. The compiler can omit stale structured relationships, but cannot reliably rewrite spatial implications embedded in arbitrary sentences.

## Evidence without fake precision

Every `description`, `appearance` attribute and `scene` attribute is an evidence object:

```json
{
  "value": "fine plain woven blue fabric",
  "status": "observed",
  "basis": "visual_observation",
  "confidence": "high",
  "note": "The weave is visible; the fiber composition is unknown."
}
```

Allowed statuses are `observed`, `inferred`, `unknown`. The basis records how the claim was obtained. An exact pixel sample can support a sampled color at a location; it does not prove that color was the designer's original paint value. A soft shadow can support an inferred soft light; it cannot recover the original lamp wattage or lens.

Unknown evidence uses `value: null`, `status: "unknown"`, `basis: "unknown"`, `confidence: "unknown"` and a reason in `note`. Confidence is an evidence label, not a calibrated probability. Counts are an integer only when the visible count is sufficiently clear; otherwise use `null` and explain the uncertainty in the description or unknowns. Synthetic examples and user briefs describe stipulated visual choices, not observed pixels.

Text has a separate `certainty`: `exact` or `uncertain`. An exact transcript must be nonempty and cannot also have uncertain spans. Preserve actual line breaks when known and required. Unreadable text must not silently become plausible wording. Font class can be observed or estimated while the family remains unknown.

`asset.kind` separates four cases: no asset; a bounding crop; a newly segmented transparent layer; or an actual supplied source layer. A segmented layer requires a real saved asset and verified alpha. The validator checks that those declarations are coherent; it cannot inspect image edges or prove that alpha was checked. A mask helps select a region only when the chosen tool supports it, and may still not guarantee unchanged pixels elsewhere.

## Reference choice and edits

`selected_for_use` means the person chose this image as an input for the current job. `allowed_roles` limits the information to borrow. These fields do not establish ownership, a legal license, model access or upload authorization beyond the actual request. A palette-only reference must not silently supply its logo, subject or text.

Example: A is the clean target with content/layout roles; B supplies material; C supplies palette. The prompt should say what B and C contribute, which source wins if they conflict, and which properties of A stay fixed. Attach those exact files in the declared order. Do not give the tool a manifest full of filenames and claim the image inputs were supplied.

An edit record is explicit enough for a UI or an agent:

```json
{
  "target_id": "A-08",
  "action": "restyle",
  "properties": ["appearance.color"],
  "instruction": "Change only the five leaves from violet to golden yellow.",
  "destination_bbox": null,
  "reference_ids": [],
  "preserve": ["five leaves", "leaf shape", "plain material", "clear container"],
  "allow": ["subtle reflected warm color on nearby glass"]
}
```

Property paths are `description`, `count`, `text`, `bbox`, `appearance`, or an attribute such as `appearance.color` or `appearance.font_class`. `editable_properties` is a useful control menu, not an authorization gate. `locked_properties` records explicit protected properties. A newer clear user instruction can revise a prior lock; update the manifest to reflect that instruction before compiling rather than silently violating it.

Keep/removal need no destination. Move requires a destination box. Restyle requires named properties and an instruction; use move for geometry. Replace substitutes the selected content and appearance within its slot. A compatible move and restyle can target the same element; conflicting keep/remove/replace instructions are rejected. Group removal/replacement applies to children. The compiler suppresses obsolete source attributes for changed properties instead of asking for both the old and new color.

Free-text invariants and criteria still need a semantic review. A validator cannot know that “make this red” conflicts with an old requirement phrased “retain the blue accent.” Change the requirement only when the user's request changed; do not loosen it after an output failed.

The working interface found exactly this issue: recoloring the return arrow left “turquoise water and return arrow” in a global palette observation and “large teal return arrow” in an original hard check. Those source facts must remain in the evidence record, but must not be asserted as the edited output's desired color. The compiler now derives `review_flags` from selected targets and their groups. After edits it omits broad source scene prose, potentially affected baseline invariants/checks, and intrinsic descriptions of the edited targets that could hide stale attributes. It keeps unchanged element attributes, explicit deltas and preservation requirements in the new prompt.

These flags are conservative: a spatial check may be flagged by a color change simply because it refers to the same object. They are not an automated natural-language proof of a contradiction. Original criteria remain in JSON as baseline evidence. An agent should reconcile flagged criteria with the explicit user edit before scoring them; it must not count an omitted check as a pass or silently abandon its unaffected requirements. If no image is attached, reconstructing an edited scene may need the agent to restore verified unaffected global style cues after this review.

The exported `review_flags` must match the current revision and selected edits; stale flags are rejected. Python callers can obtain the canonical flags with `review_flags_for(spec)`, and a compile result includes them even when the input JSON omitted the optional field. The plain-language rendering prompt is safe to use directly; complete evidence and review state travel with the JSON for a deeper agent handoff.

## Validation and compilation

Run the script from anywhere by giving its path; resource paths inside it resolve relative to the package. Python 3.9 or later is sufficient.

```sh
python3 scripts/reconstruct.py validate path/to/reconstruction.json
python3 scripts/reconstruct.py compile path/to/reconstruction.json --format json --output compiled.json
python3 scripts/reconstruct.py compile path/to/selected-edit.json --mode edit --format json --output selected-edit-prompt.json
```

JSON output separates `rendering_prompt`, actual attachment records, requested output, criteria and warnings. Text output separates the same sections for copying. Pass the rendering prompt and actual attachments to the image tool; apply only supported output settings. Paths are data and are never executed. Compilation has no network call or image-generation side effect and does not overwrite its input JSON.

`--mode edit` requires a selected clean target and a requested change. It compiles the selected delta and preservation instructions without repeating every unchanged source observation. Full reconstruction uses the default mode. Keep the complete evidence JSON as storage; do not paste it wholesale into a generator. The accompanying test encountered one tool's 32,000-character limit with an 82,283-character raw document. This limit does not establish the limits of other APIs. Resolve source paths relative to the saved JSON when they are not absolute; the tool still needs the actual image attachment.

Explicit preserve/allow duplicates and preserved property paths that directly conflict with a changed property are rejected. Arbitrary prose can still contain semantic contradictions. If a selected change alters an original success criterion, update that criterion because the user's request changed, and retain the original source observations; never weaken a criterion merely because generation failed.

The native validator supports the JSON Schema keywords used in the bundled file, plus semantic checks for IDs, coordinate bounds, source roles, evidence consistency, hierarchy, locks and dependency cycles. It is not a replacement for a general JSON Schema implementation. A full draft-2020-12 validator can additionally consume the schema if already available. Passing either check does not establish that the described image exists, matches the source or will generate successfully.

## Copyable extraction instruction

> Inspect the attached clean image and produce a visual map plus reconstruction JSON using this package's schema. Inventory every meaningful visible element at a declared granularity, assign stable IDs and plain names, and show separately selectable source crops or detail views. Label those crops as bounding crops unless actual segmentation is performed. Record source dimensions from metadata when available. Separate observed appearance, inferred explanations and unknowns; include exact/uncertain text, normalized bounds, groups, relationships, occlusions and preservation requirements. Do not infer hidden layers, unreadable text or an original prompt. Keep requested changes in selections instead of rewriting source observations. Validate and compile the JSON, supplying the real references only for selected roles. Define hard checks and soft preferences before generation. After generation, inspect every requested change and protected detail, retain the best accepted version and report concrete failures. If the task is analysis-only, return the map, JSON and prepared prompt without generating an image.
