# Prompt library

Original briefs organized around observable decisions: subject, arrangement, medium, typography, local color, grading, lighting, and constraints. Use only the fields relevant to the job. Plain text is sufficient; JSON is for coordinating and checking requirements, not a magic image-quality syntax.

## Tested examples

| Job | Starting prompt | Acceptance brief | Reviewer-generated repair | Result |
| --- | --- | --- | --- | --- |
| Product campaign revision | [Source](../examples/product/source-prompt.txt) | [JSON](../examples/product/brief.json) | [Repair](../examples/product/round-0/repair-prompt.txt) | [Image](../examples/product/candidate-1.png) |
| Diagram feedback loop | [Source](../examples/diagram/source-prompt.txt) | [JSON](../examples/diagram/brief.json) | [Repair](../examples/diagram/round-0/repair-prompt.txt) | [Image](../examples/diagram/candidate-1.png) |

These are controlled revision tests: the unchanged original was deliberately checked against a new edit brief, then repaired. They do not show that the original generation failed its own prompt. Both revisions passed the recorded visual review after one edit; this is not a benchmark or a universal success-rate claim.

## Additional recipes

[Eight complete generation prompts and four targeted edit prompts](recipes.md). These are new, ready-to-adapt prompts; **they have not been image-tested in this repository**. Each has concrete checks so users can test it through Image Loop.

For a new task:

1. Pick a recipe and replace only the details relevant to your job.
2. Invoke `/image-loop` in Claude Code or `$image-loop` in Codex.
3. Convert required details into a brief before generation.
4. Inspect the evidence, not just the final picture.

Use [OpenAI's image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting) for the general principles behind explicit composition, reference roles, and narrow edits. The recipes here use original subjects and layouts; they are not copies of the guide's examples.
