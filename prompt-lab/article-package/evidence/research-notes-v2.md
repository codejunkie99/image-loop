# Research notes for the expanded image-prompting guide

Reviewed 10 September 2026. These notes separate source findings, our practical deductions and the limits of transfer. The article's workflow and reconstruction schema are an authored synthesis, not a published universal prompt algorithm.

## Primary product documentation

- [Current prompting guide, Image 2.5 selected](https://developers.openai.com/api/docs/guides/image-prompting?model=gpt-image-2.5): inventoried all 24 illustrated stages and 65 unique image-asset URLs. The companion inventory preserves headings, links, hashes and settings. The source itself is already structured and detailed; our adaptations are not a fair quality benchmark against it.
- [Images2.5 announcement](https://openai.com/index/introducing-chatgpt-images-2-5/): source for the documented native interfaces and vendor positioning. The article distinguishes those statements from measured experiment outcomes.
- [Image generation API](https://developers.openai.com/api/docs/guides/image-generation): consult for request parameters, dimensions, alpha, quality and current limitations. Our chat tool did not expose all those controls.
- [System card](https://deploymentsafety.openai.com/chatgpt-images-2-5): inspected as product context; its safety evaluations are not scores for our aesthetic or reconstruction quality.

Native image comments and Sketch are documented features. The new experiments use chat image generation and an uploaded drawing; they do not establish execution of the authenticated native comment or drawing toolbar. One earlier Safari annotation request was submitted before the user's interface correction and remains uninspected, so it is excluded from results.

## Earlier paper review retained

The [first-edition research notes](research-notes.md) contain reading scope and limitations for nine primary papers. Their practical contributions remain:

| Source | Contribution to this workflow | Transfer limit |
|---|---|---|
| [Better Captions](https://cdn.openai.com/papers/dall-e-3.pdf) | Communicate useful visual detail and distinguish prompt expansion from empty verbosity. | Training-caption evidence does not imply every longer user prompt is better. |
| [GenEval](https://arxiv.org/abs/2310.11513) | Check objects, counts, position and attributes separately. | Our visual checklist is not its detector-based evaluator. |
| [T2I-CompBench](https://arxiv.org/abs/2307.06350v1) | Treat attribute binding and relationships as distinct failure modes. | Its training/inference improvements are not phrases to paste into a prompt. |
| [ControlNet](https://arxiv.org/abs/2302.05543) | Spatial information can be supplied visually. | A sketch upload is not evidence of ControlNet internals or its exact controls. |
| [Prompt-to-Prompt](https://arxiv.org/abs/2208.01626) | Separate desired edits from structure worth retaining. | Its attention-control method needs model access; a name in a prompt does not activate it. |
| [Attend-and-Excite](https://arxiv.org/abs/2301.13826) | Inspect missing or neglected subjects. | It studies an inference intervention, not noun repetition in hosted models. |
| [Promptist](https://arxiv.org/abs/2212.09611) | Prompt adaptation can depend on the generator and reward. | Optimized modifiers for its tested models are not validated 2.5 suffixes. |
| [Davidsonian Scene Graph](https://arxiv.org/abs/2310.18235) | Ask atomic, dependency-aware questions about a result. | Agent judgments still need calibration and sometimes deterministic checks. |
| [GenEval 2](https://arxiv.org/abs/2512.16853) | Revisit evaluation as generators change. | Old leaderboards and self-ratings do not establish new-workflow performance. |

## Additional research for mapping and agent workflows

### LayoutGPT

[LayoutGPT: Compositional Visual Planning and Generation with Large Language Models](https://arxiv.org/html/2305.15393v2), NeurIPS 2023. Read representation, prompt construction, retrieval of demonstrations, layout-to-image stage and layout-evaluation/ablation sections.

The method predicts categories and bounding boxes in structured layouts, then uses a spatially conditioned generator or 3D assets. This supports separating scene planning from appearance generation. Its CSS-style representation has explicit semantics and demonstrations. It is not evidence that arbitrary JSON coordinates become hard constraints in a hosted image model. The article's normalized rectangles are review/planning aids.

### M3

[M3: High-fidelity Text-to-Image Generation via Multi-Modal, Multi-Agent and Multi-Round Visual Reasoning](https://arxiv.org/html/2602.06166v1), 2026. Read the role pipeline, refinement/escape-hatch mechanism, implementation, results and ablations.

Its verifier compares a proposed edit with the previous best and bounds repeated failures. That informs our accept/reject loop. The authors' improvement claims depend on their tested models, benchmarks and judging process; an imperfect verifier can still accept a regression. The hybrid variant uses different tools and metrics, so “multi-agent” does not describe one fixed intervention.

### Agentic Prompt Enhancer

[APE project and results](https://research.nvidia.com/labs/sil/projects/ape/), 2026. Reviewed the primary project description, single- and multi-agent methods, routing, qualitative examples and result tables. This is a project-page review, not a claim to have obtained a separate full paper.

APE trains prompt enhancers for fixed image backends; its multi-agent route organizes semantic fields. Reported improvements are task- and model-dependent, with mixed entries rather than a universal win. Editing routes can leave simple local instructions unchanged. We borrow the decision to adapt only when useful; we did not reproduce its training or benchmarks.

### WeAgent-MMGenEdit

[WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation and Editing](https://arxiv.org/html/2609.05171v1), 2026 preprint. Read harness, evidence store, toolchain, task/check construction and comparison results.

The system keeps provenance-aware references, inspects candidate pixels, and may render a structured visual carrier before generation. This is relevant to organizing many visual sources and binding facts to layout. Its full recipe includes data, post-training and task-specific evaluation; our simpler JSON/map workflow does not inherit those results. It is recent research, not independent validation of our prototype.

### Further prior art, limited reading

[Talk2Image](https://ojs.aaai.org/index.php/AAAI/article/view/40519), 2026: read the publication metadata and abstract about dialogue-driven multi-agent image generation. This establishes relevant prior art, not a detailed method comparison. We do not include it in the full-paper reading count.

## What is original here and what remains unproven

The 50-element real inventory, selectable interface, conflict-aware reconstruction record, prompt compiler, example briefs and experiment design were built for this guide. Their usefulness is demonstrated through working exports and actual image requests. Novelty, user-effort savings and superiority over native image comments have not been established.

Our comparisons keep some variables controlled but remain small: two samples per vocabulary/formatting condition, one per reference condition, one bundled/sequential pair, and single repair demonstrations. A study of agent-count benefits would need equal total candidate budgets. A model-version study would need exposed and pinned versions/settings. A usability study would need people completing the same tasks through comments and mapping, with time and error measurements.

No source proves a master prompt that reconstructs any image exactly. The useful generalization is a method for supplying evidence, making decisions explicit and checking what the generator actually produced.
