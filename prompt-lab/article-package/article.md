# how to turn an image in your head into an image you can actually use

i’ve always struggled with image prompting. the prompts people share often feel made up: a pile of impressive words, followed by a beautiful result, with no explanation of which decisions mattered.

when my result looks wrong, that gives me very little to work with.

so we built a workflow around something more useful: making the visual decisions visible, generating an image, and checking whether those decisions survived.

we tried it on luxury product photography, fashion apps, packaging, interiors, posters, illustrations, character scenes, and complicated diagrams. the accompanying guide contains 44 studies, their actual prompts, and their results.

some worked. some needed repairs. some repairs made other details worse.

that last part matters. learning to direct an image includes learning when to keep it, when to change it, and when to use a different tool.

![The generated SABLE fashion app presentation, showing three aligned screens.](evidence/premium-examples/images/01-fashion-app.png)

*SABLE: our generated fashion app concept after correcting the middle screen’s selected category and navigation. a convincing interface still needs a functional review.*

## 1. start by deciding what the image must do

“make it premium” expresses a preference. you still have to decide what someone will see.

for a fashion app, that might mean generous spacing, consistent product photography, quiet typography, and a bag that looks identical across screens.

for a perfume campaign, it might mean garnet glass, a walnut cap, believable reflections, and enough contrast to read the label.

for a thumbnail, it might mean one room, one transformation, and four words that survive being viewed on a phone.

write a brief in this order:

1. **purpose:** what will the image help someone understand, feel, or do?
2. **canvas:** where will it appear, and what shape must it have?
3. **contents:** which subjects, objects, and exact words belong in it?
4. **relationships:** where are they, what touches what, and what comes first?
5. **appearance:** what should the materials, light, color, and typography look like?
6. **checks:** what would make the result unusable, even if it looks beautiful?

this becomes the prompt’s structure. every sentence should make a visible decision or protect one.

## 2. understand why complex images work

look at OpenAI’s published coffee-machine infographic.

![OpenAI’s published coffee-machine infographic, with a central cutaway, numbered components, flow legend, and process steps.](evidence/expanded-experiments/official-references/infographic-coffee-machine-gpt-image-2-5-sunburst.webp)

*source: [OpenAI’s GPT Image 2.5 prompting guide](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5#explain-a-process-visually), Sunburst example. this is OpenAI’s image. its engineering details were not independently validated here.*

the complexity has an organization. a central cutaway explains the machine. numbered components identify its parts. colored paths distinguish flows. a separate strip explains the sequence.

you can name these systems before writing the prompt:

- the subject people should notice first;
- the parts they need to identify;
- the connections they need to follow;
- the labels that explain those connections;
- the space that keeps everything readable.

we used that principle for a fictional ecosystem called THE RAIN ENGINE: five separated tiers, distinct materials, four downward arrows, one return arrow, and six exact text strings.

![Our generated Rain Engine poster with five separated tiers.](evidence/expanded-experiments/language/trial-S2.png)

*G02: our adaptation changes the subject and purpose. it demonstrates a workflow; it cannot establish that our prompt is better than OpenAI’s.*

the awe comes from a coherent world that rewards inspection. adding objects without deciding their relationships usually makes the image harder to read.

## 3. create a new image by building its hierarchy

our SABLE app started with three screen roles: discovery, collection, and product detail.

then we specified the product inventory, prices, active controls, material treatment, and recurring bag design. the model had a concrete interface to compose.

this passage is an exact excerpt from the submitted prompt:

> Make the bag design match between middle and right screens. No gibberish microcopy or extra badges. The premium quality comes from typography, photography, material fidelity and restraint.

the initial result looked polished, but the collection mixed clothes and accessories under the wrong selected category. the navigation state also needed correction.

we repaired those two functional details. the accepted version selects “All” and activates “Shop” on the middle screen, while the discovery screen keeps “Discover” active.

**the lesson:** review what the design means, as well as how it looks.

for your own app, write the screen roles first. for a poster, write the reading order. for a product image, decide the product’s size, placement, and relationship to the light.

the accompanying examples let you practice that translation across formats:

- **book covers and posters:** specify the title, visual metaphor, reading order, and clear margins;
- **flyers and advertisements:** separate the message, product, supporting information, and action;
- **icons and logos:** define silhouette, stroke consistency, small-size readability, and background requirements;
- **headshots:** preserve identity while changing wardrobe, framing, or light;
- **interiors and cross-sections:** distinguish visible design from hidden construction you are asking the model to invent.

our thumbnail reads clearly, but misses its requested margin. our icons improved after cleanup, but still contain faint texture. those details help you decide which outputs are ready for your actual use.

## 4. make premium quality observable

our VELLUM perfume study used a garnet bottle, walnut cap, restrained label, and an architectural setting. glass, wood, and stone needed visibly different behavior.

![VELLUM perfume in a warm architectural product photograph.](evidence/premium-examples/images/02-luxury-product.png)

*the generated result has strong material separation and readable label copy. the cap is taller and the surface more veined than requested.*

that is a useful result with specific deviations. “looks expensive” would have missed them.

our synthetic skincare UGC image needed different decisions: believable phone-camera framing, natural skin, a relaxed hand holding the product, and ordinary bathroom light.

polishing that image into a flawless studio advertisement would undermine its purpose.

before generating, translate your aesthetic into observable choices:

- **materials:** fine leather grain, weighted wool, brushed metal, translucent glass;
- **light:** direction, softness, reflections, and shadows that agree;
- **composition:** clear emphasis, breathing room, intentional cropping;
- **finish:** readable type, clean edges, believable contact between objects.

use only the choices the image needs. contradictory directions create another problem for the model to resolve.

## 5. reconstruct a reference with a visual map

when you already have an image, start by inventorying it.

separate meaningful elements: background, subjects, objects, text, arrows, shadows, and groups. give each one a stable name and identifier.

for THE RAIN ENGINE, we created 50 named regions. the interface shows the unchanged source image, selection overlays, and individual crop previews.

you can select the return arrow without repeatedly describing “the big curved thing on the right.” it has an identifier: `A-48`.

![Rain Engine after changing its large return arrow to deep magenta.](evidence/expanded-experiments/mapping/selected-arrow-edit.png)

*the selected edit changed the arrow’s color while retaining the five tiers, six strings, turquoise water, and four copper arrows. fine textures were redrawn.*

the map should record:

1. the element’s name and visible description;
2. its approximate position and size;
3. its color, material, and relevant text;
4. its relationships with other elements;
5. what may change and what must remain;
6. what cannot be inferred from the pixels.

a bounding box gives you a location. a crop gives you a preview. neither automatically provides a transparent layer or an exact object mask.

build the inventory in three passes. first, map the large silhouettes and empty spaces. second, record relationships: behind, inside, touching, pointing toward. third, add surface details and exact text.

this prevents a detailed description of the bottle label from distracting you from a bottle that occupies the wrong half of the frame.

then show the map to the person directing the image. let them select, rename, lock, remove, or replace the parts that matter. keep their choices attached to stable identifiers so the next edit can reuse them.

ChatGPT’s image comments are useful for a quick local request. a reusable map becomes valuable when you need a persistent inventory, several edits, or decisions another agent can follow.

## 6. save those decisions as reconstruction JSON

the JSON is a structured description of the visible image, with a separate record of requested changes.

it cannot recover the original prompt, hidden geometry, source layers, or exact font from appearance alone. mark those unknowns explicitly.

this excerpt uses the actual selected-edit fields from our reconstruction file:

```json
{
  "target_id": "A-48",
  "action": "restyle",
  "properties": ["appearance.color"],
  "instruction": "Change only the turquoise color of the large return arrow to deep magenta. Preserve its existing light-to-dark shading pattern; do not change the teal water or dark teal lettering."
}
```

the full file also holds the other elements, relationships, protected properties, and checks. the compiler turns that inventory into readable instructions.

for a close recreation, prioritize silhouette, proportions, spacing, and the relationships that make the source recognizable. then refine surfaces and small details. if you want a new composition using selected ingredients, state that explicitly before compiling the prompt.

keep the original observations intact when an edit changes something. the source arrow was turquoise; the requested arrow is magenta. those facts belong in different fields, otherwise the agent can accidentally ask for both colors.

also update the checks after a deliberate change. a rule that still requires a turquoise arrow would incorrectly reject the very edit you approved. the included skill carries that distinction into its workflow.

we tested a compiled description alone and the description with the source image. both preserved the broad five-tier idea. the version with the reference stayed closer to the source’s typography, spacing, and silhouettes.

each condition had one completed result. this suggests a useful workflow; it does not establish a success rate.

one raw-JSON request was rejected before generating an image. that is recorded separately from visual failures.

## 7. assign every reference a job

references can supply different information. one might define a person, another a garment, another the composition, and another the palette.

write those roles down. otherwise you leave the model to decide which aspects to borrow.

in our botanical railway experiment, we tried the same descriptive scene with a person reference, a dog reference, and both references.

![Botanical railway scene generated with both subject references.](evidence/expanded-experiments/reference-matrix/trial-M3.png)

*the two-reference result stayed closer to the intended subjects in this small comparison. all three variants still added marks to a clock that should have been blank.*

references helped identity while another constraint continued to fail.

our OFFDAY studies show how this transfers to commercial work. the packaging supplied the visual identity for a can advertisement, merchandise, and a logo extraction.

![OFFDAY packaging with coordinated coral and blue cans.](evidence/premium-examples/brand/packaging.png)

*packaging became an input to related assets. the extracted logo remains a raster study, and the mockups are not production packaging files.*

when combining references, say which image controls identity, layout, materials, or style. also say which visible details should not carry over.

## 8. use sketches when placement is the problem

if you keep explaining where a window, person, or building should go, draw the arrangement.

a useful sketch can be rectangles, silhouettes, a horizon, and a few arrows. its job is to communicate placement and relationships.

our uploaded room sketch carried the broad layout into a rendered interior. the first render added unwanted foliage outside the window; a targeted repair removed it.

in a richer study, a mountain sketch became an alpine botanical station. the prompt deliberately added three glasshouses and a bridge, while using the sketch for the valley composition.

![Alpine botanical station generated from the supplied mountain sketch.](evidence/expanded-experiments/edit-coverage/g15.png)

*G15: the uploaded drawing guided the scene. the output approximates the terrain rather than tracing every contour.*

OpenAI documents a native `@Sketch` feature in ChatGPT: draw a reference, then describe the style and details you want. our experiments used uploaded drawings; we did not separately verify that native interface. [OpenAI announcement](https://openai.com/index/introducing-chatgpt-images-2-5/)

keep the drawing simple enough to read. explain which marks represent objects, which indicate motion, and which should disappear from the finished image.

## 9. use simpler language, then test the difference

we compared plain prose with labeled sections using the same visual requirements. there were two outputs per format.

the main objects and text survived in both. a later review found clearer leader-line placement in the labeled versions, but the reviewers did not agree on every judgment.

that is a limited observation, not a universal formatting rule.

we also compared the plain wording with more technical vocabulary. those samples did not demonstrate that jargon was necessary or generally better.

start with words you can explain. use a technical term when it specifies something useful, such as an isometric view or a soft light source.

research supports breaking evaluation into concrete questions. GenEval examines objects, counts, position, and color; Davidsonian Scene Graphs organize checks around individual facts and their dependencies. neither promises a universal prompt formula. [GenEval](https://arxiv.org/abs/2310.11513), [DSG](https://arxiv.org/abs/2310.18235)

a better-caption training study also cannot prove that making your prompt longer will improve every image. [OpenAI’s DALL·E 3 paper](https://cdn.openai.com/papers/dall-e-3.pdf)

## 10. change one thing when you need to diagnose it

one change at a time makes cause and effect easier to inspect. it can also add more generation steps, each with another opportunity for drift.

we compared changing upholstery and a pendant together with doing those edits sequentially. both routes achieved the broad requested changes. both changed fine textures.

the sequential route did not earn a universal advantage.

use this decision rule:

- **one uncertain change:** isolate it so you can inspect the consequence;
- **two clear, compatible changes:** a combined edit may be sufficient;
- **dependent changes:** sequence them when the second needs the first result;
- **exact preservation:** use a mask, layer, or deterministic editing tool when available.

write each edit as **change / preserve / allow**. changing sunlight into a rainstorm should allow reflections and wet highlights to change too.

otherwise your preservation instructions may conflict with the effect you requested.

here is the exact storm-edit prompt we submitted:

> Edit the supplied accepted campaign image. Change only the time and weather from late-afternoon sunlight to a blue-hour rainstorm: cool ambient sky, rain streaks and damp atmospheric haze. Preserve the bottle identity, exact label, cap, position and proportions; pedestal, three glass arches, ferns, orchid, camera, crop and overall composition. Allow physically necessary changes to light, reflections, wet highlights and atmosphere. Keep the label readable without adding a spotlight object. No extra plants, lettering, people or bottles. Return the same 3:2 framing.

![The conservatory product campaign after a blue-hour storm edit.](evidence/expanded-experiments/continuity/g19.png)

*G19: the scene and bottle remained recognizable, but the edit introduced unrequested warm light points. the next correction would target those lights while protecting the accepted weather and composition.*

## 11. inspect the failure before writing another prompt

our color-only upholstery edit also changed the fabric’s visible texture. an additional repair did not restore it. the sensible choice was to keep the earlier acceptable image.

a shampoo cutout looked transparent because it showed a checkerboard. the saved file was opaque RGB. the repair repeated the problem.

an infographic printed the right numbers while its bar lengths were only approximate. a leaf cutaway looked educational while one label pointed to the wrong structure.

these are different failures. each needs a different check:

1. read every required word;
2. count objects and follow arrows to their endpoints;
3. compare protected regions against the accepted source;
4. inspect dimensions and transparency in the actual file;
5. measure charts and verify factual labels before publishing them.

check accuracy before rewarding beauty. a polished image can make an error harder to notice.

## 12. let agents explore controlled alternatives

sub-agents can prepare different reference combinations, write candidate briefs, or review results independently.

give them the same target and checklist. change one meaningful input between branches, such as the reference set or the layout description.

ask each branch to return its exact prompt, attachments, output, observed failures, and proposed repair. keep filenames neutral for a reviewer where practical.

we used multiple agents across this project. that helped divide generation and review work; we did not establish that adding agents automatically improves image quality.

set a small candidate budget. compare the results before expanding it. more branches create more material to judge, including more ways to overlook the same mistake.

## 13. what changes with GPT Image 2.5?

OpenAI describes stronger editing and detail handling, offers Flare and Sunburst variants, and adds drawing and image-comment workflows in ChatGPT. those are vendor descriptions and documented product features. [OpenAI announcement](https://openai.com/index/introducing-chatgpt-images-2-5/)

our built-in generation tool did not expose the executing model, variant, seed, or quality setting. these experiments therefore cannot measure GPT Image 2.5 against an earlier version.

what you can reuse is the method: specify the result, provide the right visual information, inspect the output, and repair a diagnosed failure.

## 14. give your agent the whole loop

this is a reusable instruction for future work. it is separate from the exact image prompts used in the studies.

> inspect my idea and any references. identify the purpose, canvas, subjects, relationships, exact text, appearance, and nonnegotiable checks.
>
> for a reference, create a named visual inventory and reconstruction JSON. separate observations, unknowns, and requested changes. assign each attachment a role.
>
> choose text, references, a sketch, or a local edit according to the problem. write a clear prompt, generate a candidate, and save the actual prompt and inputs.
>
> inspect every hard requirement and protected region. report pass, fail, or uncertain. repair the most important diagnosed failure, then check for new damage.
>
> stop when the requirements pass, the agreed budget ends, or a different tool is needed. return the image, prompt, inputs, and remaining limitations.

the full prompt library, reconstruction skill, and 50-page guide make this workflow concrete. choose a study close to your task, inspect its result, and adapt its decisions.

for your first attempt, keep the process small:

1. choose one output you need, such as a product advertisement;
2. choose one reference and name the information it supplies;
3. write five requirements you can check by looking at the result;
4. generate a candidate and inspect those requirements before judging its overall appeal;
5. repair the largest failure, then compare everything you wanted to preserve;
6. save the accepted image with the prompt and the remaining limitations.

when a result improves, record the visible reason: the label became readable, the object count became correct, or the product matched its reference more closely.

that gives you a useful personal library of decisions and outcomes. repeating a successful choice is much easier when you know what it solved.

you do not have to memorize someone else’s paragraph. you need to know what you want to see, how you will recognize it, and what to change when the image misses.
