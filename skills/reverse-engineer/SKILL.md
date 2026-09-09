---
name: reverse-engineer
description: Extract a supplied image into structured JSON with typography, palette, grading, composition, named elements, inferred layers, lighting, and evidence confidence.
---

# Reverse Engineer an Image

Inspect the attached image and follow the companion [Image Edit Map reverse-engineering protocol](../image-edit-map/references/reverse-engineer.md). Use its [JSON Schema](../image-edit-map/references/image-spec.schema.json). The installer includes that companion; if it is missing, say which file is needed rather than inventing the schema.

A bare invocation requests a comprehensive visual breakdown. Ask for an image if none is available. Return JSON plus a short readable explanation unless the person requests JSON only. Unknown values are null and explicitly marked unknown. Do not claim to recover the original prompt, exact fonts, hidden content, actual editable layers, or exact grading parameters from a flattened picture.

Offer the numbered map or an edit only after satisfying the extraction request. Do not generate or modify artwork during a JSON-only analysis.

Claude Code: `/reverse-engineer`. Codex: `$reverse-engineer` or select the skill through `/skills` where available.
