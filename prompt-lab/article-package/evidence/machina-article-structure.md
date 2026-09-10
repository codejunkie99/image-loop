i’d make this a personal field guide: **frustration → impressive results → understand the decisions → repeat the process yourself.**

Working title: **how to make the image you actually had in mind**

**1. “i could picture it. i couldn’t prompt it.”**

Open with your actual frustration:

> every image prompt i saved looked like someone made it up...
> i could see the image in my head. i just couldn’t explain it to the model.
> so i started breaking down what i was actually asking it to draw.

Immediately show the floating library, the campaign image, and the detailed Rain Engine diagram. Establish the ambition before teaching the method.

**2. “a better model still needs your decisions.”**

Briefly explain what OpenAI documents as different about GPT Image 2.5. Separate those claims from our own experiments, whose backend version was not exposed.

Introduce the central idea: **make the important visual decisions explicit, then inspect whether the image followed them.**

**3. “here’s how i turn an idea into a brief.”**

Use one ambitious scene throughout this section. Build the prompt in visible stages: subject and action, composition, relationships, light and materials, exact text, and requirements to check.

Show the initial request, the clearer brief, and both results. Explain what each added instruction was meant to control. Give the reader a short, copyable template.

**4. “when i have a reference, i map it first.”**

Make visual mapping the centerpiece. Show the original image beside its named parts and selectable crops. Let the reader choose Keep, Change, or Remove and see the resulting instructions.

Follow one concrete choice from selection to generated result. Explain how position, scale, relationships, and text matter alongside the objects themselves.

**5. “save the image’s decisions as reconstruction JSON.”**

Show a readable excerpt beside the corresponding image regions: element names, locations, relationships, appearance, protected features, and uncertain observations.

Then show how the agent compiles those selections into a prompt. **The JSON makes the instructions reusable; it cannot guarantee an exact reconstruction.** Put the full schema in the accompanying skill.

**6. “borrow different things from different references.”**

Use a person, an outfit, and a setting. Label exactly what each reference contributes. Show the combined result and any unwanted borrowing between sources.

Give readers a practical instruction pattern: which source controls which property, what stays fixed, and what they can invent.

**7. “fix the part that is wrong.”**

Explain comments, region selection, sketches, and the visual map through concrete jobs. A comment identifies a local change; a sketch communicates placement; the map carries named choices into later work.

Show a successful repair alongside something else that drifted. Compare one change at a time with bundled changes without claiming either always wins.

**8. “give each agent a different experiment.”**

Keep one shared brief and vary a specific reference combination or composition choice per agent. Compare outputs against the same requirements.

Show the useful alternatives and failed branches. Present parallel exploration as a workflow to test, with its extra generation cost visible.

**9. “what actually helped, and what didn’t.”**

Use a compact findings table covering ordinary language versus jargon, prose versus labeled prompts, references, reconstruction, and sequential edits.

Every finding gets an image, its limitation, and an actionable next step. Keep small-sample observations clearly labeled. Place the relevant comparisons inside earlier sections too.

**10. “give the whole process to your agent.”**

Finish with one copyable instruction and the downloadable skill. The loop is: describe or attach → map → choose → generate → inspect → revise.

Keep all 24 guide adaptations and their exact prompts in the linked visual catalog. Use selected examples to carry the main story.

Closing line: *save the decisions. the next image starts there.*

Single CTA: **give the skill to your agent, attach a reference, and ask it to map the image before generating.**

Template: personal-frustration hook → illustrated how-to → reusable artifact.
