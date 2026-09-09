# Image Loop

**Point at an image. Name the change. Check the result. Repair what failed.**

An agent skill for guided image editing with numbered visual maps, independent vision review, and a bounded repair loop. Includes `/image-loop`, `/image-edit-map`, and `/reverse-engineer` skills, a working reviewer/controller, original prompts, and real before/after examples.

![Workflow diagram after the loop added its feedback arrow](examples/diagram/candidate-1.png)

## Use it

Clone this repository and open it in Claude Code. The committed `.claude/skills/` links expose:

```text
/image-loop Create a product graphic. Check the result and repair failed requirements.
/image-edit-map Number the elements in this image so I can choose what to change.
/reverse-engineer Extract this image's visual design into JSON.
```

Attach the image for editing or reverse engineering. Example edit:

```text
/image-loop Make the bottle and cap blue, replace FIELD with TIDELINE,
and keep the headline, composition, background, and olive accent unchanged.
```

For use outside the repository, install the three skills:

```bash
git clone https://github.com/codejunkie99/image-loop.git
cd image-loop
python3 scripts/install.py --to ~/.claude/skills
# Or, for Codex:
python3 scripts/install.py --to ~/.codex/skills
```

The installer refuses to overwrite existing skills. Review existing files before explicitly using `--replace`. In Codex, invoke `$image-loop`, `$image-edit-map`, or `$reverse-engineer`, or select through `/skills` where supported. Custom `/skill-name` invocation is a [Claude Code feature](https://code.claude.com/docs/en/skills); Codex's [command surface](https://learn.chatgpt.com/docs/developer-commands) differs. A bare custom slash command is not promised on every host.

## What happens

1. The agent resolves the brief and protected details. For an ambiguous image edit, it asks useful questions and creates a separate numbered map.
2. It turns the brief into explicit acceptance criteria and generates or edits an image with the host's image tool.
3. An independent vision reviewer checks the candidate against the criteria and clean source. File checks verify dimensions, format, and transparency requirements.
4. The controller accepts a full pass, creates a targeted repair prompt for concrete failures, or stops on uncertainty, repeated failure, provider errors, or the retry cap.
5. The agent executes a repair when warranted and rechecks the complete brief. It keeps clean sources and evidence for every round.

Default limit: three repairs after the initial candidate. The reviewer cannot quietly rewrite the brief or pass missing criteria. Generation is **agent-orchestrated**: the Python script reviews and decides; it does not itself call an image-generation API.

## Two live revision tests

| Product source | After one repair |
| --- | --- |
| ![Ivory FIELD bottle with headline](examples/product/source.png) | ![Blue TIDELINE bottle with preserved headline](examples/product/candidate-1.png) |

| Test | Initial review against the requested edit | Next review |
| --- | --- | --- |
| Product graphic | Bottle color and brand text failed; three protected criteria passed | All five criteria passed after one repair |
| Workflow diagram | Return arrow and its label failed; three protected criteria passed | All five criteria passed after one repair |

Both resulting PNGs passed decoded 1254×1254 dimension and format checks. The examples deliberately start with an unchanged source and a new revision brief; they do not imply that the original generation failed its original prompt. These two cases are demonstrations, not a reliability benchmark. Preservation was assessed visually, not as pixel identity.

[Read the evidence and limitations](examples/RESULTS.md), including exact briefs, prompts, review JSON, controller decisions, and recorded account usage. The image tool did not expose a selectable generator model identifier in these calls; these are built-in-tool tests, not a verified GPT Image 2.5 model benchmark.

## Prompts and image controls

- [Prompt library](prompts/README.md): tested source/repair prompts plus twelve original, explicitly untested recipes.
- [Image controls](skills/image-edit-map/references/controls.md): text, typography, local color, layers, grading, medium, composition, lighting, and output.
- [Numbered map protocol](skills/image-edit-map/references/mapping-and-prompts.md): stable IDs, sections, separate annotation copies, and clean-source edits.
- [Reverse-engineering contract](skills/image-edit-map/references/reverse-engineer.md): structured JSON with confidence and evidence. Flattened pictures do not reliably reveal exact fonts, original layers, hidden objects, or original grading settings.

## Run the reviewer

Requires Python 3, Pillow, jsonschema, an authenticated Codex CLI, and a reviewer model that accepts images on your configured route.

```bash
uv run --with pillow --with jsonschema python skills/image-loop/scripts/review.py \
  --brief examples/product/brief.json \
  --source examples/product/source.png \
  --candidate examples/product/candidate-1.png \
  --out work/my-review --model gpt-5.6-luna
```

Read `decision.json`. A `repair` outcome includes `repair-prompt.txt`; the host agent uses it with its image tool and reviews the new image. See [reviewer setup](skills/image-loop/references/reviewer.md) for subsequent rounds and provider requirements. The tested route used GPT-5.6 Luna. GPT-5.4 Mini compatibility probes were rejected in this environment; no automatic model fallback is hidden in the script.

The reviewer consumes account usage. A smaller-model reviewer is a cost-control option to evaluate, not proof of savings. Dollar cost was not exposed by these runs. Model mistakes remain possible, particularly in small text and precise spatial relationships.

## Validate locally

```bash
uv run --with pillow --with jsonschema python -m unittest discover -s tests -v
uv run --with jsonschema python skills/image-edit-map/scripts/validate_spec.py \
  skills/image-edit-map/examples/image-spec.example.json
```

Offline tests exercise acceptance, missing/duplicate IDs, uncertainty, protected failures, retry limits, repeated failures, image-file checks, and installer overwrite protection. Live examples exercise real generation, independent review, repair, and review again. Neither establishes human approval or guaranteed correctness.

## Sources and scope

General prompt structure follows the [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting). Reviewer caution follows [OpenAI vision limitations](https://developers.openai.com/api/docs/guides/images-vision#limitations). The numbered interface, explicit contracts, controller, original briefs, and recorded examples are this repository's implementation. This package is not affiliated with or endorsed by OpenAI or Anthropic.

MIT licensed. No credentials or private conversation history are included.
