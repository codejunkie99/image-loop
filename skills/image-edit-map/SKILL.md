---
name: image-edit-map
description: Guide image edits through questions, numbered visual maps, named elements, and preservation checks. Reverse-engineer reference images into structured JSON for typography, palette, composition, inferred layers, grading, and image types. Use for image editing, visual breakdowns, and reference analysis.
---

# Image Edit Map

Turn “change that bit” into an addressable edit. Help people see, name, and change an image without needing design vocabulary.

## Start here

1. Inspect every supplied image. If no image is available, ask for it; do not invent its contents. Identify which is the edit target and which are references. Read image metadata when possible; do not infer exact dimensions from a resized preview.
2. Ask up to three short, unanswered questions: **What should change? What must stay? Where will you use it?** Offer plain-language choices relevant to the actual image. If the user is unsure, make the map to help them decide. Do not repeat questions already answered in their brief. Ask follow-ups only when they affect the requested result.
3. Make the first image-generation prompt a **numbered annotation pass**, using [the mapping protocol](references/mapping-and-prompts.md). Divide the picture into meaningful sections; point arrows from number badges to individually editable elements. Show the map plus its matching legend before asking the person to select edits. This pass creates a separate review copy, never a redesign of the source.
4. Explain: **“You can say ‘make #3 smaller,’ ‘change #5’s font,’ or ‘keep everything in section B.’”** For multiple pictures, use `A:#3` and `B:#3`.
5. On selection, form an explicit edit instruction with target, property, requested change, and preserved details. Execute once enough information is available. A user's clear edit request authorizes that edit; do not add another approval step unless they asked to review a proposal first.
6. Compare the result with the clean source and the agreed constraints. Deliver a clean image, the actual dimensions, and a brief account of changes and any remaining mismatch.

Honor “just do this,” “skip the map,” or an already complete brief. Do not force a questionnaire or annotation round over an explicit direct-edit instruction. If the user requests planning or prompts only, provide those without generating images. In reverse-engineer mode, analysis is the requested output; do not automatically begin an edit.

## What the user sees

Present a small control menu beside the map. Use [the control dictionary](references/controls.md) for explanations and relevant follow-up questions.

| Control | Changes |
| --- | --- |
| **Text** | The words, spelling, capitalization, and line breaks |
| **Font / typography** | Letterforms, weight, size, spacing, alignment, and hierarchy |
| **Color** | A specific element's fill, stroke, gradient, or opacity |
| **Layer / depth** | What sits in front, behind, inside, or overlaps something else |
| **Color grading** | The overall tonal and color treatment of a photo or selected region |
| **Picture type** | Photo, illustration, 3D render, diagram, collage, screenshot, and related media |
| **Layout / crop** | Position, size, spacing, framing, and aspect ratio |
| **Lighting / material** | Light direction, shadows, reflections, and surface texture |

Example: “Make the title blue” is a local color change. “Give the photo cooler shadows” is grading. “Put the title behind the person” is layer order. Changing one does not authorize changes to the others.

## Conversational commands

These are instructions recognized **inside this skill**, not automatically installed host slash commands. If the host intercepts slash commands, invoke `$image-edit-map` and give the command in plain language.

| Command | Behavior |
| --- | --- |
| `/map` | Number and name the visible sections/elements; show a separate annotated review image and legend |
| `/inspect A:#3` | Explain that element's editable properties in everyday language |
| `/edit A:#3 ...` | Apply the specified change with all other properties preserved |
| `/lock A:#3` or `/lock section B` | Protect specified elements/regions; clarify visual similarity versus exact pixels if needed |
| `/unlock A:#3` | Remove that requested protection without changing the artwork |
| `/reverse-engineer` | Extract a structured visual specification; follow [the reverse-engineering protocol](references/reverse-engineer.md) |
| `/compare` | Compare named versions against the requested edit and protected content |
| `/export` | Resolve dimensions, crop policy, background, and format; verify the saved file |
| `/help` | Show the control menu and two example commands suitable for the current image |

## Preserve intent

- Keep original sources untouched. Give each image a source ID and each edit a version. Use the last accepted **clean** version for subsequent edits; never an annotated review image.
- Keep stable element IDs even if elements move. Retire deleted IDs; do not reuse them. New elements get new IDs. A changed source/layout requires updating the map and its coordinates before executing stale selections.
- Exact wording, capitalization, punctuation, line breaks, diagram labels, node counts, and arrow directions are separate constraints from visual style.
- “Use this reference” requires a role: typography, palette, composition, subject, lighting, or medium. Carry over only the assigned properties. If references conflict, resolve only the conflicting role with the user.
- “Keep that diagram” protects its topology and arrangement. A restyle does not authorize changing relationships or adding/removing nodes. Match the visual structure to the meaning when designing a new diagram: a central identity can radiate outward; a sequence needs directional connections.
- Resolution-only means preserve content and design. Clarify an ambiguous “4K” target when it affects aspect ratio. Never silently stretch, crop, or add content to hit a pixel count.
- “Everything else unchanged” is a constraint to verify, not proof that a generative edit succeeded. Exact pixel preservation requires an appropriate deterministic composition/editing workflow and a pixel comparison. If the available tool cannot provide that, disclose the limit before claiming success.
- Preserve the selected branch/version. If an edit drifts, retry from the accepted clean source rather than accumulating damage through the failed result.

## Tools and evidence

Use the host's image inspection and editing tools according to their live instructions. Prefer its image-generation/editing tool for actual image edits. Do not bypass tool restrictions with scripts or another provider. This skill supplies no API key, model entitlement, native editor, or automatic image renderer.

If image editing is unavailable, provide the map manifest, legend, and prepared annotation/edit prompt, and clearly say the visual map or edit has not been rendered. Do not substitute a text table and claim an annotated image exists. If the user wants deterministic overlays or compositing, use an appropriate editor only when authorized and supported.

Separate visible evidence from estimates. A flat image does not reveal original editable layers, an exact font family, the original prompt, a precise LUT, or hidden/occluded content. Report unknowns instead of presenting guesses as recovered facts.

Before delivery, use [the verification checklist](references/verification.md). When returning JSON, conform to [the schema](references/image-spec.schema.json). Source-specific identifiers, coordinates, and values must come from the current input, not the example file.

## Optional visual preset

If the person explicitly requests the author's technical-editorial look, offer dark or paper-light ground, predominantly white/black content, restrained blue emphasis, readable typography, and meaningful diagram connections. Confirm the chosen direction; never apply a historical palette, 5:2 canvas, brand, or layout to an unrelated person's image by default.

This workflow combines a numbered editing interface with lessons from targeted image revisions. General prompting guidance also informed it: [OpenAI image prompting](https://developers.openai.com/api/docs/guides/image-prompting). Verify current tool capabilities separately; this skill deliberately does not freeze model names or API settings.
