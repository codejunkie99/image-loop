# 24 image-making cases, with prompts and observed failures

Every illustrated stage in the selected [OpenAI guide](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5) has a corresponding generated case below. Each published Sunburst image was inspected. The official example is a reference for the category, not a weak baseline to beat.

Most briefs intentionally change subject, composition or format. Their visual differences therefore **cannot establish that our methodology is superior**. Our built-in tool did not expose model, seed or quality; these are not verified GPT Image 2.5 benchmark runs. One result per category cannot establish reliability. Every first result remains visible, including failures. Repairs and the two-route edit comparison are separately labeled.

The useful pattern is consistent: decide the objects, relationships, text and preserved details; generate; inspect the file and the image; repair the failed requirement. The exact prompts below are our submitted prompts. Original guide prompts are linked rather than reproduced. Paths in the JSON are relative to the outputs directory; Markdown image links use full local paths for the desktop viewer.


## G01 · The net maker

Category: [Control style and lighting](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#control-style-and-lighting). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/photorealism-gpt-image-2-5-sunburst.webp). Close portrait.

![The net maker](../expanded-experiments/generation-coverage/g01-maritime-editorial.png)

**Method.** Give each depth layer a job: net and ochre rope in front, working hands and dog as the subjects, blue wheelhouse behind them, harbor in the distance. Specify where hands touch the net and where warm sunlight meets cool fill.

**Observed.** The wide scene has coherent hand-to-net contact, a fully framed dog, distinct rope, skin, wood and fur textures, and readable depth. No planned visible constraint failed. The wider framing gives the face less prominence.

**Next action.** Keep this result for an environmental story. For a portrait, make the face larger before adding further background detail.

**Technique to keep.** A complex scene becomes manageable when every layer has a subject, a location and a visual priority.

**Comparison boundary.** Intent changed: we chose a wider environmental composition. Greater scene breadth does not establish a better prompt or a better model.

Saved original: 1536 × 1024 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Create a landscape 3:2 editorial photograph for a feature about skilled maritime work.
Scene: an elderly sailor repairs a fishing net on the deck of a small, weathered wooden boat in a sheltered harbor. This is a candid working moment, not a fashion pose.
Visual map: foreground lower-left has loose ochre rope coils and wet dark deck planks; the sailor occupies the left-center, seated with both hands visibly tying one section of net. The net stretches diagonally from his lap toward a wooden float at lower-right. One black-and-white dog sits to his right, fully visible from ears to paws, watching his hands. Behind them are a worn blue wheelhouse, winch, neatly stowed buoys and several fishing boats farther across the water. Distant buildings stay subordinate.
Appearance: silver stubble, creased face, salt-stained canvas jacket, ribbed wool sweater, rough hands. Net fibers, chipped paint, water droplets and rope wear should be distinguishable without oversharpening.
Light: a low warm shaft of sunrise from upper-left catches the sailor's profile, hands and translucent net fibers. Cool blue harbor shade fills the unlit surfaces. Light and shadows must agree across the man, dog and deck. Fine film grain and natural tonal range; color restrained except for the blue wheelhouse and ochre rope.
Composition: eye level from the bow, enough depth of field to understand the work and setting. Distinct foreground, working figures, boat structure and harbor layers. No text, no logos, no artificial fog, no beauty retouching. Keep hands, net and dog unobstructed.
```

</details>

## G02 · The Rain Engine

Category: [Explain a process visually](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#explain-a-process-visually). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/infographic-coffee-machine-gpt-image-2-5-sunburst.webp). Dense functional cutaway.

![The Rain Engine](../expanded-experiments/language/trial-S2.png)

**Method.** Define five named tiers before writing style instructions. Give every tier its own material and contents, then list exactly four downward links and one return link. Put exact labels in a separate text inventory. This fictional mechanism is concept art.

**Observed.** Language trial S2 renders the five tiers, three masts, three filter materials, half-full tank, stepped garden, copper coil and five arrows coherently. All six strings are correct. The title is close to the edge, so generous margins remain uncertain.

**Next action.** For an actual explanatory graphic, verify the mechanism independently. If spacing needs repair, replace generous margins with a stated safe area.

**Technique to keep.** A diagram needs a graph of objects and connections before it needs an aesthetic.

**Comparison boundary.** Intent changed to an invented ecosystem with less explanatory copy. The official example is already information-rich; this adaptation tests a different visual brief.

Saved original: 1024 × 1536 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

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

</details>

## G03 · Afterlight

Category: [Render exact text](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#render-exact-text). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/thread-ad-gpt-image-2-5-sunburst.webp). Streetwear campaign.

![Afterlight](../expanded-experiments/generation-coverage/g03-afterlight-poster.png)

**Method.** Separate an exact headline and two footer lines from the sculpture zone. Build drama with a giant orange disc, folded cobalt metal, amber glass and exactly three small visitors. Count and place people instead of asking vaguely for scale.

**Observed.** The three text lines and visitor count are correct. Metal and glass contrast clearly, but the sculpture apex enters the headline baseline zone, violating the requested clean separation.

**Next action.** Lower only the arch apex while retaining the headline, footer, disc and three visitors. No correction was run for this case.

**Technique to keep.** Correct spelling and good typography are separate checks from unobstructed text placement.

**Comparison boundary.** Intent changed to a festival art poster with new copy and architecture. A more dramatic genre is not evidence of prompting superiority.

Saved original: 1024 × 1536 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Design a striking portrait 2:3 art-festival poster, a complete finished graphic, not a photograph of a poster.
Headline zone, top 22%: the word "AFTERLIGHT" exactly once, enormous condensed ivory sans-serif capitals, perfectly legible, straight baseline, generous clear margin.
Central image, middle 60%: an immense sculptural arch made of folded cobalt-blue metal and translucent amber glass rises above shallow ivory steps. A luminous orange sun-disc is visible through the opening. Thin copper wires suspend several long cobalt ribbons that twist through the air without covering the headline. Three tiny visitors stand on separate steps at the arch's base to establish scale, each a clean human silhouette. The blue structure has crisp folded edges; amber glass refracts the warm light; copper catches small highlights. Deep near-black background, dramatic but physically coherent warm backlight and cool side light. Meticulous architectural miniature photography combined with premium editorial art direction.
Footer zone, bottom 15%: two centered lines, exactly "ART AFTER DARK" then "19–21 OCT". Clean ivory typography, readable with generous spacing.
Hierarchy: headline first, luminous arch second, visitors third, footer fourth. Give every element room; make the impossible scale wondrous while keeping materials believable.
Only the three specified text lines. Do not add a venue, sponsor, logo, barcode, decorative tiny writing or watermark. Keep all typography separate from the sculpture and visitors.
```

</details>

## G04 · Tideline identity

Category: [Design a reusable logo](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#design-a-reusable-logo). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/logo-generation-1-gpt-image-2-5-sunburst.webp). Bakery logo.

![Tideline identity](../expanded-experiments/generation-coverage/g04-tideline-mark.png)

**Method.** Constrain the logo to one navy symbol and one wordmark. Describe the shared bird-and-wave silhouette, the negative space and a measurable width hierarchy. Ask for actual transparency as an output property, then inspect the file.

**Observed.** The bird/wave concept and TIDELINE spelling work, and the PNG has real alpha. The wordmark is 727 pixels wide against a 670-pixel symbol at alpha greater than 128: about 8.5% wider, despite the request for a narrower wordmark.

**Next action.** Scale only the wordmark to 80–85% of the symbol width and recenter it. Rebuild the approved identity as editable vectors for production.

**Technique to keep.** A useful identity mark may need less detail. Check proportions and file properties instead of adding decorative adjectives.

**Comparison boundary.** Intent changed to a new coastal brand and simpler shape language. This is an identity exploration, not a matched logo-quality comparison.

Saved original: 1254 × 1254 PNG (RGBA).

<details><summary>Exact submitted prompt</summary>

```text
Create one original logo for a fictional coastal conservation studio named TIDELINE. Square 1:1 canvas with a genuinely transparent background; preserve real alpha transparency.
Symbol: a compact near-circular dark navy silhouette. Inside it, one broad flowing negative-space channel curves upward like a breaking wave and resolves into the simple profile of a shorebird's head looking right. Use only two or three broad connected shapes. The bird and wave should share one elegant silhouette rather than look like separate clip-art objects. No feathers, eyes, scenic illustration, thin decorative lines or gradients.
Place the symbol centered in the upper-middle. Below it, set "TIDELINE" exactly once in dark navy uppercase geometric sans-serif, widely but evenly spaced. Align the wordmark with the symbol; keep the wordmark narrower than the symbol's outer width. Plenty of empty transparent margin on all sides.
This is a flat vector-like raster logo exploration. Crisp solid edges, balanced negative space, strong recognition at small sizes. One ink color only: deep navy. No shadows, mockup, paper texture, backdrop, drawn checkerboard, border, additional text or watermark.
```

</details>

## G05 · A field becomes a city

Category: [Use historical and real-world context](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#use-historical-and-real-world-context). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/world-knowledge-gpt-image-2-5-sunburst.webp). Crowd-level historic scene.

![A field becomes a city](../expanded-experiments/generation-coverage/g05-woodstock-recreation.png)

**Method.** Separate sourced anchors from imagined staging. Use the verified sloping field and stage-at-bottom relationship, then plan five foreground attendees, a muddy route and a crowd that diminishes into the distance.

**Observed.** The planned scene and five foreground figures are present. The topography is consistent with the museum source, but the exact viewpoint, people, clothing combinations and moment are invented; this is an AI recreation.

**Next action.** For documentary reconstruction, select an archival photograph and map its actual structures and viewpoint. Do not treat visual plausibility as historical verification.

**Technique to keep.** Research bounds invention. Label which details are observed, sourced, inferred or deliberately added.

**Comparison boundary.** Intent changed to an elevated wide view with an explicit foreground group. More spatial scale is a compositional choice, not proof of greater historical accuracy.

Saved original: 1536 × 1024 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Create a wide 3:2 photorealistic historical reconstruction of a crowd at the Woodstock Music and Art Fair, on Max Yasgur's farm in Bethel, New York, in August 1969. It should resemble a carefully staged period editorial scene, not a present-day festival.
Verified setting to depict: a very large crowd spreads across a grassy, sloping farm field; the concert stage sits at the foot of the audience slope, with wooded edges and rural land beyond. Rain and mud were part of the festival. Do not portray an exact documented instant or recognizable performer.
Composition: view from among the audience near the upper slope, looking down toward the distant stage. Foreground, five distinguishable young adult attendees sit or stand on blankets: worn denim, simple cotton shirts, a patterned long skirt, long hair and a canvas shoulder bag. Their poses are relaxed and varied, facing generally toward the stage. A muddy footpath leads diagonally through the middle-ground crowd. Scattered simple canvas tents sit toward the far wooded edge. Thousands of more distant attendees become increasingly small, with natural nonrepeating clusters.
Appearance: muted late-1960s color-film character, soft overcast daylight, real skin and fabric, grass worn into patches of earth. Period-appropriate simple stage scaffolding and speaker stacks remain small in the distance. No LED screens, smartphones, modern stage lasers, contemporary branded clothing, modern security barriers or giant printed sponsor signs.
No caption or readable writing inside the image. Preserve convincing human anatomy in the foreground and a coherent hillside perspective.
```

</details>

## G06 · The record collector

Category: [Turn a story into a comic strip](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#turn-a-story-into-a-comic-strip). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/comic-reel-gpt-image-2-5-sunburst.webp). Four-panel home story.

![The record collector](../expanded-experiments/generation-coverage/g06-cat-four-panel.png)

**Method.** Write a state table for each panel: where the cat is, whether the player is open, whether the person is present and what clue remains. Keep room landmarks fixed. Review the visible pose that communicates each action.

**Observed.** The first output keeps the room, cat and player-state sequence but the last panel reads as another departure. One repair makes the person enter and look at the cat. The repair also changes upholstery texture in otherwise unchanged panels.

**Next action.** Use the repaired page for the readable story, with its preservation limitation disclosed. If exact texture matters, constrain the edit region and compare untouched areas.

**Technique to keep.** Describe an action through visible evidence: front of coat, inward step, gaze toward the cat. Evaluate the requested change and preservation separately.

**Comparison boundary.** Intent changed in story, props and visual treatment. The repair demonstrates a specific fix with collateral texture drift, not universal superiority of sequential edits.

Saved original: 1024 × 1536 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Draw one portrait 2:3 comic page with exactly four horizontal panels stacked top to bottom, equal-width panels and clean ivory gutters. No text, dialogue, lettering, panel numbers or sound effects.
Visual style: sophisticated hand-inked European picture-book illustration, precise warm outlines, richly painted gouache, terracotta, petrol blue, mustard and sage. Detailed but readable interiors, not flat clip art.
Recurring identity: one small orange tabby cat with a white muzzle, white front paws, three dark forehead stripes and a cobalt-blue collar. Keep these features in every panel.
Recurring room: a terracotta sofa is left-center, a low walnut record cabinet with a teal record player is on the right, a large round window is behind the sofa, and the entrance is at far left. Keep furniture placement and colors consistent.
Panel 1: a person in a mustard raincoat exits through the far-left doorway, carrying a folded navy umbrella. The cat sits near the threshold watching. The teal record player on the right is closed and inactive.
Panel 2: the same room after departure. The cat stands with its front white paws on the record cabinet and lifts the teal record player's lid with one paw. One black vinyl record is visible on the turntable. No human is present.
Panel 3: the same cat sprawls happily across the terracotta sofa, eyes closed, while the open record player at right plays the black record. A small bowl of popcorn sits on the floor with a few spilled kernels. Warm afternoon light comes through the round window.
Panel 4: the raincoat-wearing person returns at the far-left doorway holding the folded navy umbrella. The cat sits innocently by the threshold as in panel 1. The record player's lid is closed again, but one small popcorn kernel remains beside the cat as the visual punchline.
Make the story immediately readable. One cat per panel; preserve room geography, color palette and recognizable objects.
```

</details>

### G06-R1 · One pose repair

![One pose repair](../expanded-experiments/generation-coverage/g06-last-panel-repaired.png)

Return action fixed; sofa and fine surface textures drift outside the edited person.

<details><summary>Exact follow-up prompt</summary>

```text
Edit the supplied four-panel comic. Change only the person's action and orientation in the fourth, bottom panel. They must unmistakably be RETURNING INTO the room: show their face and the front of their mustard coat, torso and knees directed inward toward the viewer, one foot stepping across the doorway onto the interior mat, and their gaze angled down toward the waiting orange cat. The back of their body should face the rainy outdoors, not the viewer. Keep the same short wavy brown hair, mustard coat, blue jeans, brown boots, brown shoulder bag and folded navy umbrella. One person only in that panel.
Preserve panels 1, 2 and 3 exactly as shown. In panel 4 preserve the orange cat's position and appearance, the popcorn clue, closed teal record player, sofa, furniture, window, plants, doorway, palette, lighting, ink-and-gouache style, framing and panel boundaries. Change only the person and the immediately occluded doorway pixels necessary for that pose. Do not add text or other objects. Return the complete four-panel page at the same dimensions.
```

</details>

## G07 · Fieldwork market

Category: [Create an interface preview](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#create-an-interface-preview). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/ui-farmers-market-gpt-image-2-5-sunburst.webp). Market app screen.

![Fieldwork market](../expanded-experiments/generation-coverage/g07-fieldwork-market-ui.png)

**Method.** Map screen regions and give every visible interface string explicitly. Distinguish the title, category chips, vendor cards, featured product and navigation. Treat photographs as text-bearing regions too.

**Observed.** The requested interface labels, vendor names and price are readable and correct. The model adds unrequested slogans on signs inside the vendor photographs. The file is a polished visual preview; no interface behavior is implemented.

**Next action.** Remove or blank the in-photo signs while retaining the interface copy. Build actual controls and test interactions separately.

**Technique to keep.** An exact text inventory must include incidental signs, packaging and photographed labels, not only the main layout.

**Comparison boundary.** Broad app category retained, with new information architecture, content and imagery. The different brief does not support a causal claim of better UI prompting.

Saved original: 1024 × 1536 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Create one portrait 2:3 product-design presentation containing a single straight-on modern smartphone, centered on a pale warm-gray background. The phone fills most of the frame and displays a crisp, finished farmers-market app named Fieldwork. This is a realistic shipped-app visual preview, not a concept sketch.
Screen layout top to bottom:
1. A compact status bar and a header reading "Fieldwork", with a small search icon and bag icon.
2. A large editorial hero photo of a market stall with tomatoes, flowers and leafy vegetables. Overlay a cream card at its lower edge: "Saturday market" on the first line and "8 AM – 1 PM · Riverside Park" below.
3. Three small filter chips in one row: "All", "Produce", "Bakery". All is selected in dark forest green.
4. Section heading "Meet the makers". Two equal vendor cards side by side with different photographs: baskets of tomatoes on the first, flour-dusted sourdough on the second. Labels exactly "Green Row" / "Vegetables" and "Early Bird" / "Sourdough".
5. A smaller full-width cream-tinted promotional row with a close photo of mixed tomatoes and text "Today's pick" and "Heirloom tomatoes", plus "$4 / lb" aligned at right.
6. A bottom navigation bar with three clean icons and text "Explore", "Saved", "Bag"; Explore selected.
Use warm white, deep forest green and restrained tomato-red accents. Fine charcoal typography, strong spacing, carefully aligned cards, natural photographs, crisp rounded rectangles, practical contrast. Keep the entire screen visible with no overlapping controls or cropped labels. No lorem ipsum, fake paragraphs, extra feature sections, device logos or decorative floating objects.
```

</details>

## G08 · Inside a leaf

Category: [Create scientific and educational visuals](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#create-scientific-and-educational-visuals). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/scientific-educational-cellular-respiration-gpt-image-2-5-sunburst.webp). Cellular respiration diagram.

![Inside a leaf](../expanded-experiments/generation-coverage/g08-leaf-cutaway.png)

**Method.** Start with verified anatomy, organize the layer order, and map every label to a particular structure. Reserve space for leader lines and specify gas directions. Review the endpoints after the image looks finished.

**Observed.** The cutaway is visually clear and most layer relationships are correct. The Stoma leader ends on a guard cell rather than the pore. Gas arrows point in the intended directions but do not clearly pass through the pore; another unlabeled arrow is ambiguous.

**Next action.** Correct the Stoma endpoint and gas-arrow route before teaching from this image. Have a subject expert inspect the finished annotation layer.

**Technique to keep.** A plausible diagram can contain a consequential local error. Check each label-to-structure relationship, not just spelling and polish.

**Comparison boundary.** Intent changed to leaf anatomy. The new subject and representation prevent a fair improvement claim against the published example.

Saved original: 1536 × 1024 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Create a landscape 3:2 educational plate titled "INSIDE A LEAF" for a high-school biology lesson. Show a beautiful, scientifically readable three-dimensional cutaway block through a typical eudicot leaf, floating on an ivory background. Illustration is a precise textbook model with subtle painted texture, not a microscope photograph. The tissue layers are enlarged schematically; do not add a numerical scale.
Anatomical map, top to bottom:
- a very thin waxy cuticle on top;
- one layer of upper epidermal cells;
- closely packed elongated upright palisade cells, full of small green chloroplasts;
- a lower layer of loosely arranged irregular spongy cells with obvious connected air spaces and some chloroplasts;
- one layer of lower epidermal cells, interrupted at front-center by a clear stomatal opening flanked by two guard cells.
Embed one rounded vascular bundle within the mesophyll at the right side of the cutaway. Its larger xylem vessels are above its smaller phloem cells. Keep the surrounding tissues visible.
Labels with thin noncrossing leader lines and sufficient margin, each exactly once: "Cuticle", "Upper epidermis", "Palisade mesophyll", "Spongy mesophyll", "Air space", "Lower epidermis", "Guard cells", "Stoma", "Xylem", "Phloem". Each leader must touch the correct structure; never use a label as decoration.
Below the stomatal pore show one small inward arrow labeled "CO2 in" going from outside through the pore into the internal air space, and one small outward arrow labeled "O2 out" going from that air space through the pore to outside. Separate arrows so their directions are unambiguous. The pore must actually open into the air space, not a solid cell.
Use botanical greens, cream cell walls, muted blue xylem and muted coral phloem. Preserve cell topology and a clear layer hierarchy. No animal organs, invented organelles, extra captions or decorative foliage.
```

</details>

## G09 · Civic Move — quarter in view

Category: [Build slides, diagrams, and charts](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#build-slides-diagrams-and-charts). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/market-opportunity-slide-gpt-image-2-5-sunburst.webp). Market-sizing slide.

![Civic Move — quarter in view](../expanded-experiments/generation-coverage/g09-civic-move-slide.png)

**Method.** Supply one small fixed dataset, assign each variable a chart type, define axes and units, and list all printed values. Mark the data as illustrative. Verify text separately from bar lengths and export dimensions.

**Observed.** All values and labels are coherent: trips 120/180/240, on-time 80/85/90%, and mix 50/30/20. Exact geometry is approximate: bar lengths have small ratio deviations and the 1672×941 canvas differs from exact 16:9 by about 0.053%.

**Next action.** Use the approved layout as direction and render final charts from the same data in a deterministic plotting or slide tool when numerical geometry matters.

**Technique to keep.** Correct numbers printed beside a chart do not prove the marks encode those numbers precisely.

**Comparison boundary.** Intent changed to a three-chart operational slide with synthetic data. This is a design demonstration, not a benchmark against a different dataset.

Saved original: 1672 × 941 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Create one polished landscape 16:9 presentation slide, a flat full-slide graphic, titled "CIVIC MOVE" with the subtitle "Quarter in view". Use a warm ivory background, dark navy typography, thin neutral rules, refined editorial spacing and restrained teal, blue and orange chart colors. No photographs, gradients, 3D effects or drop shadows.
Layout: header at the top, then exactly three equal-width chart panels in a single row with generous margins.
Left panel title "Trips". Vertical bar chart with three months: "Jan", "Feb", "Mar". Values are exactly 120, 180, 240. Bars share a zero baseline, heights in ratio 1:1.5:2. Place each value clearly above its bar. Y-axis labeled "Trips" with ticks 0, 120, 240. Bars teal.
Middle panel title "On-time rate". A simple blue line chart with three points Jan 80%, Feb 85%, Mar 90%. Label each point exactly "80%", "85%", "90%". Vertical scale has ticks 70%, 80%, 90%, 100%, evenly spaced. Points increase by equal vertical steps. Months aligned in order under points.
Right panel title "March mix". Horizontal bars for "Bike", "Bus", "Walk" with values 50%, 30%, 20%. Same zero baseline and common scale; lengths in ratio 5:3:2. Bike teal, Bus muted blue, Walk burnt orange. Each value at its bar end. No pie chart.
Footer at bottom-left exactly "Illustrative data · Not a real business". No source citation or other data.
Prioritize mathematical consistency and legible text over decoration. All three panels must fit comfortably. Every requested label appears in its intended place, with no extra metrics, legends, logos or generated gibberish.
```

</details>

## G10 · The Rain Engine in Spanish

Category: [Translate while preserving layout](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#translate-while-preserving-layout). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/infographic-coffee-machine-sp-gpt-image-2-5-sunburst.webp). Spanish cutaway diagram.

![The Rain Engine in Spanish](../expanded-experiments/edit-coverage/g10.png)

**Method.** Use the existing poster as the layout target. Provide a complete six-entry glossary with accents, retain the original text zones, and permit only the type-size and leader-line adjustments required by longer replacements.

**Observed.** All six Spanish replacements, including DEPÓSITO and JARDÍN, are correct. The stack and arrow topology stay consistent. Reservoir caustics and some foliage are redrawn, so exact illustration preservation fails.

**Next action.** For an unchanged print master, replace text in an editable layout layer. If another generation is acceptable, select text regions and inspect untouched illustration afterward.

**Technique to keep.** Text localization and pixel preservation are separate acceptance criteria.

**Comparison boundary.** Intent changed to our fantasy atlas. It has fewer labels and a different layout; the successful translation does not prove a superior localization method.

Saved original: 1024 × 1536 PNG (RGB).

**Inputs, in attachment order:**

- [trial-N4.png](../expanded-experiments/language/trial-N4.png): edit target: illustration, geometry, material and typography layout.


<details><summary>Exact submitted prompt</summary>

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

</details>

## G11 · Night Courier

Category: [Transfer a visual style](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#transfer-a-visual-style). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/motorcycle-gpt-image-2-5-sunburst.webp). Isolated pixel rider.

![Night Courier](../expanded-experiments/edit-coverage/g11.png)

**Method.** Assign the reference to style only: palette, square clusters and stepped edges. Exclude its objects and interface. Map a foreground rider, middle canal market and distant towers, with an explicit bridge count and title zone.

**Observed.** The result has crisp pixel treatment, strong three-layer depth, one rider and two motorcycle wheels. NIGHT COURIER is correct. It has three distant arched bridges rather than the requested two; some far-side hand and boot contacts are occluded.

**Next action.** Give the bridges stable IDs on a visual map, select the surplus bridge and remove it. In a new brief, name the two desired bridge locations.

**Technique to keep.** A style reference can guide appearance without supplying content, but count every repeated background element.

**Comparison boundary.** Intent expanded to a complete city poster. The rich environment is added content, not proof that the method renders the same brief better.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [pixels.webp](../expanded-experiments/edit-coverage/inputs/pixels.webp): style only: palette, pixel clusters and edge treatment.


<details><summary>Exact submitted prompt</summary>

```text
Use image 1 only as a visual-style reference. Extract its crisp square pixel clusters, stepped diagonals, small restricted color ramps, near-black negative space, bright cobalt/cyan, warm orange-yellow highlights and restrained magenta stars. Do not copy its words, spacecraft, planets, layout, scores, menus or logos.

Create a new landscape 3:2 illustrated game-poster scene called NIGHT COURIER. Foreground: exactly one motorcycle with two clearly visible wheels, ridden by one courier in a red jacket and ivory full-face helmet, crossing a narrow elevated bridge from left to right. Both gloved hands meet the handlebars and the boots meet the foot pegs. Show the whole motorcycle and rider, occupying the lower middle of the frame.

Middle ground: a dense rain-soaked market city built over a deep canal, with stacked shop awnings, hanging lanterns, service pipes and a few small moored boats. Background: tall cobalt towers and two arched skybridges disappearing into wet night haze. Use three clear depth layers so the foreground silhouette reads immediately. Render rain, warm window lights and cyan reflections as deliberate pixel clusters, not smooth photographic effects.

Place NIGHT COURIER exactly once in bold readable pixel lettering inside the upper-left sky area. No other letters, HUD, numbers, watermark or border. Keep all important content within a 5% margin. The result must be coherent detailed pixel art, without antialiased vector edges, painted blur, or a photograph underneath.
```

</details>

## G12 · A wardrobe assembled from four references

Category: [Preserve identity and change clothing](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#preserve-identity-and-change-clothing). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/outfit-gpt-image-2-5-sunburst.webp). Garment assembly.

![A wardrobe assembled from four references](../expanded-experiments/edit-coverage/g12.png)

**Method.** Give each input one role: person and museum, blazer, tank, boots. Enumerate garment details and preserved pose anchors. Allow natural folds and occlusion while keeping face, body, black jeans and room stable.

**Observed.** The beige blazer, white tank and gray boots appear on the referenced person with the folded arms and crossed ankles retained. Visible likeness and museum arrangement remain close. One boot buckle is hidden, so exact hardware preservation is uncertain.

**Next action.** If hardware is essential, request a useful detail view or adjust the named buckle. Do not pass a hidden component as verified.

**Technique to keep.** Reference roles reduce ambiguity. Verify visible evidence and record occluded details as unknown.

**Comparison boundary.** The broad task and source garments are retained, with a new detailed constraint set. This was not a controlled same-prompt rerun or a likeness benchmark.

Saved original: 1024 × 1536 PNG (RGB).

**Inputs, in attachment order:**

- [woman-in-museum.webp](../expanded-experiments/edit-coverage/inputs/woman-in-museum.webp): edit target, identity, pose, environment.
- [jacket.webp](../expanded-experiments/edit-coverage/inputs/jacket.webp): blazer garment only.
- [tank-top.webp](../expanded-experiments/edit-coverage/inputs/tank-top.webp): tank garment only.
- [boots.webp](../expanded-experiments/edit-coverage/inputs/boots.webp): boots garment only.


<details><summary>Exact submitted prompt</summary>

```text
Image 1 is the edit target and sole person/environment reference: the smiling dark-haired woman standing with folded arms and crossed ankles in the museum. Images 2, 3 and 4 are garment references only: the beige blazer, white scoop-neck tank top, and gray knee-high suede boots.

Replace her knitted sweater and white sneakers with an outfit assembled from those garments. Put the beige blazer from image 2 over the white tank from image 3, leaving the blazer open enough to see the tank. Match the blazer's beige fabric, notched lapels, two dark front buttons and flap pockets; adapt its drape to her existing folded-arm pose. Put the gray boots from image 4 on both feet, over her existing black jeans, retaining the suede texture, low heels, knee-high shafts and two buckle straps on each boot.

Preserve image 1's facial features, apparent age, smile, skin texture, black shoulder-length hair and earrings. Keep the folded arms, crossed ankles, body proportions, camera viewpoint, full-body framing and museum lighting. Preserve her black jeans wherever not naturally covered by blazer or boots. Keep the marble statue on the left, both gold-framed paintings on the right, floor tiles and background geometry in place. Clothing may create natural new folds, occlusions and contact shadows; do not change her anatomy to simplify the fit. No extra people, accessories, labels, logos or beauty retouching. Portrait 2:3.
```

</details>

## G13 · Botanical railway editorial

Category: [Combine references](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#combine-references). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/test-woman-with-dog-gpt-image-2-5-sunburst.webp). Street composite.

![Botanical railway editorial](../expanded-experiments/edit-coverage/g13.png)

**Method.** Assign the first reference to the woman and outfit, the second to the dog only, and create a new environment. Specify walking positions, leash-to-hand contact, full-body framing, depth, light and grounded reflections.

**Observed.** The woman, dog, leash and elaborate concourse integrate coherently. Two small background people violate the exactly-one-person rule. The clock has numeral-like marks despite the no-readable-numerals instruction.

**Next action.** Map and remove the distant people, and replace the clock markings with plain ticks, while preserving the foreground pair and leash.

**Technique to keep.** Explicit donor roles help composition; an exclusion still needs a whole-image inspection at several scales.

**Comparison boundary.** Intent changed to a new railway environment and walking arrangement. The added spectacle cannot establish method superiority.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [test-woman.webp](../expanded-experiments/edit-coverage/inputs/test-woman.webp): woman identity and outfit only.
- [test-woman-2.webp](../expanded-experiments/edit-coverage/inputs/test-woman-2.webp): dog donor only; exclude donor woman/background.


<details><summary>Exact submitted prompt</summary>

```text
Reference roles are strict. Image 1 supplies only the woman: her face, long brown hair, dark navy cap, blue-white plaid overshirt, black cropped tank, ripped blue jeans, black belt and white sneakers. Image 2 supplies only the chocolate-brown Labrador dog: broad face, amber-brown eyes, floppy ears, dark brown short fur and stocky proportions. Do not use the second woman's identity, clothes or pose. Neither image supplies the new background.

Create a photorealistic landscape 3:2 travel editorial inside a spectacular glass-roofed botanical railway concourse at late golden hour. The woman from image 1 walks toward the camera slightly left of center, full body visible. The Labrador from image 2 walks beside her on the viewer's right, full body visible, on a slack burgundy leash held in her left hand (the hand on the viewer's right). Keep her reference outfit intact. Adapt the dog's posture to walking while preserving its recognizable appearance.

Behind them, show a soaring iron-and-glass barrel vault, layered tropical palms in bronze planters, an ornate station clock without readable numerals, and the front of a deep moss-green vintage train on the right. Warm sun shafts cut through the glass and reflect on a wet black-and-ivory tiled floor. Keep architectural lines in a coherent perspective, with the woman and dog sharper than the distant roof and train. Ground all feet and paws with matching contact shadows and reflections.

Exactly one woman and one dog; no crowd or second donor person. No floating leash, merged limbs, duplicate paws, extra animals, readable signage, logos or watermarks. Preserve natural face and fur texture; this should feel like a detailed travel photograph, not a cut-and-paste collage.
```

</details>

## G14 · A cutout that only looks transparent

Category: [Create a transparent product cutout](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#create-a-transparent-product-cutout). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/extract-product-gpt-image-2-5-sunburst.webp). Product extraction.

![A cutout that only looks transparent](../expanded-experiments/edit-coverage/g14.png)

**Method.** Name the bottle as the extraction target, preserve its silhouette and printed label, and define transparency as alpha values rather than a pictured background. Inspect the saved file instead of trusting a checkerboard preview.

**Observed.** The first output is an RGB PNG with a painted checkerboard and no real alpha. A second attempt from the clean source, with stronger RGBA wording, fails in the same way. Both keep the bottle recognizable; neither is a usable transparent cutout.

**Next action.** Use a path with actual alpha or background-removal controls, then inspect its file pixels. Stop treating repeated wording as proof of a format fix.

**Technique to keep.** Prompts describe intent; tool controls and metadata establish file properties. A failed cutout is still a useful experiment when retained honestly.

**Comparison boundary.** The extraction goal remains similar, but settings and backend are unexposed. These failures do not show that named GPT Image 2.5 models lack transparency support.

Saved original: 1254 × 1254 PNG (RGB).

**Inputs, in attachment order:**

- [shampoo.webp](../expanded-experiments/edit-coverage/inputs/shampoo.webp): exact product identity and typography.


<details><summary>Exact submitted prompt</summary>

```text
Image 1 is the exact product to extract. Return a square PNG cutout with genuine transparent alpha outside the bottle. Remove the wooden tabletop, tan wall, and cast shadow completely; do not replace them with white, gray, black, a checkerboard pattern, or a painted transparency effect.

Preserve the single peach-orange shampoo bottle, its rounded shoulder, cylindrical body, flip-top cap, front-facing orientation and warm product shading. Preserve its printed black label faithfully: WOMEN; SHAMPOO; FOR; NORMAL HAIR; 12 FL OZ (355 mL). Keep the existing typography and line positions rather than redesigning packaging. Retain the whole cap and bottom silhouette, centered with a small transparent margin. Keep opaque bottle interiors opaque and fine edge antialiasing natural. No extra objects, text, drop shadows or reflections outside the bottle.
```

</details>

### G14-R1 · Stronger alpha wording, still opaque

![Stronger alpha wording, still opaque](../expanded-experiments/edit-coverage/g14-alpha-repair.png)

The single repair attempt still failed: stronger RGBA/alpha-value wording produced a second opaque painted checkerboard. No actual cutout was achieved.

<details><summary>Exact follow-up prompt</summary>

```text
Extract only the peach-orange shampoo bottle from the attached original product photo. The deliverable is a real transparent PNG file in RGBA mode: every background pixel outside the bottle must have alpha 0, the opaque bottle interior must have alpha 255, and only boundary antialiasing may use intermediate alpha. Do not depict transparency as an image. Do not paint any checkerboard, grid, gray tiles, white backdrop, black backdrop, wall, table, cast shadow or reflection outside the object.

Keep the original bottle silhouette, flip-top cap, orange color, warm shading, orientation and label layout. Preserve the printed words WOMEN, SHAMPOO, FOR, NORMAL HAIR, and 12 FL OZ (355 mL). Center the whole bottle on a square canvas with a small genuinely transparent margin. This is an extraction, not a packaging redesign. Return the actual transparent RGBA PNG, not a preview of an object on a transparency pattern.
```

</details>

## G15 · An alpine botanical station from a sketch

Category: [Turn a drawing into a realistic image](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#turn-a-drawing-into-a-realistic-image). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/realistic-valley-gpt-image-2-5-sunburst.webp). Realistic valley.

![An alpine botanical station from a sketch](../expanded-experiments/edit-coverage/g15.png)

**Method.** Treat drawn lines as geometry, not texture. List the mountain slopes, river path and tree anchor. Separately mark three glasshouses, one bridge and one path as intentional additions instead of recovered information.

**Observed.** The main valley, river and tree relationships transfer into a detailed landscape. The three glasshouses, bridge and path are present. Exact drawn contours and relative geometry remain approximate.

**Next action.** If layout accuracy matters, approve a clearer region map for the tree and river before pursuing more realism.

**Technique to keep.** A sketch carries layout evidence. Separate what it specifies from what the prompt invents.

**Comparison boundary.** Intent expanded with a new research station and landscape format. This tests an uploaded drawing, not the native ChatGPT Sketch interface.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [drawings.webp](../expanded-experiments/edit-coverage/inputs/drawings.webp): layout and perspective only; no bridge exists in source.


<details><summary>Exact submitted prompt</summary>

```text
Image 1 is a composition sketch only. Its black lines are layout marks, not objects or the final visual style. Build a photorealistic landscape 3:2 alpine botanical research station from this map.

Preserve these spatial anchors: two mountain slopes descend from the upper left and upper right into the central distant valley; a winding river begins near the middle horizon and broadens in S-curves toward the lower foreground; one large leafy tree stands on the right foreground bank; scattered smooth rocks trace the river edges. Keep the river banks and large tree close to their sketched positions and relative scale. Convert the central drawn sun into natural sunrise glow in the same valley opening, rather than a giant solid disc. Four loose cloud groups occupy the upper sky where the sketch indicates them.

Intentional additions, not features recovered from the sketch: put exactly three low glass greenhouses on planted stone terraces on the left riverbank, in the middle distance. Add one slender wooden footbridge across the river in the middle distance, below the valley opening and behind the foreground tree. Connect the greenhouses to the bridge with one gravel footpath. Keep the river open and visible around and beneath the bridge.

Render lush alpine specimen gardens, dew on meadow grasses, weathered stone retaining walls, detailed greenhouse metal frames and glazing, distant snow traces on rocky mountain ridges, clear turquoise river water over visible stones, and soft low sunlight with cool valley haze. Retain a spacious sky and deep layered distance. No labels, drawn outlines, cartoon sun rays, extra bridges, large buildings or people. The final scene must follow the sketch's main layout while looking like a plausible high-resolution landscape photograph.
```

</details>

## G16 · Remove the cap, keep the flower

Category: [Remove an object](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#remove-an-object). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/man-with-no-flower-gpt-image-2-5-sunburst.webp). Flower removed.

![Remove the cap, keep the flower](../expanded-experiments/edit-coverage/g16.png)

**Method.** Identify one deletion target including its crown and brim. List the flower, fingers, face, shirt graphic and wall as protected elements. Mark the newly exposed scalp as unknown and request a plausible completion only there.

**Observed.** The cap is removed while the flower, pose, portrait and main background remain visually consistent. Newly visible hair is plausible but cannot be verified against content hidden in the source.

**Next action.** No additional edit is needed for this brief. Keep the uncertainty note if presenting this as reconstruction.

**Technique to keep.** Object removal often invents an occluded surface. Preserve the visible evidence without pretending the hidden original is known.

**Comparison boundary.** The deletion target changed. This is a separate local-edit demonstration rather than a quality comparison for the same removal.

Saved original: 1024 × 1536 PNG (RGB).

**Inputs, in attachment order:**

- [man-with-blue-hat.webp](../expanded-experiments/edit-coverage/inputs/man-with-blue-hat.webp): edit target; cap removal only.


<details><summary>Exact submitted prompt</summary>

```text
Edit image 1 by removing only the blue baseball cap. The cap is the sole deletion target, including its crown and brim. Reconstruct only the newly exposed scalp with plausible short dark hair that connects naturally to the hair already visible at the temples. The hidden original hairstyle is unknown; do not change the visible face to invent a new person.

Preserve the man's facial features, smile, teeth, stubble, ears, gaze, head tilt and skin texture. Preserve the white daisy with yellow center, its green stem, the fingers holding it, the hand pose and arm. Preserve the white T-shirt, green pine-tree graphic, fabric folds, colorful graffiti brick wall, background texture, original crop, camera view, light and color. Do not remove the flower, beautify the face, alter the shirt graphic, clean the wall, add text or change any other object. Keep the original portrait 2:3 composition.
```

</details>

## G17 · Carry the wardrobe into an action scene

Category: [Insert a person into a scene](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#insert-a-person-into-a-scene). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/scene-gpt-image-2-5-sunburst.webp). Runner and bear.

![Carry the wardrobe into an action scene](../expanded-experiments/edit-coverage/g17.png)

**Method.** Use the wardrobe output only for person and clothing, and the action image for scene, pose, scale and light. State that the existing runner is replaced, so the required person count remains one. Lock distinct campsite anchors.

**Observed.** The woman and outfit integrate into the running action while bear, tent, case, chair, trees and mountain stay in the expected arrangement. Dust is heavier than requested, and fine textures redraw, but the main substitution succeeds.

**Next action.** If garment cleanliness matters, reduce dust only in the named clothing regions. Do not regenerate a successful scene merely to make it different.

**Technique to keep.** A person reference and a scene reference should have distinct responsibilities; specify replacement versus addition explicitly.

**Comparison boundary.** The published scene is an input to our replacement edit. It cannot also function as an independent matched baseline.

Saved original: 1024 × 1536 PNG (RGB).

**Inputs, in attachment order:**

- [g12.png](../expanded-experiments/edit-coverage/g12.png): person identity and clothing only; generated G12 result.
- [scene-gpt-image-2-5-sunburst.webp](../expanded-experiments/official-references/scene-gpt-image-2-5-sunburst.webp): scene, existing runner pose, scale, camera, lighting.


<details><summary>Exact submitted prompt</summary>

```text
Image 1 supplies the person and clothing only: the dark-haired woman in beige blazer, white tank top, black jeans and gray knee-high boots. Image 2 is the exact scene, camera and action-pose reference: a runner escaping a bear through a mountain campsite. Replace image 2's existing runner with the woman from image 1 so there is still exactly one person. Do not add a second person and do not copy the museum background.

Preserve the referenced woman's facial structure, apparent age, dark hair and recognizable identity while giving her a natural alarmed expression. Preserve her beige blazer, white tank, black jeans and gray boots from image 1; add only plausible motion folds and a light amount of trail dust. Adapt her body to image 2's running pose, direction and scale, with one knee raised and arms moving naturally. Her face must remain visible and her footwear must meet the terrain plausibly.

Lock the rest of image 2: the pursuing brown bear on the left, damaged gray tent and green storage case on the right, overturned dark camp chair on the left, scattered gear, pine trunks, rocky leaf-strewn ground, distant granite mountain profile and warm evening sky. Match the existing scene's depth of field, perspective, muted natural colors, lighting and grounded contact shadows. Maintain the original portrait 2:3 framing. Keep the image photographically credible; no dramatic new explosions, extra wildlife, wounds, blood, text, logos or watermark.
```

</details>

## G18 · A conservatory product campaign

Category: [Create the starting image](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#create-the-starting-image). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/billboard-gpt-image-2-5-sunburst.webp). Billboard at sunset.

![A conservatory product campaign](../expanded-experiments/continuity/g18.png)

**Method.** Use the product reference for bottle shape, color and label spelling. Build the setting around a wet basalt pedestal, left ferns, right orchid and background glass arches. Keep the label clear and reserve a copy-free top quarter.

**Observed.** The bottle, plants, reflections and warm atmospheric light form a coherent campaign. Label words survive, but typeface and fine bottle geometry are redrawn. The exact three-arch count is uncertain because glass ribs overlap and blur.

**Next action.** If three arches are essential, give each arch a distinct mapped location. For brand production, compare actual letterforms and packaging geometry with the source.

**Technique to keep.** A product reference can anchor identity while the setting changes; readable label spelling is weaker than exact packaging preservation.

**Comparison boundary.** Intent changed to a miniature conservatory campaign. The comparison demonstrates a different setting and framing, not greater effectiveness for the same advertisement.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [shampoo.webp](../expanded-experiments/official-references/shampoo.webp): bottle identity and label.


<details><summary>Exact submitted prompt</summary>

```text
Create a polished landscape 3:2 photographic campaign image. Image 1 supplies the exact peach shampoo bottle: preserve its cylindrical proportions, cap, peach color and the visible label spelling. Place one bottle in the lower-middle on a wet dark basalt pedestal. Build an intricate miniature botanical conservatory around it: three tall glass arches in the background, broad fern fronds at image-left, a single pale orchid stem at image-right, and fine suspended water droplets. Late afternoon sunlight from upper-left passes through humid air; glass, droplets and polished basalt have coherent reflections. The bottle is the clear focal point and its front label faces the viewer. Keep every prop behind or beside the bottle rather than covering it. Reserve the top quarter as softly lit atmosphere without lettering. This is a fictional art-directed campaign, not a claim about ingredients. No added words, people, logos or second bottle. Preserve readable source label rather than inventing new brand copy.
```

</details>

## G19 · The same campaign in a rainstorm

Category: [Change one condition](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#change-one-condition). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/billboard-winter-gpt-image-2-5-sunburst.webp). Billboard in snow.

![The same campaign in a rainstorm](../expanded-experiments/continuity/g19.png)

**Method.** Edit the accepted campaign with one environmental change. Keep bottle, label, crop, pedestal and plants fixed, while explicitly allowing the light, reflections and atmosphere to respond physically to rain and blue hour.

**Observed.** The rainstorm and cool light read clearly, with bottle and major composition retained. New warm light points appear behind the bottle despite the no-extra-props intent. The inherited arch-count uncertainty remains.

**Next action.** Decide whether those lights are acceptable; otherwise map and remove only the added light sources, preserving the storm and bottle.

**Technique to keep.** A condition change propagates to lighting and materials. Specify permitted consequences and inspect for newly invented objects.

**Comparison boundary.** This uses our campaign and a different weather target. Within our pair, the requested condition changes successfully with a collateral addition.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [g18.png](../expanded-experiments/continuity/g18.png): accepted campaign edit target.


<details><summary>Exact submitted prompt</summary>

```text
Edit the supplied accepted campaign image. Change only the time and weather from late-afternoon sunlight to a blue-hour rainstorm: cool ambient sky, rain streaks and damp atmospheric haze. Preserve the bottle identity, exact label, cap, position and proportions; pedestal, three glass arches, ferns, orchid, camera, crop and overall composition. Allow physically necessary changes to light, reflections, wet highlights and atmosphere. Keep the label readable without adding a spotlight object. No extra plants, lettering, people or bottles. Return the same 3:2 framing.
```

</details>

## G20 · Meet the Atlas Keeper

Category: [Establish the character](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#establish-the-character). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/childrens-book-illustration-1-gpt-image-2-5-sunburst.webp). Forest hero.

![Meet the Atlas Keeper](../expanded-experiments/continuity/g20.png)

**Method.** Make character identity inspectable: round ivory head, two eye colors tied to image sides, one gold crescent, teal scarf and red satchel. Place that small character in a much larger floating library to create scale.

**Observed.** All listed signature traits are visible, with one robot, coherent compass contact and a deep floating-library environment. No planned visible criterion fails. This is the starting identity image for later scenes and merchandise.

**Next action.** Use this accepted output as the identity reference and list which traits must persist in each new view.

**Technique to keep.** A recurring character needs a small set of visible anchors that can survive changes of scene and pose.

**Comparison boundary.** Intent changed to an original ceramic robot and new world. The richer environment is a creative choice, not a controlled model comparison.

Saved original: 1536 × 1024 PNG (RGB).

<details><summary>Exact submitted prompt</summary>

```text
Create a visually rich 3:2 landscape storybook diorama of an Atlas Keeper discovering a floating library at dawn. The Keeper is a small ivory ceramic robot, full body visible in the left foreground, with a round head, two circular eyes (amber on image-left, cyan on image-right), one tiny gold crescent on its forehead, short jointed arms and legs, a teal neckerchief and one red rectangular satchel at its right hip. One hand rests on an open brass compass. In the middle distance a vast circular library is built into a floating stone island: curved shelves, delicate brass bridges, hanging gardens, warm reading-room windows, and a tall central glass dome. A broad stone stair curves from the Keeper toward the library; an immense sea of clouds gives clear depth and scale. Use tactile stop-motion ceramic and paper materials with meticulous miniature details, warm ivory, copper, deep teal and small red accents. Warm sunlight enters from upper-left. Keep the Keeper's eyes, crescent and satchel easy to inspect. One robot only. No people, extra eyes, titles or written labels.
```

</details>

## G21 · The Keeper enters the observatory

Category: [Continue the story](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#continue-the-story). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/childrens-book-illustration-2-gpt-image-2-5-sunburst.webp). Winter story continuation.

![The Keeper enters the observatory](../expanded-experiments/continuity/g21.png)

**Method.** Carry only the Keeper identity into a new room. Retain colored eyes, crescent, scarf and satchel, then change pose, location and lighting. Specify both hand contact with the compass and the armillary sphere at image-left.

**Observed.** The character anchors and new observatory work. The armillary sits on a pedestal even though the prompt requested suspension. The initial checklist omitted that relationship, so its passing checks did not cover the full brief.

**Next action.** Add suspended versus supported to the checklist, then repair only the sphere support if suspension matters to the scene.

**Technique to keep.** Review the original brief alongside the checklist. An omitted requirement can make a score look better than the actual result.

**Comparison boundary.** Intent changed in character, setting and action. Our own continuity pair shows retained signature traits, not universal identity reliability.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [g20.png](../expanded-experiments/continuity/g20.png): Keeper identity only.


<details><summary>Exact submitted prompt</summary>

```text
Use image 1 solely as the Atlas Keeper character reference. Continue the story in a new 3:2 landscape scene: the same small ivory ceramic robot now stands on the right side of a vast midnight observatory, holding its open brass compass in both hands while looking toward an enormous suspended brass armillary sphere at image-left. Preserve the same round head, exactly two round eyes (amber on image-left and cyan on image-right in the visible near-frontal face), one tiny gold forehead crescent, teal neckerchief, short jointed limbs and red rectangular satchel. Surround the observatory with intricate arched shelves, spiral stairs, blue glass star windows and fine brass measuring instruments. Moonlight enters from upper-left; warm lamps give restrained amber accents. Keep tactile ceramic and paper miniature craft, with great depth and readable silhouettes. The original library exterior and cloud sea should not be copied into this new room. Exactly one Keeper and one huge armillary sphere. No added words, people or extra eyes.
```

</details>

## G22 · Green upholstery and a copper pendant

Category: [Change furniture in a room](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#change-furniture-in-a-room). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/kitchen-chairs-gpt-image-2-5-sunburst.webp). Wooden replacement chairs.

![Green upholstery and a copper pendant](../expanded-experiments/continuity/g22.png)

**Method.** Assign two independent edits to named objects: four chair seats become green while black legs stay black; pendant cage and chain become copper while geometry stays fixed. Compare one combined request with the same changes in two stages.

**Observed.** The combined result and the final sequential result both achieve the materials and preserve the broad room. Both regenerate fine detail. The combined route uses one call; the sequential route uses two and redraws surfaces again.

**Next action.** Use a combined request when changes are independent and easy to verify. Split changes when dependencies or diagnosis make intermediate review valuable.

**Technique to keep.** One element at a time is a diagnostic strategy, not a universal rendering advantage. This single pair does not establish general reliability.

**Comparison boundary.** The requested room changes differ from the published example. A separate local comparison tests bundled versus sequential execution on our own two-change goal.

Saved original: 1448 × 1086 PNG (RGB).

**Inputs, in attachment order:**

- [kitchen.webp](../expanded-experiments/official-references/kitchen.webp): kitchen edit target.


<details><summary>Exact submitted prompt</summary>

```text
Edit the supplied kitchen photo with two precisely scoped changes. First, recolor the upholstery of all four existing white dining chairs to deep forest green, retaining their exact shapes, stitched channels, positions and black legs. Second, change the black metal cage and chain of the hanging pendant lamp to brushed copper, retaining the lamp's exact geometry and hanging position. Preserve all other source content: four-chair count, circular glass table, striped vase and dried flowers, window frames and outdoor view, refrigerator, cabinetry, globe, countertop, plants, ceiling vent, floor, camera, crop and daylight. Allow local reflections and small color spill needed by the new materials. No other changes; same 4:3 image framing.
```

</details>

### E22A · First edit separately

![First edit separately](../expanded-experiments/continuity/e22a.png)

Green chairs retained; pendant remains black.

<details><summary>Exact follow-up prompt</summary>

```text
Edit the supplied kitchen photo. Recolor only the upholstery of all four white dining chairs to deep forest green. Retain their exact shapes, stitched channels, positions and black legs. Preserve the black pendant lamp, circular glass table, striped vase, dried flowers, windows and outdoor view, refrigerator, cabinetry, globe, countertop, plants, ceiling vent, floor, camera, crop and daylight. Allow only necessary small local reflections from the upholstery. No other changes; keep 4:3 framing.
```

</details>

### E22B · Second edit separately

![Second edit separately](../expanded-experiments/continuity/e22b.png)

Green chairs retained; pendant becomes copper. Fine texture is regenerated.

<details><summary>Exact follow-up prompt</summary>

```text
Edit the supplied green-chair kitchen image. Change only the metal cage and chain of the hanging black pendant lamp to brushed copper. Keep the precise lamp shape and hanging position. Preserve all four forest-green chairs, stitched channels and black legs; glass table, striped vase, dried flowers, windows/outdoor view, refrigerator, cabinets, globe, countertop, plants, ceiling vent, floor, crop and daylight. Allow necessary small copper reflections. No other changes. Same 4:3 framing.
```

</details>

## G23 · Winter Atlas

Category: [Design a holiday card](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#design-a-holiday-card). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/christmas-holiday-card-teddy-gpt-image-2-5-sunburst.webp). Teddy greeting card.

![Winter Atlas](../expanded-experiments/continuity/g23.png)

**Method.** Reuse the Keeper identity but create a new snow scene. Reserve a measured title region, provide exact heading and footer, and define snowy bridge, observatory, evergreens and cream outer margins as separate layers.

**Observed.** WINTER ATLAS and the full footer are correct; signature character traits and layered scenery persist. The robot faces the viewer instead of clearly walking toward the observatory, so the intended action does not read.

**Next action.** Specify a visible stride and body orientation toward the observatory, with the face turned enough to retain identifying eye details.

**Technique to keep.** Copy can succeed while narrative direction fails. Check where a body is headed, not simply whether the character is present.

**Comparison boundary.** Intent changed to a recurring original character and new greeting. This tests reuse with typography, not a matched greeting-card improvement.

Saved original: 1024 × 1536 PNG (RGB).

**Inputs, in attachment order:**

- [g20.png](../expanded-experiments/continuity/g20.png): Keeper identity only.


<details><summary>Exact submitted prompt</summary>

```text
Create a finished portrait 2:3 winter greeting card using image 1 as the Atlas Keeper character identity reference only. Show the same ivory ceramic robot, two colored round eyes, forehead gold crescent, teal scarf and red satchel walking on a snowy stone bridge toward an illuminated glass observatory. Layer intricate dark evergreen silhouettes, drifting snow and a navy twilight sky; warm gold light glows from tiny windows. Use beautifully detailed cut-paper and ceramic miniature illustration with an elegant cream outer paper margin. Reserve the upper 18 percent for the exact heading "WINTER ATLAS" in large refined serif lettering. Below the illustrated scene, typeset exactly "MEET ME WHERE THE LIGHT RETURNS" in small widely spaced uppercase. Those are the only two text strings. One robot, no human figures, no religious symbols. Keep all letters readable, the robot inside the frame, and the source face/outfit recognizable.
```

</details>

## G24 · Atlas Keeper — Field Edition

Category: [Design collectible merchandise](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#design-collectible-merchandise). [Published example](https://developers.openai.com/images/platform/guides/image-prompting/christmas-collectible-toy-airplane-gpt-image-2-5-sunburst.webp). Packaged airplane.

![Atlas Keeper — Field Edition](../expanded-experiments/continuity/g24.png)

**Method.** Use the identity image for the toy alone. Map the figure to the left compartment and exactly three accessories to separate right compartments. List the three allowed text strings and define plastic, paper and studio light.

**Observed.** The character traits, three accessory compartments, compass, book, lantern and main copy are all present. Tiny compass markings may contain extra letters, so the strict no-other-text requirement remains uncertain.

**Next action.** For exact packaging copy, inspect tiny instrument faces as well as the card. Replace ambiguous compass lettering with unlettered ticks if needed.

**Technique to keep.** A reference can become a different material and product format while recognizable traits persist; microtext remains part of the text audit.

**Comparison boundary.** Intent changed to our character, accessory inventory and package design. It demonstrates format transfer, not superiority over a different collectible.

Saved original: 1536 × 1024 PNG (RGB).

**Inputs, in attachment order:**

- [g20.png](../expanded-experiments/continuity/g20.png): Keeper identity only.


<details><summary>Exact submitted prompt</summary>

```text
Create a high-end 3:2 landscape studio photograph of a collectible Atlas Keeper toy in a clear molded blister on an off-white illustrated backing card. Image 1 controls the toy character only: ivory ceramic round head, amber image-left eye and cyan image-right eye, one gold forehead crescent, teal neckerchief, short jointed limbs and red rectangular satchel. The figure stands in the left compartment. Three separate accessory compartments stacked at right contain exactly one brass compass, one closed teal book and one tiny copper lantern. Printed heading on the card: "ATLAS KEEPER". Small subtitle: "FIELD EDITION". A single circular badge says "01". No other text. Include a finely drawn faint observatory pattern on the backing without extra letters. Use precise product photography, subtle clear-plastic reflections, paper texture and soft upper-left studio light on a dark teal tabletop. Entire package fully visible, no hands or extra toys. Preserve the character's signature details; do not reproduce the reference environment.
```

</details>
