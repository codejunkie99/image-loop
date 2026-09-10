# A bounded comparison loop with subagents

Use parallel agents when the user or applicable instructions authorize delegation and when independent variants can run alongside useful work. A single agent can run this same protocol sequentially. More agents do not imply more useful evidence: three uncontrolled ideas produce three different pictures, not an isolated test of a technique.

## Freeze the task before searching

Save a source/version manifest, the intended scene, exact text, layout and reference roles. Define observable hard requirements and a small set of soft preferences. Decide the call budget, number of runs per condition, allowed repairs and stopping rule before seeing the candidates. A practical exploratory block can contain two conditions with two runs each and up to two repair calls; the budget is a working choice, not a model law. Respect a smaller user budget.

Keep different questions in different blocks:

| Question | Controlled comparison | What stays the same |
| --- | --- | --- |
| Does simpler language help? | Plain short phrasing versus structured longer phrasing with the same visual facts. | Meaning, references, settings, composition, criterion list and call count. If the long version adds facts, this is an information test, not a language test. |
| Does mapping help reconstruction? | Narrative description versus a prompt compiled from named objects, bounds and relations. | Same source, same target requirements and available reference inputs. Report any extra information the map introduces. |
| Which reference combination helps? | No reference; identity only; layout only; identity plus layout, with roles specified. | Rendering brief, required scene and available settings. Choose a bounded subset when the full combination matrix is expensive. |
| Is one change at a time better? | Two compatible changes in one edit versus the same changes sequentially. | Same clean starting image and final criteria. Report the different call counts and accumulated drift; do not attribute a second call's benefit to wording. |
| What changes with a model version? | Same task and inputs through verified, identified model endpoints or UI modes. | Settings where they are truly supported by both models. If the backend is unexposed, report a tool comparison, not a proven GPT Image 2.5 advantage. |

One-element and one-property edits are different. “Recolor the sofa and preserve fabric” changes one property; “replace the sofa” changes several. A moved object may require a moved shadow. Compatible coupled changes can work together, while independent uncertain changes are easier to diagnose separately. Test the actual claim instead of making “always one at a time” a slogan.

## Divide responsibilities

The coordinator owns the immutable baseline JSON, source IDs, common criteria and run budget. Give each generator a specific condition and a private output name. Instruct it to produce the exact requested variant, record the actual tool call and inspect/save the resulting file. Workers are not alone in the workspace: they must not overwrite shared files or another worker's results.

For a reference-combination search, give each worker an explicit attachment set and role assignment—for example B provides identity, C layout, D material. Record input ordering, and do not reuse an image produced by another condition unless that dependency is the intended treatment. Workers should not alter the common success criteria, silently add references, choose a preferred candidate without disclosing the discarded runs, or claim settings the tool never exposed.

An evaluator receives neutral candidate names, the actual images, the task, clean source where needed and the common rubric. It should not receive labels such as “better prompt,” “advanced method,” predicted winner or a generator's self-rating. A fresh evaluator can be another authorized agent or a separate pass with clean context. Blind the labels where practical; acknowledge that visual characteristics can still reveal the treatment. The evaluator must view the image, not just the prompt or another agent's summary.

If tools do not allow concurrent image calls, serialize generation while agents independently prepare prompts or evaluate completed outputs. If a worker cannot access a reference or the actual image tool, it should return a prepared prompt and a blocker, not a fictional rendered result.

## Record what actually happened

For each attempt keep: neutral ID, condition, full prompt, reference file/version/order/role, clean starting version, actual tool, exposed model/settings/seed, output file and metadata, call count, and result checks. Use `not exposed` rather than guessing. Optional timestamps, cost and latency help compare efficiency when genuinely available. Do not silently discard inconvenient outputs.

Evaluate existence before dependent attributes and relationships. Each hard criterion receives `pass`, `fail`, `uncertain` or `not_evaluated` with visible evidence. `Uncertain` and `not_evaluated` do not count as passes. If a required planter is missing, its leaf color cannot pass. A diagram's aesthetics do not compensate for a wrong arrow direction.

If useful, score each soft preference on a predefined 0–4 scale: 0 absent, 1 poor, 2 partial, 3 good, 4 strong. Compute a weighted mean only among eligible, evaluated preferences. Weights rank preferences; they never soften hard requirements. Report raw criterion checks and the number of hard passes alongside any average. A human aesthetic judgment is still subjective and should be labeled accordingly.

## Diagnose, repair, stop

After the first comparison, identify the largest concrete failure: missing object, incorrect binding, geometry, unreadable text, copied reference content, broken identity, texture drift or export mismatch. Choose a repair that supplies the missing information or control. Keep the failed result in the record and repair from the best accepted clean version.

A successful repair answers whether that intervention helped that candidate. It does not erase the original condition's failure. If you repair only one condition, report the unequal call budget. For a fair technique comparison, either give both the same repair allowance or present initial performance and repair cost separately.

Stop when the hard requirements are met and further calls address no stated need, when the agreed budget is reached, or when the same hard failure recurs without a new control strategy. Deliver unresolved failures candidly. Recommend another method when the job needs exact typography, measured geometry, editable vectors or preserved pixels. Report small experiments as case studies; a single attractive image is not evidence of universal superiority or a measured success rate.

## Reusable worker briefs

**Generator:** “Run condition [neutral ID] from the supplied baseline and references. Keep the semantic brief and success criteria unchanged. Vary only [declared factor]. You own [output paths] and are not alone in this workspace. Generate at most [budget] actual outputs, save every attempt and record exact prompts/inputs/exposed settings. Return concrete file paths and any blockers; do not report the intended image as an observed result.”

**Evaluator:** “Inspect these neutrally named images against the supplied task and criteria. Do not infer which method is expected to win. Mark each hard item pass/fail/uncertain/not_evaluated with visible evidence; check dependent properties only when prerequisites are present. Compare requested changes and preservation separately. Score optional preferences only using the provided rubric. Do not claim pixel equality or backend identity without appropriate evidence.”
