# Experiment record

Eight image-generation/edit calls across three workflows, plus one original code-drawn sketch. Conducted 10 September 2026. All eight outputs were visually inspected. Every generated output is a 1536×1024 PNG; the original sketch is 1200×800.

The built-in image_gen tool did not expose its backend model name, seed or quality setting. These are workflow demonstrations, not a controlled comparison of Flare and Sunburst or proof that the method generalizes to every subject. B1/B2 use the same text with different image inputs, but lack repeated trials and a controlled seed. The same assistant wrote and assessed the prompts and had seen the original creation brief before reconstructing it. No independent judge was used.

The protocol below was written before the first image call. Geometry descriptions remain approximate unless a strict measurement is explicitly stated. A hard failure is retained in the record even if the output looks attractive.

## Outcomes

| Call | Task | Result against the requested constraints |
|---|---|---|
| A1 | Product image from text | Fail: correct objects, but the mug intrudes into reserved space and sits above the permitted lower region. |
| A2 | Repair composition | Pass original object and layout requirements; approximate scaling was not an exact transform. |
| B1 | Reconstruct A2 from a written observation brief | Pass original scene checks; changed silhouettes, proportions and placement limit reference fidelity. |
| B2 | Same brief with A2 attached | Pass original scene checks; closer reference fidelity in this single example, with remaining differences. |
| C1 | Render original room sketch | Recognizable arrangement; fail the explicit exclusion of plants because of outdoor foliage. Geometry remains approximate. |
| C2 | Remove foliage through window | Requested correction passes; approximate sketch geometry remains. Accepted source for further edits. |
| C3 | Change blue upholstery to orange | Color change passes; preservation fails because the fabric pattern becomes substantially more conspicuous. |
| C4 | Repair fabric using C2 as a texture reference | Fail: the conspicuous fabric pattern remains. Stop this branch and retain C2. |

The local sequence produced accepted product and blue-room images. It did not produce an accepted orange-room image under the strict fabric-preservation requirement. That failure is part of the result.

The pre-generation protocol distinguishes approximate sketch geometry from exact geometry. Some detailed prompt requirements, including the plant exclusion, were added before the corresponding call and are checked in the reviews. The room workflow contains one initial render, one new color-change objective and two corrections. The color correction did not succeed, so no further generation was performed.


## Original protocol

### Protocol saved before generation

Date: 2026-09-10. This is a small illustrative workflow test, not a benchmark or claim of universal reliability.
Generator: built-in image_gen tool. Record backend/model if returned; otherwise unknown. No seed or explicit quality controls are exposed by this tool.
Method: author requirements before generating, inspect actual outputs, record failures and every revision. Use independent text generation, reference-conditioned generation, sketch-conditioned rendering, and a localized edit. These conditions differ in information supplied; this is not a controlled causal study of wording.

## Test A: original product image
3:2 landscape. One matte teal mug on one low coral rectangular plinth on left. Handle points image-right. Two whole yellow lemons sit on ivory floor to its right. One plain silver teaspoon lies horizontally in front of plinth. All main objects below y=45%; top 35% empty. Soft light from upper left, shadows toward lower right. No text, logos or other props.
Hard checks: (A1) 3:2 canvas; (A2) exactly one teal mug and one coral plinth; (A3) mug handle right; (A4) exactly two whole lemons to right, off plinth; (A5) one horizontal spoon in front; (A6) top 35% free of objects/text; (A7) no extra objects or text. Soft checks: matte versus glossy distinction, gentle shadows, spatial balance. Verify dimensions from file metadata separately.

## Test B: recreate A from observation
Analyze A as a reference. Record observed geometry and approximate object boxes in normalized image coordinates; label inferred materials/light and unknown physical camera settings. Generate B1 using the observation-only brief and no image, then B2 using the same brief with A as the reference. This analyst has seen A's original prompt, so this is not blind reverse engineering. Compare silhouettes, placement, relative scale, colors and negative space. Do not claim exact pixel recovery. Both results get the original A hard checks plus visual reference comparison.

## Test C: sketch to room render and targeted edit
Create an original schematic 3:2 sketch: front wall, floor boundary y=60%; one square window upper-left; one two-seat sofa right; one round coffee table front-center-left; one floor lamp at far right; one broad floor rug. The sketch fixes placement and relative scale, not line style. Render warm neutral plaster, cobalt-blue sofa, walnut table, off-white rug, black lamp; daylight from window. Hard checks: canvas ratio; all five named items; correct left/right positions; cobalt sofa initially; round table; no annotations, people or additional furniture. Soft checks: approximate sketch geometry and plausible room shadows.
Then change sofa fabric only from cobalt to burnt orange, allowing corresponding local color reflections and shading. Preserve wall/window/table/lamp/rug, sofa shape, camera, crop and layout. Inspect both requested change and unwanted drift. Pixel identity is not assumed.

## Loop and stopping
Brief -> choose control input -> generate -> inspect each requirement -> fix highest-impact failure -> inspect again. Missing/uncertain required detail is not a pass. Keep best accepted image. One targeted correction per iteration; maximum two corrections per case before switching control method or documenting unresolved limits. End once examples demonstrate all three requested workflows and at least one real generation/edit feedback cycle. No extrapolation from these examples to arbitrary subjects.


## A1: generate

Output: `images/a1-original-draft.png` — 1536×1024 PNG.

Input images: none.

Exact submitted prompt:

```text
Create a photorealistic studio product image for a website hero, landscape canvas 3:2. On a seamless warm ivory floor and background, place one matte teal ceramic mug on one low coral rectangular plinth, in the left half. The mug handle points to image-right. Place exactly two whole yellow lemons on the ivory floor to the right of the plinth; they are separate, touching neither mug nor plinth. Place one plain silver teaspoon horizontally on the floor in front of the plinth, bowl to image-left. Keep every object fully visible in the lower 55% of the frame. Leave the upper 35% as uninterrupted empty ivory background for a headline to be added later; do not generate the headline. Slightly elevated front view, enough to see the mug opening and the top of the plinth. Broad soft light from upper left; gentle contact shadows extend toward lower right. Real ceramic, subtly textured lemon rind and brushed silver; quiet, uncluttered composition. Only the mug, plinth, two lemons, and spoon. No writing, logos, decorative props or borders.
```

Actual output inspected. Landscape 1536x1024 PNG, subsequently verified from file metadata. Correct one teal mug, coral plinth, right handle, two separate lemons on floor, one spoon in front, no extra props/text. FAIL composition/negative space: mug top at approximately y=338/1024=33%, intruding into the requested clear top 35%; also does not keep all objects in the lower 55%. The output is attractive but should not be accepted against this brief. Fix only composition: reduce group scale to ~80%, move it to lower portion, preserve object relationships and appearance.


## A2: edit

Output: `images/a2-layout-repaired.png` — 1536×1024 PNG.

Input images: `images/a1-original-draft.png`.

Exact submitted prompt:

```text
Edit the input product photograph. Change only the composition scale and placement: make the entire existing still-life arrangement about 80% of its current size in the frame, then position it so every object lies between 46% and 90% of the image height measured from the top. The upper 45% must be completely empty ivory background. Keep the 3:2 landscape canvas. Preserve the exact mug design and teal color, right-facing handle, low coral rectangular plinth, exactly two whole yellow lemons to the plinth's right, and one horizontal silver teaspoon in front with bowl at left. Keep the same relative positions and proportions within the arrangement, materials, perspective, soft upper-left illumination and ivory backdrop. Maintain natural contact shadows. No new objects or text.
```

Actual returned image inspected. The mug begins at roughly 49% of image height; all objects end by ~86%. All original A requirements now pass visually; file metadata subsequently confirmed 1536x1024 PNG. The requested approximate 80% scaling was not exact: the arrangement is closer to 70% of original width. That percentage was a corrective cue, not an original acceptance criterion. This supports accepting the required negative space while avoiding a claim of exact numeric model control.

Reference analysis for B: composition and objects directly observed. Material labels and light source inferred from visual appearance. Actual camera lens/focal length/exposure unknown. Normalized approximate boxes were hand estimated from the visible image, not detector measurements. B comparisons are non-blind because the analyst has seen the original creation prompt.


## B1: generate

Output: `images/b1-text-reconstruction.png` — 1536×1024 PNG.

Input images: none.

Exact submitted prompt:

```text
Create a photorealistic studio still life on a 3:2 landscape canvas. If an image is supplied, use it as the authority for composition, silhouettes, proportions, colors and lighting. Reconstruct the following visible scene: a warm ivory seamless floor and background, gently brighter at upper left. The upper 49% of the canvas is empty. One teal cylindrical ceramic mug with slightly rounded base and thick circular loop handle pointing image-right sits on a low salmon-coral rectangular block in the lower-left-middle. See inside its dark teal opening from a slightly elevated front view. Approximate object bounding boxes, expressed as percentages from the top-left of the canvas: mug including handle x30–49, y49–72; block x23–50, y66–79. The block has a broad front face and a visible flat top. Two whole saturated yellow lemons rest on the floor to the block's right, with a gap from the block: the nearer left lemon at x55–67,y66–81 and the farther right lemon at x67–79,y63–77. Their long axes lean gently down toward image-right; preserve small pointed tips and detailed dimpled rind. One horizontal silver teaspoon lies below and in front of the block at x29–54,y80–86, with oval bowl at image-left and a slightly curved slender handle toward image-right. Soft upper-left illumination makes the left side of the mug lighter; soft contact shadows fall to lower right. Matte finely textured ceramic and block, subtly reflective silver, natural lemon texture. No visible horizon, text, logos, borders or other objects. Every object is fully visible; preserve the broad empty space and modest size of the arrangement.
```

The written observation brief produced the right overall content and arrangement. All original A hard checks pass visually. Reference differences: thinner mug handle and changed mug proportions/rim, a larger/taller-looking block relative to mug, smaller spoon bowl and changed spoon handle, and changed lemon positions/sizes. The empty upper region remains. This is a credible semantic/compositional reconstruction, not an identical product or scene. Do not label it an exact recreation.


## B2: reference-conditioned

Output: `images/b2-reference-reconstruction.png` — 1536×1024 PNG.

Input images: `images/a2-layout-repaired.png`.

Exact submitted prompt:

```text
Create a photorealistic studio still life on a 3:2 landscape canvas. If an image is supplied, use it as the authority for composition, silhouettes, proportions, colors and lighting. Reconstruct the following visible scene: a warm ivory seamless floor and background, gently brighter at upper left. The upper 49% of the canvas is empty. One teal cylindrical ceramic mug with slightly rounded base and thick circular loop handle pointing image-right sits on a low salmon-coral rectangular block in the lower-left-middle. See inside its dark teal opening from a slightly elevated front view. Approximate object bounding boxes, expressed as percentages from the top-left of the canvas: mug including handle x30–49, y49–72; block x23–50, y66–79. The block has a broad front face and a visible flat top. Two whole saturated yellow lemons rest on the floor to the block's right, with a gap from the block: the nearer left lemon at x55–67,y66–81 and the farther right lemon at x67–79,y63–77. Their long axes lean gently down toward image-right; preserve small pointed tips and detailed dimpled rind. One horizontal silver teaspoon lies below and in front of the block at x29–54,y80–86, with oval bowl at image-left and a slightly curved slender handle toward image-right. Soft upper-left illumination makes the left side of the mug lighter; soft contact shadows fall to lower right. Matte finely textured ceramic and block, subtly reflective silver, natural lemon texture. No visible horizon, text, logos, borders or other objects. Every object is fully visible; preserve the broad empty space and modest size of the arrangement.
```

Same prompt as B1, with A2 attached as a reference. All original A hard checks pass visually. Relative to B1, the reference-conditioned result more closely retains the mug/handle shape, block proportions, lemon placement and spoon silhouette. Differences remain in surface texture, local highlights and background/lightness; small geometry shifts remain too. This is a one-pair qualitative observation, not a statistical claim or pixel-perfect reproduction. No fixed seed, known backend model, repeated trial, or independent evaluator was available.


## C1: sketch-to-render

Output: `images/c1-sketch-render.png` — 1536×1024 PNG.

Input images: `images/c0-room-sketch.png`.

Exact submitted prompt:

```text
Use the input sketch as a layout and proportion guide for a photorealistic interior image on a 3:2 landscape canvas. The sketch's outlines control the location, relative scale, silhouettes and slightly elevated frontal viewpoint; its line drawing style should not appear in the result. Render a quiet sitting room with warm off-white plaster walls and a pale oak floor. The straight background line is where the wall meets the floor. There is one square four-pane window on the upper-left wall, one cobalt-blue upholstered two-seat sofa in the right half, one round walnut coffee table in front of the sofa and slightly left of it, one broad off-white woven rug beneath the table and sofa, and one black floor lamp with an off-white tapered shade at far right. Preserve the sofa's two back cushions and two seat cushions, simple arms and legs. The elliptical shape in the sketch is a circular tabletop seen in perspective, not an oval table. Keep the same left/right arrangement and approximate sizes shown by the sketch. Soft daylight enters through the left window, creating natural shadows to the right. The window may reveal a soft bright sky. No people, plants, artwork, books, extra furniture, text, diagrams or construction lines. Every named element should stay fully in frame.
```

The five named elements are present; the four-pane window is on the left, blue two-seat sofa right, round table front-left of sofa, floor lamp far right, rug beneath. Framing and materials look plausible. Relative layout is recognizable, but geometry is approximate: sofa and table are higher/larger than their sketch outlines; the window is slightly taller than square. Do not claim exact tracing. No text or extra indoor furniture.

An explicit exclusion failed: outdoor trees/foliage appear through the window although the prompt says no plants. The sketch did not contain these. Correct only the exterior window content before the separate upholstery edit. The corrective source should preserve all indoor objects.


## C2: edit

Output: `images/c2-window-repaired.png` — 1536×1024 PNG.

Input images: `images/c1-sketch-render.png`.

Exact submitted prompt:

```text
Edit this room image. Change only the outdoor scene visible through the upper-left window: remove all trees, greenery and foliage, replacing them with unobstructed soft pale-blue sky and a few diffuse white clouds. Keep the existing four-pane window frame, its shape, position and size unchanged. Preserve the cobalt-blue two-seat sofa, every cushion and leg, round walnut coffee table, off-white woven rug, black floor lamp and off-white shade, wall and floor materials, camera, framing, 3:2 landscape canvas, indoor lighting and interior shadows. Do not change any indoor object, add any new object, or add text.
```

The unwanted foliage is gone; pale sky/clouds fill all four panes. The room's sofa, round table, rug, lamp and layout remain visually consistent with C1. Near-square window and other geometry remain approximate relative to the original sketch. Fine surface appearance is not assumed pixel-identical. This is the chosen source for the planned upholstery color edit.


## C3: edit

Output: `images/c3-orange-edit.png` — 1536×1024 PNG.

Input images: `images/c2-window-repaired.png`.

Exact submitted prompt:

```text
Edit the supplied room photograph. Change only the sofa upholstery color from cobalt blue to a warm burnt orange, with the same tactile fabric quality. Preserve the sofa's silhouette, dimensions, two back cushions, two seat cushions, arms, seams, legs and exact position. Keep the four-pane window and pale sky, warm plaster wall, pale oak floor, round walnut coffee table, off-white woven rug, black floor lamp and off-white shade unchanged. Preserve the existing camera, perspective, framing, 3:2 landscape canvas, light direction and object placement. Allow the sofa's shading and very subtle immediately adjacent color reflections to respond naturally to the new fabric color. No new objects, greenery or text.
```

Requested burnt-orange color achieved. Sofa structure/cushion count and overall room placement remain close to C2. No greenery or extra furniture/text. Preservation failure: the upholstery has a substantially more conspicuous looped/embossed-looking pattern than the blue source; the request was color only with the same fabric quality. Visual inspection cannot establish whether the model invented a motif or amplified a subtle existing one. Either way, the visible material treatment drifted. Small surface/lighting differences also occur elsewhere, so no pixel-identity claim. One focused repair will use C3 as target and C2 only as fabric reference, maintaining orange color.


## C4: texture-repair

Output: `images/c4-texture-repair-attempt.png` — 1536×1024 PNG.

Input images: `images/c3-orange-edit.png`, `images/c2-window-repaired.png`.

Exact submitted prompt:

```text
Image 1 is the edit target: the room with the burnt-orange sofa. Image 2 is a reference ONLY for the sofa upholstery's original plain, finely brushed fabric texture; do not copy its blue color. In image 1, change only the sofa surface texture: remove the conspicuous looping, embossed or damask-like pattern and restore the plain, fine, softly brushed fabric appearance seen on the blue sofa in image 2. Keep the burnt-orange color from image 1, with natural tonal shading. Preserve all sofa geometry, seams, two back cushions, two seat cushions, arms, legs, position and silhouette. Keep the rest of image 1 unchanged: window and sky, wall, floor, lamp, coffee table, rug, lighting direction, composition and 3:2 landscape canvas. Do not add objects or text. The desired change is surface pattern only, not color or geometry.
```

FAIL the requested texture correction. The burnt-orange color, two-seat sofa and broad room arrangement survive, but the conspicuous looped/embossed-looking fabric pattern remains. The result does not visibly restore the quieter fabric treatment of C2. Providing C2 as a fabric-only reference did not solve this requirement in this attempt. No pixel-identity claim is made for any part of the scene.

Stop this branch and preserve C2 as the accepted blue-room source. C3 and C4 remain unsuccessful candidates for the stricter color-only request. A next production step would be a selective color adjustment on the original upholstery, or a supported masked edit with another preservation check; neither was performed here. The failed repair is included rather than discarded. Eight generation/edit calls total were made; the separate color-change request was a new objective, while C2 and C4 were the two corrective attempts in the room workflow.


## Supporting measurement

Pillow read the files as 1536x1024 PNG for A1, A2 and B1; original room sketch is 1200x800. A supporting color-threshold check scans the left ~52% of the image for pixels with G-R >18, B-R >15 and G>40. This is a scene-specific indicator for the teal mug, not a general object detector or perceptual similarity metric. Topmost detected teal pixels: A1 y337 (32.91%); A2 y503 (49.12%); B1 y512 (50.00%). Direct inspection confirmed that the mug is the highest foreground object in these images. The observed negative-space correction is therefore supported by both visual inspection and a simple measurement. No backend model name, seed or quality value was exposed by the generation tool.

## How the procedure changed

1. The first composition failure led to a separate reserved-space check.
2. Reconstruction exposed silhouette drift, leading to explicit similarity-versus-geometry criteria and reference roles.
3. The sketch render exposed an invented background detail; exclusions are checked even outside the main subject.
4. The color edit exposed material drift; the repair used the previous image as a fabric-only reference while retaining the new color. The repair failed, supporting the stop-and-switch rule rather than a claim that reference roles guarantee preservation.

These are changes to a practical workflow, not evidence of a learned universal prompt optimizer.
