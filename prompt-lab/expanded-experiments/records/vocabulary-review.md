# Plain words versus art-direction jargon

The two jargon repeats produced the same important objects, arrows and text that are visibly present in the two plain-language repeats. These samples do not show a need for specialist vocabulary. They also do not establish that ordinary wording always wins. The practical choice is to use words the person or agent can inspect and revise confidently.

## What this comparison isolates

The existing plain-prose prompt used 309 whitespace-separated words. Its jargon rewrite uses 315. Both are one paragraph, with the same ordered subjects, counts, materials, positions, relationships, text, framing, style and exclusions. The rewrite substitutes terms such as “inter-tier negative space” for “air gaps,” “filiform” for “slender,” and “foliar” for “leaf.” No quality slogans, new lighting specification, artist reference or extra detail were added. The complete prompt and a 20-row equivalence table were saved before either new generation. See `vocabulary-records.json` and `vocabulary-equivalence.md`.

This is a vocabulary comparison. It is separate from the experiment comparing prose with structured headings, and separate from asking whether an underspecified one-sentence prompt loses information. Plain language can still be detailed.

Each jargon repeat was a separate built-in image-generation request without explicit reference images. The plain N4 and A8 requests occurred earlier. No model identifier, seed or quality setting was exposed. Timing was not randomized, semantic equivalence is an analyst judgment, and this review was not blinded. Two images per wording condition are insufficient to estimate a reliable average effect or prove repeatability.

## Files and concrete observations

All four outputs are portrait 1024×1536 images. The two new originals were copied without modification and SHA-256 hashes are recorded.

| Trial | Wording | Image | Visible result |
|---|---|---|---|
| N4 | Plain prose | `outputs/expanded-experiments/language/trial-N4.png` | Five levels, three white masts, three filter materials, half-full glass sphere, planted stepped garden, copper coil, four downward arrows and one right-hand return arrow. All six strings are correct. Brass framing gives it a relatively mechanical character. |
| A8 | Plain prose | `outputs/expanded-experiments/language/trial-A8.png` | The same main requirements and exact copy are present. More rocky ground and planted edges give the assembly a garden-island character. The tier labels use longer lines that reach into the illustrated assemblies. |
| V2 | Jargon prose | `outputs/expanded-experiments/vocabulary/trial-V2.png` | The same main requirements and exact copy are present. The filter layers are especially distinct, including a pale lattice-like ceramic layer. The lower garden has cascading terraces and small gold bridges; the coil has a broad gear-like base. |
| V6 | Jargon prose | `outputs/expanded-experiments/vocabulary/trial-V6.png` | The same main requirements and exact copy are present. Bridges are more prominent and the machinery has pointed lower supports. The top platform is seen strongly from below while the lower assemblies expose their tops; interpretation of the requested elevated view is uncertain. |

The count check was literal: four copper arrowheads in the four gaps and one turquoise arrowhead near the cloud. The text check was manual: THE RAIN ENGINE, CLOUD, FILTER, VAULT, GARDEN and RETURN are correctly spelled and each appears once in V2 and V6. No additional text is visible. Counting six strings does not certify the invented machinery as technically functional; the prompt explicitly labels the world as imaginative concept art.

V2 passes 14 preregistered criteria with one uncertain. V6 passes 13 with two uncertain. In both, “generous margins” is uncertain because vertical clearance is modest and no numeric margin was preregistered. In V6 the view criterion is also uncertain: a single camera situated partway up a tall stack could explain the differing visible faces, but the intended elevated view is not unambiguous. These are criterion-level observations, not a general image-quality score. The parent's original review remains the formal record for N4/A8; this review does not rewrite it.

## What the reader can conclude

The richly detailed plain-language images already achieved the intended relationships and copy. Replacing ordinary words with specialist terms did not add a visible new capability in these four samples. V2's ceramic structure and V6's bridges are appealing possible variations, but comparable variation also appears between N4 and A8. With this sample size and an unexposed backend, those differences cannot be attributed confidently to jargon.

Use a technical term when it identifies a visual decision more precisely: for example, an “exploded view” has a useful established meaning. Pair an unfamiliar term with plain description if the reader might misunderstand it. There is no evidence here that “filiform” is a better instruction than “slender,” or that the model needs “interstices” to leave gaps. Keep counts, locations, materials and relationships; simplify vocabulary that merely makes the prompt harder to audit.

If the view discrepancy matters, the next trial should specify the intended visible planes explicitly: “Show the top surface of every platform; do not show any platform from below.” That adds information and therefore would be a new constraint experiment, not part of this vocabulary comparison. No such repair was run here.
