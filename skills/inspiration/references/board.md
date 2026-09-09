# Reference board and planner

Keep the full reverse-engineered inventory separate from the selected generation axes. An ingredient is a property of a named element, not an entire source image. For example, the font appearance of R1's headline and the wording of that headline are different ingredients. Hex colors, font families, and grading settings inferred from appearance are estimates.

`board.json` has these required fields (see the repository's `examples/inspiration/board.json` for a runnable example):

```json
{
  "brief": "An original square poster for a ceramic cup. Text: DAILY.",
  "references": [{"id": "R1", "source": "cup-photo.png"}],
  "axes": {
    "lighting": [{"id": "R1:light", "source_id": "R1", "element": "window light", "description": "Soft side light with a feathered shadow", "confidence": "high"}]
  },
  "fixed": {"lighting": "R1:light"},
  "incompatible": []
}
```

Source paths are relative to the board file unless absolute. Source can also be an inspected URL or a clearly labeled `user-note:` reference. Save access/inspection evidence with the full inventory. Trait IDs are globally unique. Axis names are arbitrary, nonempty property names; prefer the vocabulary in SKILL.md. Confidence is `high`, `medium`, `low`, or `unknown`; unknown traits may be inventoried but cannot participate in generation. An axis containing only unknown traits needs user clarification. A fixed trait must belong to its named axis. Incompatible pairs are lists of two distinct known trait IDs, such as `["R1:flat-medium", "R2:photographic-reflection"]`.

```bash
python skills/inspiration/scripts/combine.py board.json --count 4 --seed 7 --out plan.json
```

The Python standard-library helper validates the board, applies fixed selections and incompatible pairs, and returns unique combinations with source provenance. It evaluates at most 5,000 tuples and keeps a pool of at most 512; greedy Hamming distance spreads selected traits. It never generates images. If the requested count cannot be found, it returns fewer with an explicit note. On large constrained spaces, a shortfall does not prove no other valid combinations exist. Same board, count, and seed produce the same plan. IDs `C001` etc. are local to that plan; prefix them with the round (`r1-C001`) in the run ledger.

The `prompt` output is a starting brief with trait assignments, not a guarantee of aesthetic coherence. Before generation, add exact text, output size, hard checks, and explicit reference roles. Inspect combinations for conflicting lighting, depth, material, or typography requirements not represented in the incompatible list. Mark exclusions and the reason; do not silently change the selected recipe.

For a loop child, copy the selected parent's recipe into a new board, fix liked axes, and offer alternatives on only the one or two axes being explored. Retain source IDs, record `parent_id`, and skip recipes already tried. If the planner returns only the parent or duplicates from earlier rounds, stop or ask for new ingredients; do not spend generation calls on duplicate recipes without a stated reason.

Recommended run files:

```text
run/
  inventory/                  # one map/spec per source, with inspection notes
  board.json
  r1/plan.json
  r1/C001/prompt.txt
  r1/C001/image.png
  r1/C001/review/              # original image-loop brief and review artifacts
  r1/judgment.json
  state.json                  # latest gate inputs, see judging.md
  decision.json
  lineage.json                # child, parent, recipe, changed/fixed traits
  calls.jsonl                 # one entry per generation attempt, including failures
```
