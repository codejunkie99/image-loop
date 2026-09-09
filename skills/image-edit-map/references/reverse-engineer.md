# /reverse-engineer

## Purpose

Given an image, produce a reusable visual specification and a numbered inventory. Extract what is visible; make uncertainty explicit. This is analysis, not proof of the original creative process.

## Workflow

1. Inspect the image and decode available metadata with a file tool. Supply measured width/height to the extraction step; never trust dimensions inferred from a model's resized view. If no file tool is available, dimensions are unknown. Ask only for a missing image, an ambiguous target/reference relationship, or a scope choice that matters. A bare `/reverse-engineer` means a comprehensive visual breakdown; it does not require the user to answer editing questions first.
2. Assign images, sections, stable element IDs, source-relative bounds, and connector relationships as in the mapping protocol. Pass any existing ID manifest into extraction; do not let a second analysis renumber elements. Do not wait for an annotation render to begin JSON extraction. Only explicit user constraints populate `locked_properties`; otherwise use empty arrays. Suggested preservation belongs in the reconstruction brief, not actual edit locks.
3. Extract the categories below. Unknown is `null`; an absent category is `[]`. Add explicit unknowns so an empty field cannot masquerade as a complete extraction.
4. Return valid JSON matching `image-spec.schema.json`, plus a short human-readable summary unless JSON-only was requested. If files are supported, save `image-spec.json`. Provide the numbered visual map when requested or as the normal guided-mode companion; JSON-only must not trigger an unsolicited image generation.
5. Include a reconstruction brief that distinguishes visual goals from unverified production settings. It is a newly written approximation, never “the original prompt.” Offer the next useful action: inspect an element, edit a property, or reuse selected style attributes.

## Required coverage

- Canvas: measured or unknown dimensions, aspect ratio, orientation, observed transparency, profile if known, coordinate convention.
- Image purpose, primary medium, visual style, and regional medium differences.
- Sections and elements: names, types, bounds, anchors, section membership, edit controls, per-property locks.
- Composition: hierarchy, grid, spacing, alignment, whitespace, relative scale, visual path, safe areas.
- Typography and text: transcript, uncertain characters, line breaks, font classification/candidates, weight, size estimate, tracking, leading, alignment, effects, hierarchy.
- Palette: named roles, sampled/estimated values, gradients, local colors, stroke/fill/opacity distinctions.
- Grading: global versus regional scope, contrast, tonal curve appearance, shadow/highlight color, saturation, grain, vignette, white-balance appearance.
- Lighting and materials: direction, softness, shadows, reflections, material cues and textures. Distinguish inferred lighting from measured metadata.
- Layers: inferred front-to-back relationships, grouping, occlusion, effects, uncertainty. Never claim hidden content or editable source layers are recovered.
- Semantics: connectors with explicit endpoints and direction, labels, node counts, chart values and units where legible. Mark an unclear endpoint unknown rather than connecting it arbitrarily.
- Preservation: identity/product details, exact text, locked regions, and properties to keep when reconstructing.
- Export considerations: whether the observed asset appears flat or has measured alpha, constraints of current dimensions, and any target output explicitly requested by the user.
- Unknowns and follow-up questions: font identity, unreadable text, grading recipe, ambiguous topology, missing source assets.

## Evidence convention

Every extracted attribute uses an observation object:

```json
{
  "value": "geometric sans serif",
  "basis": "visual_estimate",
  "confidence": "medium",
  "note": "Rounded bowls; exact family unverified."
}
```

Allowed bases: `source_metadata`, `pixel_measurement`, `visual_observation`, `visual_estimate`, `user_supplied`, `unknown`. Confidence: `high`, `medium`, `low`, `unknown`. Numeric values remain estimates unless supported by measurement. Unknown observations have `value: null`, `basis: "unknown"`, `confidence: "unknown"`, and a reason in `note`. Confidence describes evidence strength, not a calibrated probability.

Category arrays contain scoped attribute records: `target_id` references an image or element; `attributes` holds observations. For example a typography record may contain `font_family`, `font_class`, `weight`, and `line_height_relative`. Spell out units in attribute names or notes. Grade only the photo if the surrounding typography is meant to stay unaffected. Each image must have a picture-type record, even if its medium is unknown.

## Extraction prompt

```text
Analyze the attached image into a structured visual specification.
Use the provided image-spec.schema.json contract.
Identify sections and individually editable elements with stable IDs and normalized bounds.
Separate text content, typography, local color, inferred layers, grading, medium,
composition, lighting, materials, relationships, and preservation constraints.
Attach an evidence basis and confidence to extracted attributes.
Use null for unknown values; do not infer exact fonts, editor settings, hidden layers,
original prompts, or authorship from appearance alone.
Mark illegible text and ambiguous connector endpoints explicitly.
Return JSON only if requested. Otherwise also provide a short readable legend and summary.
```

## Validation

The schema is JSON Schema draft 2020-12. Use an available schema validator to check structural conformance. `scripts/validate_spec.py` additionally checks bounds and references; it requires Python 3 and `jsonschema`. Pass `--image source.png` (and `--image-id A` for multiple images) to cross-check reported dimensions using Pillow. Neither structural validation nor dimension checks prove visual descriptions: inspect those independently. A live test produced schema-valid but incorrect "measured" dimensions, so metadata verification is a separate required check when a local source is available.

The example is a deliberately partial, synthetic specification for a fictional banner, not an extraction from a real image. Never reuse its coordinates, text, palette, or confidence claims on a user's photograph.
