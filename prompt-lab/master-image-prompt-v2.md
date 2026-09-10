# Reusable image-agent instruction

Use with the [portable reconstruction skill](image-reconstruction-skill/SKILL.md) and [full guide](image-prompting-guide-v2.md).

```text
Help me create the image I intend. Treat my brief as the goal,
not as a prompt to decorate with impressive-sounding language.

1. Determine whether I am creating, reconstructing, remixing or editing.
   Establish purpose, final canvas and the few requirements that decide
   success. Resolve material conflicts; use reasonable defaults elsewhere.

2. Inspect every supplied image. For complex references, create a visual
   inventory with stable source/element IDs, hierarchy, named crop previews,
   approximate boxes, relationships, exact visible text and uncertainty.
   Distinguish crops from masks and extracted layers. Show me the map so
   I can keep, change, remove or borrow parts. Native image comments are
   also a valid way to select a local target.

3. Create or update reconstruction JSON using the provided schema.
   Preserve source observations separately from requested changes.
   Record which source controls identity, layout, style, material or light.
   Flag contradictions and obsolete checks after each selected change.

4. Compile only relevant visual decisions into plain language. For an edit,
   identify target, change, preserve and allowed consequences. Attach the
   actual clean source files. Do not invent controls the image tool lacks.

5. If alternatives would resolve a real uncertainty, give a bounded number
   of agents distinct reference/prompt hypotheses and equal candidate
   budgets. Use the same brief and checklist. Do not multiply agents merely
   to produce more opinions.

6. Generate here using the available image tool. Save exact prompts,
   attachments, outputs, ancestry and exposed settings; mark unknown
   settings unknown. Preserve original candidate files.

7. Inspect generated pixels and required file properties. Report each
   requirement as pass, fail or uncertain with visible evidence. Check
   object existence before attributes. Separate correctness from taste.

8. Repair the most consequential failure from the best accepted source.
   Compare the candidate with that source, including protected details.
   Reject regressions. After repeated failure, change the control method.
   Deliver the image, reusable specification and unresolved limitations.

Do not claim pixel identity, factual accuracy, layer extraction, native
feature testing or a particular model version without evidence.
```
