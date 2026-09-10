# Reference ablation: operator review

Read this after recording the independent neutral-code review. The operator submitted each arm and is not blind. Every image is retained unchanged; the same fixed descriptive prompt appears in all three calls. Only input images and their declarations change. Model, seed and quality are unexposed. One candidate per arm cannot establish general reliability or statistical superiority.

| Code | Reference arm | Observation |
|---|---|---|
| T2 | person_only | Target woman's visible appearance is retained. The unreferenced dog is a plausible generic chocolate Labrador but less clearly resembles the stockier source animal. |
| R7 | dog_only | Dog appearance is close to its donor. The woman's appearance shifts toward the unwanted woman contained in that same reference image, illustrating why a role sentence may be insufficient. |
| M3 | both | This one candidate best retains the visible appearances of both intended sources together. That is an observation from this set, not an estimate of how reliably two references outperform one. |

## What is visually useful

The dog-only result still follows the requested clothing and station scene, but the generated woman takes on lighter hair, a broad toothy smile and a head tilt closer to the unwanted woman in the dog reference. The reference-role instruction did not fully isolate the donor dog. This is consistent with visual contamination; it does not prove exactly how the model used its input. A clean crop or isolated dog reference is the next concrete control to try. That repair was not run here.

The two-reference result retained both intended appearances better in this small set. The person-only result retained the woman but supplied a less source-specific dog. These are useful case observations; no percentage improvement, guaranteed identity match or sub-agent-versus-single-agent superiority follows from them.

## Confounds

- Reference count and visual information are deliberately changed, and attachment declaration text/length changes with them.
- One sample per arm, no fixed or exposed seed, unexposed model/backend/quality; no causal or general reliability claim.
- Donor dog image contains another woman; its human content may contaminate outputs despite role instructions.
- Operator knows the arm; independent parent reviewer receives neutral codes and common checks before condition key.
- Code assignment and display order use SystemRandom; generation submission order remains person-only, dog-only, both.
- The common scene brief restates G13 subject descriptors without unavailable-image pointers; compare these three arms to each other, not causally to the earlier G13 run.

## T2 — person_only

[Retained image](../reference-matrix/trial-T2.png), 1536 × 1024 PNG.

- **R01 PASS: Woman has recognizable visual likeness to the target woman source; report uncertainty rather than asserting identity.** Cap, darker brown hair, restrained closed-mouth smile and overall facial appearance remain close to the target woman source.
- **R02 UNCERTAIN: Dog has recognizable appearance of the target chocolate Labrador source; compare face, ears, coat and proportions.** The generated Labrador satisfies the text description but reads leaner, with a narrower/lighter muzzle than the target dog; exact donor resemblance is uncertain.
- **R03 PASS: No substitution or obvious identity/clothing contamination from the woman present in the dog-donor photograph.** No visible borrowing of the dog-source woman's lighter hair and broad toothy smile is apparent.
- **R04 PASS: Exactly one woman and one dog anywhere in the scene, including distant background.** One foreground woman and one dog; no confidently identifiable extra human or animal appears in the distant background.
- **R05 PASS: Woman retains navy cap, plaid overshirt, black crop top, ripped jeans, black belt and white sneakers.** All specified clothes are present, including ripped jeans and white sneakers.
- **R06 PASS: Woman walks toward camera left of center; dog on viewer right; both full bodies and plausible anatomy visible.** Both full bodies are visible with the requested positions and walking direction.
- **R07 PASS: Slack burgundy leash connects dog collar to her left hand on viewer right.** Burgundy leash connects the woman's correct hand to the dog's collar.
- **R08 PASS: Glass barrel vault, tropical palms and bronze planters create a layered botanical station.** Glass vault, palms and bronze planters are prominent.
- **R09 PASS: Moss-green vintage train is behind on right and ornate station clock is present.** The green train remains right and ornate clock is present.
- **R10 PASS: Warm golden light, wet black/ivory floor, contact shadows and reflections integrate subjects.** Golden light and reflections integrate the subjects with the wet tiled floor.
- **R11 PASS: Landscape 3:2 output; foreground subjects sharper than background.** 1536×1024 output, subjects sharper than distant architecture.
- **R12 UNCERTAIN: No legible signage, clock numerals, logos or watermark.** Clock has dark numeral-like glyphs; exact legibility is uncertain. No other clear signage or logo appears.

### Exact prompt

```text
Reference roles:
Attached image 1 supplies the woman’s identity and outfit only. Do not copy its street background. No dog reference is attached; follow the dog description in the fixed scene brief.

Fixed scene brief:
Create a photorealistic landscape 3:2 travel editorial inside a spectacular glass-roofed botanical railway concourse at late golden hour.

Main subjects: one adult woman with long brown hair, a slight natural smile, dark navy cap, blue-white plaid overshirt, black cropped tank, ripped blue jeans, black belt and white sneakers; and one stocky chocolate-brown Labrador with a broad face, amber-brown eyes, floppy ears and short dark brown fur. Use any supplied identity reference for its assigned subject, while following these same scene and content requirements.

The woman walks toward the camera slightly left of center, full body visible. The Labrador walks beside her on the viewer's right, full body visible, on a slack burgundy leash held in her left hand (the hand on the viewer's right). Keep the woman's described outfit intact. Adapt the dog's posture to walking while preserving the described or referenced appearance.

Behind them, show a soaring iron-and-glass barrel vault, layered tropical palms in bronze planters, an ornate station clock without readable numerals, and the front of a deep moss-green vintage train on the right. Warm sun shafts cut through the glass and reflect on a wet black-and-ivory tiled floor. Keep architectural lines in a coherent perspective, with the woman and dog sharper than the distant roof and train. Ground all feet and paws with matching contact shadows and reflections.

Exactly one woman and one dog; no crowd or second donor person. No floating leash, merged limbs, duplicate paws, extra animals, readable signage, logos or watermarks. Preserve natural face and fur texture; this should feel like a detailed travel photograph, not a cut-and-paste collage.
```

## R7 — dog_only

[Retained image](../reference-matrix/trial-R7.png), 1536 × 1024 PNG.

- **R01 FAIL: Woman has recognizable visual likeness to the target woman source; report uncertainty rather than asserting identity.** The woman's lighter highlighted hair, broad toothy smile and tilted head differ from the target woman source. The target woman's image was intentionally unavailable in this arm.
- **R02 PASS: Dog has recognizable appearance of the target chocolate Labrador source; compare face, ears, coat and proportions.** The dog retains the source Labrador's broader dark head, drooping ears and stockier chest.
- **R03 FAIL: No substitution or obvious identity/clothing contamination from the woman present in the dog-donor photograph.** The generated woman's hair brightness, grin and head tilt move toward the woman present in the dog-donor image despite the instruction to ignore that woman. This is observable evidence consistent with donor contamination, not proof of an internal causal mechanism.
- **R04 PASS: Exactly one woman and one dog anywhere in the scene, including distant background.** One woman and one dog; no obvious extra distant people or animals.
- **R05 PASS: Woman retains navy cap, plaid overshirt, black crop top, ripped jeans, black belt and white sneakers.** Requested cap/plaid/black top/ripped jeans/belt/white sneakers are preserved even though the person appearance shifts.
- **R06 PASS: Woman walks toward camera left of center; dog on viewer right; both full bodies and plausible anatomy visible.** Subjects occupy the requested positions and both full walking bodies remain visible.
- **R07 PASS: Slack burgundy leash connects dog collar to her left hand on viewer right.** Burgundy leash joins the correct hand to the collar.
- **R08 PASS: Glass barrel vault, tropical palms and bronze planters create a layered botanical station.** Vault, palms and bronze planter architecture are clear.
- **R09 PASS: Moss-green vintage train is behind on right and ornate station clock is present.** Green train is right and clock is present.
- **R10 PASS: Warm golden light, wet black/ivory floor, contact shadows and reflections integrate subjects.** Coherent warm light, floor contacts and reflections.
- **R11 PASS: Landscape 3:2 output; foreground subjects sharper than background.** 1536×1024 landscape; foreground subjects are more detailed than distant architecture.
- **R12 UNCERTAIN: No legible signage, clock numerals, logos or watermark.** Clock contains numeral-like dark marks; exact readable values are uncertain.

### Exact prompt

```text
Reference roles:
Attached image 1 supplies only the chocolate-brown Labrador dog’s appearance. Do not copy the woman or background from that image. No woman reference is attached; follow the woman description in the fixed scene brief.

Fixed scene brief:
Create a photorealistic landscape 3:2 travel editorial inside a spectacular glass-roofed botanical railway concourse at late golden hour.

Main subjects: one adult woman with long brown hair, a slight natural smile, dark navy cap, blue-white plaid overshirt, black cropped tank, ripped blue jeans, black belt and white sneakers; and one stocky chocolate-brown Labrador with a broad face, amber-brown eyes, floppy ears and short dark brown fur. Use any supplied identity reference for its assigned subject, while following these same scene and content requirements.

The woman walks toward the camera slightly left of center, full body visible. The Labrador walks beside her on the viewer's right, full body visible, on a slack burgundy leash held in her left hand (the hand on the viewer's right). Keep the woman's described outfit intact. Adapt the dog's posture to walking while preserving the described or referenced appearance.

Behind them, show a soaring iron-and-glass barrel vault, layered tropical palms in bronze planters, an ornate station clock without readable numerals, and the front of a deep moss-green vintage train on the right. Warm sun shafts cut through the glass and reflect on a wet black-and-ivory tiled floor. Keep architectural lines in a coherent perspective, with the woman and dog sharper than the distant roof and train. Ground all feet and paws with matching contact shadows and reflections.

Exactly one woman and one dog; no crowd or second donor person. No floating leash, merged limbs, duplicate paws, extra animals, readable signage, logos or watermarks. Preserve natural face and fur texture; this should feel like a detailed travel photograph, not a cut-and-paste collage.
```

## M3 — both

[Retained image](../reference-matrix/trial-M3.png), 1536 × 1024 PNG.

- **R01 PASS: Woman has recognizable visual likeness to the target woman source; report uncertainty rather than asserting identity.** Darker hair, cap, restrained smile and overall appearance remain close to the target woman reference.
- **R02 PASS: Dog has recognizable appearance of the target chocolate Labrador source; compare face, ears, coat and proportions.** Broad dark muzzle, amber eyes, floppy ears and stockier body remain close to the dog donor's appearance.
- **R03 PASS: No substitution or obvious identity/clothing contamination from the woman present in the dog-donor photograph.** No obvious visible donor-woman appearance substitution occurs.
- **R04 PASS: Exactly one woman and one dog anywhere in the scene, including distant background.** Exactly one woman and one dog are visible; no obvious background people or animals.
- **R05 PASS: Woman retains navy cap, plaid overshirt, black crop top, ripped jeans, black belt and white sneakers.** All named garments remain present.
- **R06 PASS: Woman walks toward camera left of center; dog on viewer right; both full bodies and plausible anatomy visible.** Requested left/right arrangement, forward walk and full bodies are present.
- **R07 PASS: Slack burgundy leash connects dog collar to her left hand on viewer right.** Leash is held by her left hand on viewer right and connects to the dog.
- **R08 PASS: Glass barrel vault, tropical palms and bronze planters create a layered botanical station.** Glass vault, layered palms and bronze planters fill coherent depth layers.
- **R09 PASS: Moss-green vintage train is behind on right and ornate station clock is present.** Green vintage train occupies the right; station clock present.
- **R10 PASS: Warm golden light, wet black/ivory floor, contact shadows and reflections integrate subjects.** Matching warm light, contact shadows and reflected tile floor.
- **R11 PASS: Landscape 3:2 output; foreground subjects sharper than background.** 1536×1024 landscape with sharper foreground subjects.
- **R12 UNCERTAIN: No legible signage, clock numerals, logos or watermark.** Clock contains blurred numeral-like forms; exact legibility is uncertain.

### Exact prompt

```text
Reference roles:
Attached image 1 supplies the woman’s identity and outfit only. Attached image 2 supplies only the chocolate-brown Labrador dog’s appearance. Do not copy the woman from image 2. Neither image supplies the new background.

Fixed scene brief:
Create a photorealistic landscape 3:2 travel editorial inside a spectacular glass-roofed botanical railway concourse at late golden hour.

Main subjects: one adult woman with long brown hair, a slight natural smile, dark navy cap, blue-white plaid overshirt, black cropped tank, ripped blue jeans, black belt and white sneakers; and one stocky chocolate-brown Labrador with a broad face, amber-brown eyes, floppy ears and short dark brown fur. Use any supplied identity reference for its assigned subject, while following these same scene and content requirements.

The woman walks toward the camera slightly left of center, full body visible. The Labrador walks beside her on the viewer's right, full body visible, on a slack burgundy leash held in her left hand (the hand on the viewer's right). Keep the woman's described outfit intact. Adapt the dog's posture to walking while preserving the described or referenced appearance.

Behind them, show a soaring iron-and-glass barrel vault, layered tropical palms in bronze planters, an ornate station clock without readable numerals, and the front of a deep moss-green vintage train on the right. Warm sun shafts cut through the glass and reflect on a wet black-and-ivory tiled floor. Keep architectural lines in a coherent perspective, with the woman and dog sharper than the distant roof and train. Ground all feet and paws with matching contact shadows and reflections.

Exactly one woman and one dog; no crowd or second donor person. No floating leash, merged limbs, duplicate paws, extra animals, readable signage, logos or watermarks. Preserve natural face and fur texture; this should feel like a detailed travel photograph, not a cut-and-paste collage.
```
