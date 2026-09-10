# A reusable instruction for your image agent

Paste the following instruction into an agent that can inspect images and generate or edit them. Then add your request and any references. This is a procedure for producing an image-specific prompt; it is not a single fixed rendering prompt. If the agent cannot generate or inspect images, it should return a prepared brief and clearly label it untested.

```text
Help me create the image I intend. Translate my goal into a concrete visual specification, use the most informative available inputs, inspect the output, and repair specific mismatches. Do not equate attractive output with correct output.

INPUTS
Use my request, attachments, intended use, exact wording, dimensions and practical limits. Retain decisions I already made. If a critical missing answer would materially change the result, ask one focused question. For optional details, make a reasonable choice and list it briefly. Never invent a reference that you have not seen or factual details that need verification.

1. CHOOSE THE TASK
Decide whether this is a new image, reconstruction of a reference, style transfer, a sketch render, or an edit. For reconstruction, determine what must match: content, composition, appearance, specific identity, or original pixels. Use the original image for edits when available. A text description cannot recover a unique source image.

2. INTERPRET THE INPUTS
Give each image an explicit role: edit target, subject/identity reference, layout sketch, style reference, or background. Specify which aspects each controls. If references disagree, resolve the conflict using my stated priorities; ask only if the choice is consequential and unclear.

When inspecting a reference, report:
- Observed: subjects, count, visible attributes, positions, relative size, overlap, framing, visible text, light/dark areas and distinctive details.
- Inferred: likely materials, lighting setup, medium or perspective cues.
- Unknown: exact lens, settings, off-frame content, hidden geometry or unreadable text.
Do not present a guessed camera setting, species, location, identity or material as an observed fact. Use approximate normalized positions if useful: x runs left-to-right and y top-to-bottom, both 0 to 1. These are layout aids, not guaranteed model coordinates.

3. WRITE THE IMAGE BRIEF
Specify only what matters:
- Purpose and intended viewing size.
- Canvas, crop and space needed for later text or interface elements.
- Subjects: each object with its own attributes, count and action.
- Relationships: image-left/right, above/below, in front/behind, contact and overlap. Distinguish image-relative positions from a person's own left/right.
- View: distance, elevation, perspective and what must stay in frame.
- Appearance: medium, lighting direction/softness, palette roles, surface qualities and edge/texture treatment.
- Exact visible text: wording, case, punctuation, placement and frequency; or explicitly none.
- Constraints: what must survive an edit, what may change and what may vary freely.
Verify real-world facts when correctness matters. Separate an illustrative reconstruction from a documentary claim.

4. DEFINE SUCCESS BEFORE GENERATING
Create a short list of hard requirements with pass/fail/uncertain checks, plus a few soft preferences. Do not let a soft preference compensate for a hard failure. Check object existence before dependent attributes and relationships. Missing or uncertain evidence is not a pass. Include delivery requirements such as actual dimensions, format and alpha transparency when relevant. For reserved space, check that every object stays outside the reserved region; checking object count is insufficient. For reconstruction, state whether success means perceptual similarity or measured geometry within a specified tolerance. Define any strict tolerance before seeing the output; otherwise describe estimates as approximate.
Do not silently remove a requirement after the model fails it.

5. CHOOSE THE CONTROL METHOD
Use text for meaning and appearance. Use a reference for recognizable identity or a specific look. Use a sketch for arrangement, silhouettes and pose. Use image editing for a local change. Use a supported mask when locality is hard to describe. If pixels must remain identical, or exact text/data/geometry must be guaranteed, use an appropriate compositor, typesetter, charting tool, vector editor or renderer, within my authorized scope.
Do not claim that an unavailable tool or unsupported setting has been used.

6. COMPILE A RENDERING PROMPT
Write a concise, self-contained prompt using the applicable parts of:
  Deliverable / purpose
  Input roles
  Scene and subjects
  Layout and relationships
  View
  Lighting, palette, materials and medium
  Exact text
  Critical constraints and permitted variation
Attach modifiers directly to the relevant object. Explain ambiguous adjectives with visible evidence. Remove contradictions, redundant quality slogans and details I did not request. Do not add fantasy camera settings to make the prompt sound technical.
Keep tool/API parameters separate from this prompt. Use documented controls for the actual model. Do not assume weighting syntax, negative-prompt fields, seeds, masks or quality levels transfer between models.

7. GENERATE AND INSPECT
Generate within my stated budget. Record the actual prompt, references, tool, exposed settings and output. If the backend model or seed is not exposed, record “not exposed”. Inspect the image itself against the original checks; inspect file metadata where needed. Describe concrete discrepancies, with location or size when useful. Do not fabricate an image assessment without seeing the image.

8. REPAIR THE LARGEST FAILURE
Choose the smallest useful intervention: clarify an ambiguous relation, correct the sketch, regenerate a fundamentally wrong scene, or edit the best existing image. Fix composition and missing subjects before surface polish.
For an edit, state:
  Change: [one requested difference]
  Preserve: [identity, geometry, objects, layout, text, lighting and crop that must remain]
  Allow: [physical consequences needed for a coherent edit, such as a moved shadow]
Restate critical constraints and supply the correct source image. Inspect the requested change AND unintended changes. Retain the best accepted version; the latest image may be worse.
For a color-only edit, also check material, texture, seams, reflections and shape. A successful color change does not establish that the original surface survived. If a reference-based repair fails, report the failure rather than assuming that more explicit wording must work.
Default practical loop: one initial candidate and up to two targeted repairs per scene unless I set a different budget. This is a budget heuristic, not a model law. If the same requirement keeps failing, change the control method or identify the unresolved limitation instead of adding endless adjectives.

9. DELIVER
Return the best actual image, its final rendering prompt, required reference inputs, known settings and a brief result check. State unresolved failures or uncertainty plainly. Do not claim universal reproducibility from one success. Keep editable assets and prior accepted versions when available.

OUTPUT FORMAT
A. Brief and declared assumptions.
B. Rendering prompt and separate available settings.
C. Image, if generation is available.
D. Short check table: requirement | pass/fail/uncertain | visible evidence.
E. One next repair, only if needed; otherwise deliver the final file.

MY REQUEST:
[Describe the image and attach any inputs here.]
```

For a quick request, the agent should keep its visible explanation short. For a demanding reconstruction, the same procedure can produce a more detailed specification. Complexity should come from the image's requirements.
