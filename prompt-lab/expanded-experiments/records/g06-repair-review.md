# G06 repair: make the return visible

The repair fixes the story. The person now faces into the room, steps over the threshold and looks down at the waiting cat. The original's last panel showed the person's back and read as another departure. One explicit pose edit made the intended action legible.

Source: `outputs/expanded-experiments/generation-coverage/g06-cat-four-panel.png`.

Repaired original: `outputs/expanded-experiments/generation-coverage/g06-last-panel-repaired.png`.

Both PNGs are 1024×1536. The returned original was copied without image processing; its SHA-256 and source path are in `g06-repair-record.json`.

## The instruction and what changed

Before the edit, the source was inspected at original resolution. The prompt described the observable pose: visible face and front of coat, torso and knees toward the room, one foot crossing onto the interior mat, gaze toward the cat, back toward the outdoors. It explicitly retained the short brown wavy hair, mustard coat, jeans, boots, shoulder bag and navy umbrella. It asked for exactly the original first three panels and an unchanged room and cat in the fourth. Nine checks were saved before the call. The full prompt is in the record.

The output satisfies the requested action and keeps the main props. There is one person in the final panel, with an inward step, downturned gaze and visible face. The cat and popcorn clue remain beside the mat. The teal player is closed in the final panel, and the earlier player states remain closed, open, open. Furniture, window, room arrangement and four-panel page structure remain closely consistent.

The source only showed the back of the person's head. The generated front-facing face is therefore newly invented. Clothing and hairstyle continuity can be checked; exact facial identity cannot.

## Preservation was partial

The phrase “change only the person” did not preserve every other pixel. Sofa upholstery across all four panels gained a more visible repeating scroll or floral pattern. Fine pillow markings, grain, book-spine details and some surface textures also changed outside the requested region. The broad room, palette and story states remain consistent, so the repair works narratively, but it is not an exact local replacement.

An RGB difference check over the unchanged first-three-panel band, coordinates `[0, 0, 1024, 1055]`, confirms that the output is not pixel-identical. Mean absolute differences are approximately 8.59, 7.70 and 6.84 on the 0–255 red, green and blue channels. About 99.78% of pixels have at least one changed channel. This percentage is **not** a measure of semantic damage: small grain, color and edge changes count. The visible upholstery drift is the material preservation finding.

Eight preregistered checks pass at their stated visual level; one is uncertain because tiny book markings cannot be certified as unchanged text. The stronger exact-preservation instruction in the prompt fails independently of those broad consistency checks. This is why a review should record two results: whether the requested change worked, and whether preserved details stayed fixed.

## Actionable lesson

When a story beat is ambiguous, specify the physical evidence of the action. “Returning home” permits several plausible poses; “front of coat visible, one foot inside, looking at the cat” narrows the image directly.

One focused change can make diagnosis easier, but it does not guarantee isolation. Review untouched regions after every edit. If fabric texture or precise pixels matter, the next step would be a constrained selection around the person and doorway, followed by comparison of the untouched panels. That follow-up was not run. The result here supports a useful repair workflow, not a claim that sequential edits always outperform a combined edit or that this backend outperforms another model.
