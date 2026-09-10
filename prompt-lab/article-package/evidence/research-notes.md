# Research behind the image prompting guide

Reviewed 10 September 2026. This is a focused literature review, not a systematic review or meta-analysis. Research findings, my practical deductions, and the small live demonstration are different kinds of evidence.

## Official sources

**[GPT Image 2.5 prompting guide](https://developers.openai.com/api/docs/guides/image-prompting)** — opened in the Codex browser with the GPT Image 2.5 tab selected. Read the complete selected guide, including model selection, settings, migration, generation examples, reference roles, editing, sketch rendering, repeated edits, character continuity, and result checks. Visually inspected the river-valley sketch and both renderings. The supplied runnable example remains pinned to GPT Image 2, so it should not be mistaken for a fully migrated 2.5 example. The article adds a reference-analysis worksheet, constraint priorities, operational checks, failure diagnosis, and a portable agent procedure.

**[Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)** — OpenAI, 8 September 2026. Confirms the actual new Sketch feature and its `@Sketch` entry point. The linked [Sketch page](https://chatgpt.com/sketch) resolves to the ChatGPT sketch entry. The browser available for this research was signed out; authenticated drawing controls were not tested. The live experiment uses a locally created sketch as an image input, demonstrating sketch-to-render behavior without claiming to test the authenticated Sketch UI.

**[Image generation API documentation](https://developers.openai.com/api/docs/guides/image-generation)** — checked its stated limitations. Precise text placement, recurring identity, and layout control can still fail. The article distinguishes API options from words inside a prompt and does not claim that built-in image generation exposes every API control.

## Papers and what they actually establish

### 1. Better captions

Betker et al., **[Improving Image Generation with Better Captions](https://cdn.openai.com/papers/dall-e-3.pdf)**, 2023. Read dataset recaptioning, evaluation design, caption-type comparisons, prompt upsampling, and limitations (§§2–5).

**Finding:** training on descriptive synthetic captions improved prompt following in the tested models; the paper also explores expanding short prompts with a language model.

**Practical deduction:** useful detail describes visible content and resolves ambiguity. Expansion can help when it preserves the intended image.

**Boundary:** training evidence does not establish a universal ideal prompt length. The paper reports remaining spatial, text, and species-specific failures. Its results concern DALL-E 3 and experimental models, not GPT Image 2.5.

### 2. Object-level evaluation

Ghosh, Hajishirzi and Schmidt, **[GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment](https://arxiv.org/abs/2310.11513)**, 2023. Read framework, human alignment, failure analysis and limitations (§§3–6).

**Finding:** object presence, count, position and color provide more specific diagnostics than a single global similarity measure.

**Practical deduction:** check each requirement independently before deciding whether the result works.

**Boundary:** detectors have restricted categories and can fail on stylized art or details such as fingers. A detector score is not ground truth, and the original paper's model rankings are historical.

### 3. Compositional binding

Huang et al., **[T2I-CompBench](https://arxiv.org/abs/2307.06350v1)**, 2023. Read the original v1 PDF, especially categories, metrics, reward-selected training and limitations (§§3–7; appendix E). Later versions of this arXiv record have a different, expanded title.

**Finding:** the benchmark separates color, shape and texture binding from spatial and other relationships, exposing errors hidden by attractive output.

**Practical deduction:** attach each attribute to its object and write relationships explicitly: “the yellow chair is left of the blue table.”

**Boundary:** the paper does not prove that this sentence format fixes those errors. Its GORS improvement involves model training, not a phrase readers can paste into ChatGPT.

### 4. Sketches and spatial conditions

Zhang, Rao and Agrawala, **[Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543)**, ICCV 2023. Read architecture, training/inference, sketch experiments and comparisons (§§3–4).

**Finding:** ControlNet adds trained spatial conditioning, including edges, poses, depth and sketches, to a pretrained diffusion model.

**Practical deduction:** send visual structure as an image when its geometry is difficult to convey in words.

**Boundary:** uploading a drawing to ChatGPT is not invoking ControlNet. This paper supports the general value of visual conditions; it does not reveal OpenAI Sketch's internal implementation or guarantee exact geometry.

### 5. Preserving structure during edits

Hertz et al., **[Prompt-to-Prompt Image Editing with Cross Attention Control](https://arxiv.org/abs/2208.01626)**, 2022. Read cross-attention manipulation, applications and limitations (§§3–5).

**Finding:** in the tested diffusion systems, manipulating attention can retain aspects of a source composition during text-directed edits. Merely changing a generation prompt can otherwise change the scene substantially.

**Practical deduction:** when most of an image is right, work from that image and specify the change and the elements to preserve.

**Boundary:** the research method requires internal access and controlled randomness. Writing “Prompt-to-Prompt” in a hosted model's prompt does not activate it. Inversion and local precision remain limitations.

### 6. Missing subjects

Chefer et al., **[Attend-and-Excite](https://arxiv.org/abs/2301.13826)**, SIGGRAPH 2023. Read inference intervention, comparisons, metrics and limitations (§§4–6).

**Finding:** Stable Diffusion can omit requested subjects or misassign attributes. Their attention intervention improves subject coverage in the studied setting.

**Practical deduction:** check the least obvious requested object, not just the dominant subject. A beautiful foreground can conceal a missing requirement.

**Boundary:** this is an inference algorithm, not evidence that repeating a noun or adding capital letters produces the same improvement. Generalization is limited by the underlying generator.

### 7. Prompt adaptation

Hao et al., **[Optimizing Prompts for Text-to-Image Generation](https://arxiv.org/abs/2212.09611)**, first posted 2022; reviewed revised text dated 2023. Read Promptist's supervised training, reward definition, experiments and human evaluation (§§2–3).

**Finding:** a learned prompt adapter can improve tested Stable Diffusion results using relevance and aesthetic rewards. Effective modifiers can depend on the generator.

**Practical deduction:** transfer the user's requirements between models, then test model-specific wording; avoid treating a popular suffix as a universal instruction.

**Boundary:** aesthetic rewards only approximate a person's goal. The study does not validate its optimized strings on GPT Image 2.5.

### 8. Dependency-aware checking

Cho et al., **[Davidsonian Scene Graph](https://arxiv.org/abs/2310.18235)**, first posted 2023, ICLR 2024. Read question generation, dependencies, VQA evaluation and conclusions (§§3–5).

**Finding:** distinct, atomic questions and dependency relationships reduce several problems in automatic text-image evaluation. Judges still disagree with people, particularly on some subjective or difficult details.

**Practical deduction:** establish that an object exists before checking its properties; distinguish failure from uncertainty and avoid double-counting the same fact.

**Boundary:** an agent's checklist is inspired by this work, not an implementation of the published evaluator. Critical details still need direct inspection or a suitable deterministic check.

### 9. Evaluation can become stale

Kamath et al., **[GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation](https://arxiv.org/abs/2512.16853)**, 2025. Read benchmark audit, updated composition tests, Soft-TIFA and evaluation drift (§§3–6).

**Finding:** older automated judgments diverged from human judgments on newer generators. The paper proposes a harder benchmark and an updated evaluator, while warning that neither is permanently immune to drift.

**Practical deduction:** record model and settings, inspect real outputs and periodically check whether your evaluator still measures what matters.

**Boundary:** neither a historical leaderboard nor a single model's self-rating proves success for a new workflow. This paper predates GPT Image 2.5.

## Synthesis and evidence limits

The article's visual worksheet, priority order, repair budget and master prompt are my synthesis. They are intended to make decisions explicit and revisions testable. They are not a published universal algorithm, a discovered OpenAI internal architecture, or a guarantee of reproducing every possible image.

The live demonstration tests a small product scene, reference reconstruction, a room sketch, and a localized edit. It cannot establish performance on arbitrary people, places, scientific facts, fine typography, cultural details, or all models. A wider validation set would need repeated generations, independent reviewers, varied subject matter and reported failure rates.
