# Rain Engine: pre-registered language-organization trial

Four calls: plain, structured, plain, structured. Each condition receives exactly the same sentences and visual information. The only difference is headings and paragraph organization. Both use ordinary language. This isolates organization more cleanly than comparing a vague two-line brief against a detailed specification. It does **not** test whether longer or more ornate language is better. No image references, edits, retries, or selection exclusions are planned. All four outputs will be retained.

The existing official guide's process infographic, exact text, and educational diagram examples motivate a harder composite case: a fictional exploded water-cycle world. It is explicitly conceptual, not an engineering claim. The built-in tool does not expose model, seed or quality; results cannot be attributed specifically to GPT Image 2.5. With two samples per condition, findings are descriptive and do not establish a reliable causal advantage.

## Intended scene

An intricate, beautiful fictional water-cycle world, readable as a five-tier exploded atlas. Visual compliance and aesthetic appeal are evaluated separately.

## Checks fixed before generation

- **L01** Portrait canvas with width:height 2:3 (actual file dimensions).
- **L02** Exactly five visually separated tiers, vertical order preserved, one central stack, air gaps visible.
- **L03** Top tier has exactly three slender white harvesting masts beneath one curling cloud.
- **L04** Second tier has three distinguishable exposed filter layers: rough basalt, black carbon, pale ceramic.
- **L05** Middle tier is one clear glass sphere, visibly about half filled with turquoise water.
- **L06** Fourth tier shows leafy stepped garden terraces and tiny gold bridges between terraces.
- **L07** Bottom tier shows one large copper coil with white vapor emerging.
- **L08** Exactly four thin copper downward arrows link each adjacent pair of tiers in the air gaps.
- **L09** Exactly one turquoise return arrow on the right curves from bottom coil toward top cloud, with upward direction clear.
- **L10** Title THE RAIN ENGINE is spelled exactly once and is the largest text above the stack.
- **L11** CLOUD, FILTER, VAULT, GARDEN, RETURN appear exactly once each, spelled correctly, on the left beside the corresponding tiers.
- **L12** Tier labels have thin leader lines, remain readable, and do not overlap illustrated components.
- **L13** Museum atlas treatment, ivory/teal/moss/copper/gold palette, fine contours and soft 3D material shading visibly present.
- **L14** Consistent elevated three-quarter perspective and broadly upper-left illumination, without obvious contradictory lighting.
- **L15** Full stack/labels inside generous margins; no text beyond six strings; no people, logos, watermark, or decorative border.

Mark each pass, fail, or uncertain. Record what can be seen. Do not turn uncertain details into passes. Judge visual ambition, coherence and beauty separately from instruction compliance; prefer a specific observation over a global numerical beauty score. The reviewer sees neutral file codes and this checklist before the condition key. This is partial reviewer blinding, not a controlled laboratory trial.

## Plain-language prompt

```text
Create a portrait 2:3 illustrated atlas poster called THE RAIN ENGINE. It shows a fictional floating ecosystem as five separated tiers, stacked vertically on one central axis. Leave visible air gaps between tiers. This is imaginative concept art, not a validated engineering schematic. The top tier is a circular platform with exactly three slender white cloud-harvesting masts under one curling cloud. The second tier is an exposed filter, with three clearly different layers: rough basalt, black carbon, and pale ceramic. The middle tier is one clear glass spherical reservoir, half filled with turquoise water. The fourth tier is a lush garden on stepped terraces, with tiny gold bridges between terraces. The bottom tier is one large copper coil releasing a plume of white vapor. Show exactly four thin copper downward arrows in the gaps: top to second, second to middle, middle to fourth, and fourth to bottom. Show one turquoise return arrow outside the stack on the right, curving from the bottom coil up to the top cloud. Keep all five arrows distinct and readable. Print THE RAIN ENGINE exactly once, as the large title centered above the stack. Place these five smaller labels on the left, aligned with their respective tiers from top to bottom: CLOUD, FILTER, VAULT, GARDEN, RETURN. Use simple thin leader lines to the tiers. These six strings are the only text. Keep the labels large enough to read and clear of the illustration. Use an elegant museum atlas style: precise fine ink contours, softly shaded three-dimensional cutaways, a warm ivory background, deep teal and moss green forms, copper machinery, and restrained gold accents. Use one consistent elevated three-quarter view, with light from the upper left. Give the surfaces intricate mineral, glass, leaf, and machined-metal detail. Keep the full stack and all labels inside generous margins. Do not include people, logos, watermarks, or decorative borders.
```

## Structured prompt

```text
Purpose and composition:
Create a portrait 2:3 illustrated atlas poster called THE RAIN ENGINE. It shows a fictional floating ecosystem as five separated tiers, stacked vertically on one central axis. Leave visible air gaps between tiers. This is imaginative concept art, not a validated engineering schematic.

Tier contents, top to bottom:
The top tier is a circular platform with exactly three slender white cloud-harvesting masts under one curling cloud. The second tier is an exposed filter, with three clearly different layers: rough basalt, black carbon, and pale ceramic. The middle tier is one clear glass spherical reservoir, half filled with turquoise water. The fourth tier is a lush garden on stepped terraces, with tiny gold bridges between terraces. The bottom tier is one large copper coil releasing a plume of white vapor.

Relationships:
Show exactly four thin copper downward arrows in the gaps: top to second, second to middle, middle to fourth, and fourth to bottom. Show one turquoise return arrow outside the stack on the right, curving from the bottom coil up to the top cloud. Keep all five arrows distinct and readable.

Text and hierarchy:
Print THE RAIN ENGINE exactly once, as the large title centered above the stack. Place these five smaller labels on the left, aligned with their respective tiers from top to bottom: CLOUD, FILTER, VAULT, GARDEN, RETURN. Use simple thin leader lines to the tiers. These six strings are the only text. Keep the labels large enough to read and clear of the illustration.

Appearance and constraints:
Use an elegant museum atlas style: precise fine ink contours, softly shaded three-dimensional cutaways, a warm ivory background, deep teal and moss green forms, copper machinery, and restrained gold accents. Use one consistent elevated three-quarter view, with light from the upper left. Give the surfaces intricate mineral, glass, leaf, and machined-metal detail. Keep the full stack and all labels inside generous margins. Do not include people, logos, watermarks, or decorative borders.
```

## Outcome

Generation not yet started at protocol creation. Results will be appended without rewriting this protocol.

### Completion note

All four planned outputs were generated, copied without modification, visually inspected, and verified as 1024×1536 PNG. Exact prompts, neutral codes, condition key, source paths, SHA-256 hashes and observed dimensions are in `language-records.json`. The generation operator's separate observations are in `language-operator-review.md`; the independent parent reviewer should record its own neutral-code assessment before opening that file or the decoding key.

The publicly retained images and protocol are under `outputs/expanded-experiments/language/`. The operator observed no clear rendering advantage from adding headings alone. Both conditions already used the same specific, ordinary-language scene decisions. The close top margin was a shared uncertainty. This is descriptive evidence from two samples per condition, with model, seed and quality unexposed.

Conditions were submitted in alternating order, not randomized. Neutral display order was shuffled using `SystemRandom` after generation and stored in `language-checks.json`; this provides a partially blinded review workflow, not full experimental blinding.


## Retained result files

- **N4** — `plain_prose`, sample 1; 1024 × 1536 PNG; [image](trial-N4.png).
- **V6** — `labeled_sections`, sample 1; 1024 × 1536 PNG; [image](trial-V6.png).
- **A8** — `plain_prose`, sample 2; 1024 × 1536 PNG; [image](trial-A8.png).
- **S2** — `labeled_sections`, sample 2; 1024 × 1536 PNG; [image](trial-S2.png).

All four requested outputs were retained without cropping, retouching, or regeneration. Actual backend/model, seed, and quality remain unexposed. The raw images demonstrate this workflow through the available built-in generator; they do not establish a GPT Image 2.5 performance result.
