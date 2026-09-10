# Guide-derived edit/reference coverage: G10–G17

Eight initially registered demonstrations, one image each, using the built-in image generator. Every input was visually inspected before use; every output is retained unchanged. Model/backend, seed and quality were not exposed. These examples show techniques and limitations; they are not a comparison against the published guide outputs or evidence of a GPT Image 2.5 improvement. No repair is included in this initial eight-call record.

The original guide and source images were retrieved from [OpenAI’s prompting guide](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5). Reference roles, our new prompts and all criteria are logged below.

| Workflow | Observed outcome |
|---|---|
| G10 — Localize a dense fantasy atlas | All six Spanish replacements and the major layout succeed; fine illustration preservation does not fully succeed. |
| G11 — Pixel-art motorcycle megacity | A compelling style transfer with excellent scene hierarchy, but a countable structural error: three background bridges instead of two. |
| G12 — Identity-preserving wardrobe from three garment references | The four-reference wardrobe assembly succeeds at visible identity, pose, clothing and environment retention; some occluded boot hardware cannot be verified. |
| G13 — Two-reference botanical railway editorial | The person/dog reference roles and ambitious new environment integrate well. The model adds forbidden distant people and potentially readable clock markings. |
| G14 — Actual-alpha shampoo cutout | Failed production cutout: plausible bottle extraction appearance, but no real transparency at all. |
| G15 — Sketch to alpine botanical station | The simple drawing becomes a detailed alpine station with all intended additions. Main relationships transfer; geometry remains approximate. |
| G16 — Remove cap and preserve portrait | The requested local deletion works while the flower, portrait and scene remain visually consistent. |
| G17 — Insert referenced person into complex action scene | The referenced outfit and person integrate into the complex action scene while major background anchors hold. |

## G10: Localize a dense fantasy atlas

All six Spanish replacements and the major layout succeed; fine illustration preservation does not fully succeed.

[Retained output](g10.png) · 1024 × 1536 PNG (RGB).

### Input roles

- `trial-N4.png`: edit target: illustration, geometry, material and typography layout; local generated artifact.

### Prompt fixed before generation

```text
Edit image 1, the complete Rain Engine poster. It is the exact layout and illustration target; do not redesign it.

Change only its six text strings using this complete Spanish glossary:
THE RAIN ENGINE → EL MOTOR DE LLUVIA
CLOUD → NUBE
FILTER → FILTRO
VAULT → DEPÓSITO
GARDEN → JARDÍN
RETURN → RETORNO

Print every replacement exactly once, with the accents shown. Preserve the existing title position, each label's left alignment and baseline, serif character, dark teal ink and hierarchy. Reduce type size or tracking only as necessary to fit each replacement into its current text zone; shorten a leader line only if the longer label requires room.

Lock everything else: the portrait 2:3 canvas, five floating tiers, exactly three white masts, three filter layers, glass reservoir and water level, intricate garden and bridges, copper coil, cloud shapes, four downward arrows, long turquoise return arrow, all material colors, lighting and illustration geometry. No English text, extra labels, new objects, borders or watermarks. Return the translated poster.
```

### Criteria and observed evidence

- **G10-01 PASS — Title is exactly EL MOTOR DE LLUVIA, once.** EL MOTOR DE LLUVIA appears once above the stack.
- **G10-02 PASS — Labels NUBE, FILTRO, DEPÓSITO, JARDÍN, RETORNO are correct and appear once each.** NUBE, FILTRO, DEPÓSITO, JARDÍN and RETORNO appear once each with both required accents.
- **G10-03 PASS — No original English labels remain and no other text is added.** No English label remains.
- **G10-04 PASS — Five tiers stay in their original positions, sizes and order.** The five tiers remain closely aligned with the input's centers, silhouettes and order.
- **G10-05 PASS — Three masts and three filter layers remain recognizable and unchanged in count.** Three white masts and three visibly different filter layers remain.
- **G10-06 PASS — Four downward arrows and one turquoise return arrow preserve direction and route.** All four downward arrows and the external upward turquoise arrow remain in corresponding positions.
- **G10-07 FAIL — Reservoir water level, garden bridges and copper coil retain appearance.** Strict preservation fails: the reservoir's internal caustics and parts of the garden foliage were visibly redrawn, even though water level, bridges and coil remain broadly consistent.
- **G10-08 PASS — Palette, paper background and light remain visually consistent.** The cream paper and dark-teal/copper/green palette remain coherent; local surface highlights are not identical.
- **G10-09 PASS — Replacement type remains readable in its original zones without colliding with art.** All replacement labels fit their zones; the longer reservoir label shortens its leader line.
- **G10-10 PASS — Canvas remains portrait 2:3; dimensions and any material changes are reported.** Actual output is 1024×1536 PNG, matching the source dimensions.

### Next step, if needed

For a print master with exact image preservation, localize text in an editable source or deterministic layout layer. If another generative attempt is acceptable, isolate the text regions and explicitly compare untouched regions afterward; no such repair was run here.

Uses the first language-trial image as a read-only input; the language experiment and its files remain immutable.

## G11: Pixel-art motorcycle megacity

A compelling style transfer with excellent scene hierarchy, but a countable structural error: three background bridges instead of two.

[Retained output](g11.png) · 1536 × 1024 PNG (RGB).

### Input roles

- `pixels.webp`: style only: palette, pixel clusters and edge treatment; [public source](https://developers.openai.com/images/platform/guides/image-prompting/pixels.webp).

### Prompt fixed before generation

```text
Use image 1 only as a visual-style reference. Extract its crisp square pixel clusters, stepped diagonals, small restricted color ramps, near-black negative space, bright cobalt/cyan, warm orange-yellow highlights and restrained magenta stars. Do not copy its words, spacecraft, planets, layout, scores, menus or logos.

Create a new landscape 3:2 illustrated game-poster scene called NIGHT COURIER. Foreground: exactly one motorcycle with two clearly visible wheels, ridden by one courier in a red jacket and ivory full-face helmet, crossing a narrow elevated bridge from left to right. Both gloved hands meet the handlebars and the boots meet the foot pegs. Show the whole motorcycle and rider, occupying the lower middle of the frame.

Middle ground: a dense rain-soaked market city built over a deep canal, with stacked shop awnings, hanging lanterns, service pipes and a few small moored boats. Background: tall cobalt towers and two arched skybridges disappearing into wet night haze. Use three clear depth layers so the foreground silhouette reads immediately. Render rain, warm window lights and cyan reflections as deliberate pixel clusters, not smooth photographic effects.

Place NIGHT COURIER exactly once in bold readable pixel lettering inside the upper-left sky area. No other letters, HUD, numbers, watermark or border. Keep all important content within a 5% margin. The result must be coherent detailed pixel art, without antialiased vector edges, painted blur, or a photograph underneath.
```

### Criteria and observed evidence

- **G11-01 PASS — Landscape 3:2 canvas.** Actual output is 1536×1024 PNG.
- **G11-02 PASS — Exactly one courier and one motorcycle; both wheels visible.** One courier rides one motorcycle; both wheels are visible.
- **G11-03 PASS — Rider has red jacket and ivory full-face helmet.** Red jacket and ivory full-face helmet are clear.
- **G11-04 UNCERTAIN — Hands and boots plausibly connect to bike controls.** The near hand and boot connect plausibly; far-side controls and limbs are occluded, so all contacts cannot be verified.
- **G11-05 PASS — Foreground bridge, middle canal market and distant towers read as separate depth layers.** Foreground bridge and rider, midground market/canal, and distant cobalt towers are clearly separated.
- **G11-06 FAIL — Two background arched skybridges are visible.** Three arched background bridges are visible at different heights instead of the requested two.
- **G11-07 PASS — Style is visibly pixel art with stepped edges and restrained color ramps.** Edges, lettering and reflections use deliberately blocky pixel clusters.
- **G11-08 PASS — Reference palette is recognizable while source spaceships, planets and game interface are absent.** Blue/cyan and orange-yellow palette transfers; source spacecraft, planet and game menu are absent.
- **G11-09 PASS — NIGHT COURIER appears once and no other readable text or numbers appear.** NIGHT COURIER is spelled correctly, once; no other readable text is visible.
- **G11-10 PASS — Main subject is fully framed inside margins; rain/light do not obscure it.** The full rider/motorcycle is visible and separated from busy background detail.

### Next step, if needed

Give the three current bridges stable IDs, choose the surplus one with a visual map, and remove only that bridge while preserving the other two and the motorcycle. A cleaner next brief would state both desired bridge locations explicitly. These are proposed repairs, not tested outcomes.

## G12: Identity-preserving wardrobe from three garment references

The four-reference wardrobe assembly succeeds at visible identity, pose, clothing and environment retention; some occluded boot hardware cannot be verified.

[Retained output](g12.png) · 1024 × 1536 PNG (RGB).

### Input roles

- `woman-in-museum.webp`: edit target, identity, pose, environment; [public source](https://developers.openai.com/images/platform/guides/image-prompting/woman-in-museum.webp).
- `jacket.webp`: blazer garment only; [public source](https://developers.openai.com/images/platform/guides/image-prompting/jacket.webp).
- `tank-top.webp`: tank garment only; [public source](https://developers.openai.com/images/platform/guides/image-prompting/tank-top.webp).
- `boots.webp`: boots garment only; [public source](https://developers.openai.com/images/platform/guides/image-prompting/boots.webp).

### Prompt fixed before generation

```text
Image 1 is the edit target and sole person/environment reference: the smiling dark-haired woman standing with folded arms and crossed ankles in the museum. Images 2, 3 and 4 are garment references only: the beige blazer, white scoop-neck tank top, and gray knee-high suede boots.

Replace her knitted sweater and white sneakers with an outfit assembled from those garments. Put the beige blazer from image 2 over the white tank from image 3, leaving the blazer open enough to see the tank. Match the blazer's beige fabric, notched lapels, two dark front buttons and flap pockets; adapt its drape to her existing folded-arm pose. Put the gray boots from image 4 on both feet, over her existing black jeans, retaining the suede texture, low heels, knee-high shafts and two buckle straps on each boot.

Preserve image 1's facial features, apparent age, smile, skin texture, black shoulder-length hair and earrings. Keep the folded arms, crossed ankles, body proportions, camera viewpoint, full-body framing and museum lighting. Preserve her black jeans wherever not naturally covered by blazer or boots. Keep the marble statue on the left, both gold-framed paintings on the right, floor tiles and background geometry in place. Clothing may create natural new folds, occlusions and contact shadows; do not change her anatomy to simplify the fit. No extra people, accessories, labels, logos or beauty retouching. Portrait 2:3.
```

### Criteria and observed evidence

- **G12-01 PASS — Recognizable facial likeness, smile, hair and earrings from the original; no identity verification claim.** The dark-haired woman retains a closely similar face, smile, hair length and visible earrings; this is visual likeness assessment.
- **G12-02 PASS — Folded arms and crossed-ankle pose preserved with plausible anatomy.** Folded arms and crossed ankles are preserved with plausible garment occlusions.
- **G12-03 PASS — Beige blazer matches lapels, two dark buttons, flap-pocket character and open fit.** Beige open blazer has notched lapels, two dark front buttons and flap pockets.
- **G12-04 PASS — White scoop-neck tank visible under blazer.** White scoop-neck tank is visible under the open blazer.
- **G12-05 PASS — Two gray knee-high suede boots replace both sneakers.** Both original white sneakers are replaced with gray high boots.
- **G12-06 UNCERTAIN — Boots preserve low heels and two buckle straps on each boot, insofar as visible.** Low heels and gray suede are visible; two buckle straps are clear on the rear boot, but the front boot's upper buckle cannot be verified from its rotated/occluded view.
- **G12-07 PASS — Original black jeans remain wherever not covered by replacement clothes.** Black jeans remain between blazer and boots, adapted to the boot occlusion.
- **G12-08 PASS — Statue, paintings and floor remain in their original arrangement.** The statue, two gold-framed paintings and tile layout remain closely consistent.
- **G12-09 PASS — New garments fit body and lighting with plausible folds and contact shadows.** Blazer sleeves, lapels and boot shafts follow the existing pose; lighting is coherent.
- **G12-10 PASS — No extra people/accessories/text; portrait 2:3 and full-body framing preserved.** Full body remains framed at 1024×1536 with no extra person, text or accessory.

### Next step, if needed

If exact garment hardware matters, evaluate a second requested pose or a detail view, or adjust only the named boot detail. Do not treat a hidden buckle as a confirmed match.

## G13: Two-reference botanical railway editorial

The person/dog reference roles and ambitious new environment integrate well. The model adds forbidden distant people and potentially readable clock markings.

[Retained output](g13.png) · 1536 × 1024 PNG (RGB).

### Input roles

- `test-woman.webp`: woman identity and outfit only; [public source](https://developers.openai.com/images/platform/guides/image-prompting/test-woman.webp).
- `test-woman-2.webp`: dog donor only; exclude donor woman/background; [public source](https://developers.openai.com/images/platform/guides/image-prompting/test-woman-2.webp).

### Prompt fixed before generation

```text
Reference roles are strict. Image 1 supplies only the woman: her face, long brown hair, dark navy cap, blue-white plaid overshirt, black cropped tank, ripped blue jeans, black belt and white sneakers. Image 2 supplies only the chocolate-brown Labrador dog: broad face, amber-brown eyes, floppy ears, dark brown short fur and stocky proportions. Do not use the second woman's identity, clothes or pose. Neither image supplies the new background.

Create a photorealistic landscape 3:2 travel editorial inside a spectacular glass-roofed botanical railway concourse at late golden hour. The woman from image 1 walks toward the camera slightly left of center, full body visible. The Labrador from image 2 walks beside her on the viewer's right, full body visible, on a slack burgundy leash held in her left hand (the hand on the viewer's right). Keep her reference outfit intact. Adapt the dog's posture to walking while preserving its recognizable appearance.

Behind them, show a soaring iron-and-glass barrel vault, layered tropical palms in bronze planters, an ornate station clock without readable numerals, and the front of a deep moss-green vintage train on the right. Warm sun shafts cut through the glass and reflect on a wet black-and-ivory tiled floor. Keep architectural lines in a coherent perspective, with the woman and dog sharper than the distant roof and train. Ground all feet and paws with matching contact shadows and reflections.

Exactly one woman and one dog; no crowd or second donor person. No floating leash, merged limbs, duplicate paws, extra animals, readable signage, logos or watermarks. Preserve natural face and fur texture; this should feel like a detailed travel photograph, not a cut-and-paste collage.
```

### Criteria and observed evidence

- **G13-01 FAIL — Exactly one woman and one chocolate Labrador; no donor woman or extra animals.** The foreground correctly contains the specified woman and Labrador, but two tiny background human figures appear in the distant concourse despite the exactly-one-person requirement.
- **G13-02 PASS — Woman resembles image 1 and retains cap, plaid shirt, black top, ripped jeans, belt and white sneakers.** The first woman's cap, plaid shirt, black crop top, ripped jeans, belt and white sneakers transfer with recognizable facial appearance.
- **G13-03 PASS — Dog resembles the image 2 Labrador in face, ears, color and stocky proportions.** The Labrador retains chocolate fur, broad face, floppy ears and amber-brown eyes; walking pose differs as requested.
- **G13-04 PASS — Both subjects walk toward camera, woman left of center and dog on viewer right.** Woman is left of center and the dog on viewer's right, both walking toward camera.
- **G13-05 PASS — Burgundy leash connects dog to the correct visible hand without floating segments.** The burgundy leash runs continuously from her left hand to the dog's collar.
- **G13-06 PASS — Full bodies, feet and paws are visible and anatomically plausible.** Whole bodies, shoes and paws remain visible; the walking contacts look plausible.
- **G13-07 PASS — Iron-and-glass vault, palms and bronze planters create layered botanical concourse.** Glass barrel vault, layered palms, bronze planters and reflected sunlight are prominent.
- **G13-08 PASS — Moss-green vintage train is behind them on the right; ornate clock is present.** Moss-green train occupies the right background; ornate clock is present.
- **G13-09 PASS — Light, scale, ground contacts and reflections make the composite coherent.** Subject scale, warm light, tiled-floor contacts and reflections are coherent.
- **G13-10 UNCERTAIN — Landscape 3:2 with no legible signage, logos or watermarks.** 1536×1024 landscape output. Tiny train markings are not confidently legible; the clock has numeral-like marks despite the prompt's no-readable-numerals request.

### Next step, if needed

Use a mapped deletion pass for the two distant people and replace the clock face with unnumbered hour ticks, leaving the foreground subjects and leash locked. No cleanup pass was run in this eight-call demonstration.

## G14: Actual-alpha shampoo cutout

Failed production cutout: plausible bottle extraction appearance, but no real transparency at all.

[Retained output](g14.png) · 1254 × 1254 PNG (RGB).

### Input roles

- `shampoo.webp`: exact product identity and typography; [public source](https://developers.openai.com/images/platform/guides/image-prompting/shampoo.webp).

### Prompt fixed before generation

```text
Image 1 is the exact product to extract. Return a square PNG cutout with genuine transparent alpha outside the bottle. Remove the wooden tabletop, tan wall, and cast shadow completely; do not replace them with white, gray, black, a checkerboard pattern, or a painted transparency effect.

Preserve the single peach-orange shampoo bottle, its rounded shoulder, cylindrical body, flip-top cap, front-facing orientation and warm product shading. Preserve its printed black label faithfully: WOMEN; SHAMPOO; FOR; NORMAL HAIR; 12 FL OZ (355 mL). Keep the existing typography and line positions rather than redesigning packaging. Retain the whole cap and bottom silhouette, centered with a small transparent margin. Keep opaque bottle interiors opaque and fine edge antialiasing natural. No extra objects, text, drop shadows or reflections outside the bottle.
```

### Criteria and observed evidence

- **G14-01 FAIL — PNG has an alpha channel with genuinely zero-alpha exterior pixels (metadata).** 1254×1254 RGB PNG; no alpha channel or transparency metadata. Converted alpha extrema are [255,255].
- **G14-02 FAIL — Background is transparent rather than opaque checkerboard or solid fill.** The checkerboard is painted into opaque pixels. Transparent pixel count is 0 of 1,572,516 and all four corners have alpha 255.
- **G14-03 PASS — Bottle interior is opaque and whole bottle silhouette retained.** Bottle body remains opaque and its cap-to-base silhouette is whole.
- **G14-04 PASS — Peach-orange color, cylindrical body, rounded shoulder and flip-top cap preserved.** Peach-orange cylindrical bottle, rounded shoulder and flip-top cap remain recognizable.
- **G14-05 PASS — WOMEN and SHAMPOO labels retained with exact spelling.** WOMEN and SHAMPOO are legible and spelled correctly.
- **G14-06 PASS — FOR, NORMAL HAIR and 12 FL OZ (355 mL) remain correctly spelled and positioned.** FOR, NORMAL HAIR and 12 FL OZ (355 mL) remain legible and correctly spelled.
- **G14-07 PASS — No tabletop, wall, cast shadow or other object remains.** Original table, tan wall and cast shadow are removed, but replaced by an unusable opaque checkerboard.
- **G14-08 FAIL — Square canvas, centered bottle and transparent margin.** The canvas is square and bottle centered, but its margin is not transparent.
- **G14-09 PASS — Edge shape is clean without obvious missing cap/body or fringe.** The bottle edge is visually clean; this does not compensate for failed alpha.

### Next step, if needed

Use a tool path with an actual transparent-background/output-alpha control, or a background-removal/mask operation that preserves the product pixels, then recheck the saved PNG. Another phrasing alone is not evidence of a fix. This backend exposed no alpha-setting argument and no repair was attempted.

Transparent appearance in a viewer is insufficient; alpha distribution and corner pixels must be inspected.

## G15: Sketch to alpine botanical station

The simple drawing becomes a detailed alpine station with all intended additions. Main relationships transfer; geometry remains approximate.

[Retained output](g15.png) · 1536 × 1024 PNG (RGB).

### Input roles

- `drawings.webp`: layout and perspective only; no bridge exists in source; [public source](https://developers.openai.com/images/platform/guides/image-prompting/drawings.webp).

### Prompt fixed before generation

```text
Image 1 is a composition sketch only. Its black lines are layout marks, not objects or the final visual style. Build a photorealistic landscape 3:2 alpine botanical research station from this map.

Preserve these spatial anchors: two mountain slopes descend from the upper left and upper right into the central distant valley; a winding river begins near the middle horizon and broadens in S-curves toward the lower foreground; one large leafy tree stands on the right foreground bank; scattered smooth rocks trace the river edges. Keep the river banks and large tree close to their sketched positions and relative scale. Convert the central drawn sun into natural sunrise glow in the same valley opening, rather than a giant solid disc. Four loose cloud groups occupy the upper sky where the sketch indicates them.

Intentional additions, not features recovered from the sketch: put exactly three low glass greenhouses on planted stone terraces on the left riverbank, in the middle distance. Add one slender wooden footbridge across the river in the middle distance, below the valley opening and behind the foreground tree. Connect the greenhouses to the bridge with one gravel footpath. Keep the river open and visible around and beneath the bridge.

Render lush alpine specimen gardens, dew on meadow grasses, weathered stone retaining walls, detailed greenhouse metal frames and glazing, distant snow traces on rocky mountain ridges, clear turquoise river water over visible stones, and soft low sunlight with cool valley haze. Retain a spacious sky and deep layered distance. No labels, drawn outlines, cartoon sun rays, extra bridges, large buildings or people. The final scene must follow the sketch's main layout while looking like a plausible high-resolution landscape photograph.
```

### Criteria and observed evidence

- **G15-01 PASS — Landscape 3:2 framing preserved.** Actual output is 1536×1024 PNG, the source sketch's 3:2 aspect ratio.
- **G15-02 PASS — Left/right slopes frame the central valley in positions consistent with sketch.** Left and right mountain masses frame the central valley; detailed peaks rise higher than the simple source outlines.
- **G15-03 PASS — River follows comparable S-curves from central horizon toward broad foreground.** The river runs from the central distance through broad foreground S-curves.
- **G15-04 UNCERTAIN — One prominent leafy right-bank foreground tree remains near its source position.** One prominent leafy tree occupies the right foreground bank, but its canopy is larger and higher than the sketched tree, so precise scale/placement preservation is uncertain.
- **G15-05 PASS — River rocks and banks remain visible; no blockage of primary water path.** Rocky banks and the water path remain visible.
- **G15-06 PASS — Natural sunrise glow occupies valley opening without drawn rays or giant cartoon disc.** A natural low sun and warm valley glow replace the cartoon semicircle/rays.
- **G15-07 PASS — Four loose cloud groups occupy broadly corresponding upper-sky regions.** Four principal cloud clusters occupy upper-left, inner-left, inner-right and upper-right areas; additional small horizon haze appears.
- **G15-08 PASS — Exactly three low glass greenhouses on planted left-bank terraces.** Exactly three separate low glass greenhouses sit on the planted left terraces.
- **G15-09 PASS — Exactly one new wooden midground footbridge spans river and connects to greenhouse path.** One wooden footbridge crosses the river in the middle distance with a connecting path; this was declared a new feature before generation.
- **G15-10 PASS — Photographic materials and coherent atmospheric depth; no labels/black outlines/people.** Glass, stone, foliage and river are photographic in treatment, with layered haze and no labels/outlines/people.

### Next step, if needed

For tighter geometry, add a clean layout sketch or region map with the accepted tree bounds and river contour. Keep geometry approval separate from realism. No further rendering was done here.

The inspected source has no bridge. Bridge and station are declared additions. This is reference-image sketch conditioning, not a verified native ChatGPT Sketch UI test.

## G16: Remove cap and preserve portrait

The requested local deletion works while the flower, portrait and scene remain visually consistent.

[Retained output](g16.png) · 1024 × 1536 PNG (RGB).

### Input roles

- `man-with-blue-hat.webp`: edit target; cap removal only; [public source](https://developers.openai.com/images/platform/guides/image-prompting/man-with-blue-hat.webp).

### Prompt fixed before generation

```text
Edit image 1 by removing only the blue baseball cap. The cap is the sole deletion target, including its crown and brim. Reconstruct only the newly exposed scalp with plausible short dark hair that connects naturally to the hair already visible at the temples. The hidden original hairstyle is unknown; do not change the visible face to invent a new person.

Preserve the man's facial features, smile, teeth, stubble, ears, gaze, head tilt and skin texture. Preserve the white daisy with yellow center, its green stem, the fingers holding it, the hand pose and arm. Preserve the white T-shirt, green pine-tree graphic, fabric folds, colorful graffiti brick wall, background texture, original crop, camera view, light and color. Do not remove the flower, beautify the face, alter the shirt graphic, clean the wall, add text or change any other object. Keep the original portrait 2:3 composition.
```

### Criteria and observed evidence

- **G16-01 PASS — Blue cap crown and brim fully absent.** Blue cap crown and brim are absent.
- **G16-02 PASS — Newly exposed scalp has plausible short dark hair continuous with visible temple hair.** Short dark hair fills the newly visible scalp and connects plausibly to temple hair.
- **G16-03 PASS — Facial likeness, smile, teeth, stubble, ears and head tilt remain recognizable.** Smile, stubble, teeth, ears, gaze and head tilt remain closely recognizable, although fine skin/stubble pixels are regenerated.
- **G16-04 PASS — White daisy, yellow center and green stem retained in same position.** Daisy's white petals, yellow center, stem and position are retained.
- **G16-05 PASS — Hand, fingers and arm retain pose and plausible anatomy.** The hand's flower-holding pose and arm remain plausible and in place.
- **G16-06 PASS — White shirt and green tree graphic preserved.** White T-shirt and central green tree graphic are retained.
- **G16-07 PASS — Graffiti bricks, framing, light and colors stay visually consistent.** Graffiti and brick pattern, crop and lighting remain closely consistent.
- **G16-08 PASS — No added text or objects; portrait 2:3 retained.** Actual output is 1024×1536 PNG with no added object or text.

### Next step, if needed

No further image edit is warranted for the demonstrated brief. The invented hair is plausible completion of occluded content, not proof of the unseen original hairstyle.

Task intentionally removes the cap; the guide removes a different object. Reconstructing occluded hair is an inference, not recovery of unseen pixels.

## G17: Insert referenced person into complex action scene

The referenced outfit and person integrate into the complex action scene while major background anchors hold.

[Retained output](g17.png) · 1024 × 1536 PNG (RGB).

### Input roles

- `g12.png`: person identity and clothing only; generated G12 result; local generated artifact.
- `scene-gpt-image-2-5-sunburst.webp`: scene, existing runner pose, scale, camera, lighting; [public source](https://developers.openai.com/images/platform/guides/image-prompting/scene-gpt-image-2-5-sunburst.webp).

### Prompt fixed before generation

```text
Image 1 supplies the person and clothing only: the dark-haired woman in beige blazer, white tank top, black jeans and gray knee-high boots. Image 2 is the exact scene, camera and action-pose reference: a runner escaping a bear through a mountain campsite. Replace image 2's existing runner with the woman from image 1 so there is still exactly one person. Do not add a second person and do not copy the museum background.

Preserve the referenced woman's facial structure, apparent age, dark hair and recognizable identity while giving her a natural alarmed expression. Preserve her beige blazer, white tank, black jeans and gray boots from image 1; add only plausible motion folds and a light amount of trail dust. Adapt her body to image 2's running pose, direction and scale, with one knee raised and arms moving naturally. Her face must remain visible and her footwear must meet the terrain plausibly.

Lock the rest of image 2: the pursuing brown bear on the left, damaged gray tent and green storage case on the right, overturned dark camp chair on the left, scattered gear, pine trunks, rocky leaf-strewn ground, distant granite mountain profile and warm evening sky. Match the existing scene's depth of field, perspective, muted natural colors, lighting and grounded contact shadows. Maintain the original portrait 2:3 framing. Keep the image photographically credible; no dramatic new explosions, extra wildlife, wounds, blood, text, logos or watermark.
```

### Criteria and observed evidence

- **G17-01 PASS — Exactly one person replaces the original runner; no museum background.** Exactly one woman occupies the original runner's position; no museum content appears.
- **G17-02 PASS — Face/hair show recognizable likeness to G12 reference with plausible alarmed expression.** Face/hair remain recognizably consistent with G12 while expression becomes alarmed; resemblance is an observational judgment.
- **G17-03 PASS — Beige blazer, white tank, black jeans and gray boots retained.** Beige blazer, white tank, black jeans and visible gray high boot transfer; the far leg is partly occluded by the running pose.
- **G17-04 PASS — Running pose, direction and scale fit original scene without malformed limbs.** Forward-running pose, raised knee, arm swing, body scale and direction follow the source action.
- **G17-05 PASS — Bear stays behind on left, retaining plausible scale and appearance.** Bear remains behind on the left.
- **G17-06 PASS — Tent and green case remain on right; overturned chair remains on left.** Tent and green case stay right; overturned dark chair stays left.
- **G17-07 PASS — Scattered gear, pine trunks and foreground ground arrangement preserved.** Scattered gear, trees and rocky leaf-strewn foreground retain their arrangement, with fine texture redraws.
- **G17-08 PASS — Granite mountain profile, sky and background depth retain source arrangement.** Distant granite peak profile and evening sky remain closely consistent.
- **G17-09 PASS — Light, contact shadows, focus and integration remain coherent.** Subject clothing, motion and scene lighting integrate coherently; dust is heavier than the brief's light-dust suggestion.
- **G17-10 PASS — Portrait 2:3 with no extra wildlife, blood, text or watermark.** Actual output is 1024×1536 PNG; no extra wildlife, blood, text or watermark.

### Next step, if needed

If clothing cleanliness matters, isolate the muddy jeans/blazer regions for a dust reduction edit. For this demonstration the main replacement and background constraints are satisfied; no additional pass was run.

G12 output is a planned dependency; it must be visually inspected before G17 submission. Official source scene already includes a runner, so this is replacement/compositing rather than an empty-scene insertion.

## What these trials establish

Named reference roles can support rich new compositions and tightly scoped edits. They do not guarantee exact counts, background exclusion, fixed pixels or file properties. The pixel scene missed an explicit bridge count; the train scene added distant people; the translated atlas redrew some untouched texture; the product export painted a checkerboard instead of supplying alpha. Those are visible, retained failures, not discarded samples. The next useful action depends on which requirement failed: local cleanup, a stronger spatial map, a source-layer edit, or an actual output-format control.
