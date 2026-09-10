#!/usr/bin/env python3
"""Validate this package's JSON contract and compile it; no renderer or dependencies.

The small schema walker implements exactly the keywords used in the bundled schema.
It is not a general JSON Schema implementation. Semantic checks add bounds, evidence,
ID integrity, reference use, hierarchy, dependency and edit-lock validation.
"""

import argparse
import copy
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "references" / "reconstruction.schema.json"


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def object_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    def invalid_number(value):
        raise Invalid(f"Non-finite JSON number: {value}")
    return json.loads(Path(path).read_text(encoding="utf-8"),
                      object_pairs_hook=object_no_duplicates,
                      parse_constant=invalid_number)


def type_matches(value, kind):
    return {
        "object": isinstance(value, dict), "array": isinstance(value, list),
        "string": isinstance(value, str), "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "null": value is None,
    }[kind]


def schema_check(value, rule, root, path="$"):
    if "$ref" in rule:
        ref = root
        for part in rule["$ref"].removeprefix("#/").split("/"):
            ref = ref[part.replace("~1", "/").replace("~0", "~")]
        return schema_check(value, ref, root, path)
    if "type" in rule:
        kinds = rule["type"] if isinstance(rule["type"], list) else [rule["type"]]
        require(any(type_matches(value, kind) for kind in kinds), f"{path}: expected {kinds}")
    if "const" in rule:
        require(type(value) is type(rule["const"]) and value == rule["const"],
                f"{path}: expected constant {rule['const']!r}")
    if "enum" in rule:
        require(any(type(value) is type(item) and value == item for item in rule["enum"]),
                f"{path}: unsupported value {value!r}")
    if isinstance(value, dict):
        for key in rule.get("required", []):
            require(key in value, f"{path}: missing {key}")
        for key, item in value.items():
            child = rule.get("properties", {}).get(key)
            if child is None:
                extra = rule.get("additionalProperties", True)
                require(extra is not False, f"{path}: unexpected property {key}")
                child = extra if isinstance(extra, dict) else {}
            schema_check(item, child, root, f"{path}.{key}")
    elif isinstance(value, list):
        require(len(value) >= rule.get("minItems", 0), f"{path}: too few items")
        require(len(value) <= rule.get("maxItems", math.inf), f"{path}: too many items")
        if rule.get("uniqueItems"):
            serial = [json.dumps(item, sort_keys=True) for item in value]
            require(len(set(serial)) == len(serial), f"{path}: duplicate items")
        for index, item in enumerate(value):
            schema_check(item, rule.get("items", {}), root, f"{path}[{index}]")
    elif isinstance(value, str):
        require(len(value) >= rule.get("minLength", 0), f"{path}: string too short")
        if "pattern" in rule:
            require(re.search(rule["pattern"], value), f"{path}: wrong ID format")
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        require(math.isfinite(value), f"{path}: number must be finite")
        require(value >= rule.get("minimum", -math.inf), f"{path}: below minimum")
        require(value <= rule.get("maximum", math.inf), f"{path}: above maximum")
        require(value > rule.get("exclusiveMinimum", -math.inf), f"{path}: must be greater than minimum")


def unique_index(items, label):
    result = {}
    for item in items:
        require(item["id"] not in result, f"Duplicate {label} ID: {item['id']}")
        result[item["id"]] = item
    return result


def check_box(box, label, basis=None):
    if box is None:
        if basis is not None:
            require(basis == "unknown", f"{label}: null box needs unknown geometry_basis")
        return
    x, y, width, height = box
    require(width > 0 and height > 0, f"{label}: width and height must be positive")
    require(x + width <= 1 + 1e-9 and y + height <= 1 + 1e-9,
            f"{label}: box extends beyond the canvas")
    if basis is not None:
        require(basis != "unknown", f"{label}: known box needs an evidence basis")


def check_evidence(item, label, synthetic=False):
    unknown = item["status"] == "unknown"
    require((item["value"] is None) == unknown, f"{label}: only unknown evidence has null value")
    require((item["basis"] == "unknown") == unknown, f"{label}: unknown basis/status disagree")
    require((item["confidence"] == "unknown") == unknown, f"{label}: unknown confidence/status disagree")
    if unknown:
        require(bool(item["note"].strip()), f"{label}: explain the unknown")
    if synthetic:
        require(item["basis"] not in ("file_metadata", "pixel_measurement"),
                f"{label}: synthetic example cannot claim file or pixel measurement")


def ancestors(node_id, nodes):
    seen = {node_id}
    parent = nodes[node_id]["parent_id"]
    while parent is not None:
        require(parent not in seen, f"Group cycle involving {node_id}")
        seen.add(parent)
        yield parent
        parent = nodes[parent]["parent_id"]


def property_overlap(first, second):
    return first == "*" or second == "*" or first == second or first.startswith(second + ".") or second.startswith(first + ".")


def effects(selection):
    action = selection["action"]
    if action == "remove":
        return ["*"]
    if action == "replace":
        return ["description", "appearance", "text", "count"]
    if action == "move":
        return ["bbox"]
    return selection["properties"] if action == "restyle" else []


def review_flags_for(spec):
    """Conservative dependency review, not a natural-language contradiction solver."""
    nodes = {node["id"]: node for node in spec["groups"] + spec["elements"]}
    edits = [selection for selection in spec["selections"] if selection["action"] != "keep"]
    affected = set()
    for selection in edits:
        target = selection["target_id"]
        for node in nodes.values():
            if node["id"] == target or target in ancestors(node["id"], nodes):
                affected.update([node["id"], node["source_id"], *ancestors(node["id"], nodes)])
    flags = {"revision": spec["revision"],
             "scene_fields": [key for key, value in spec["scene"].items() if edits and value["status"] != "unknown"],
             "invariant_ids": [item["id"] for item in spec["invariants"] if edits and (not item["target_ids"] or affected.intersection(item["target_ids"]))],
             "criterion_ids": [item["id"] for item in spec["criteria"]["hard"] + spec["criteria"]["soft"] if edits and (not item["target_ids"] or affected.intersection(item["target_ids"]))],
             "notes": []}
    if edits:
        flags["notes"] = [
            "Selected edits supersede conflicting source observations. The flagged global source cues, invariants and checks remain baseline evidence, not current rendering commands.",
            "The compiler omits potentially affected baseline prose and source descriptions of changed elements. It adds the explicit delta and preserves unselected content instead.",
            "Reconcile flagged checks with the selected edits before scoring them. These flags indicate potential overlap, not a proved contradiction or a passed check."]
    return flags


def validate(spec):
    schema = read_json(SCHEMA_PATH)
    schema_check(spec, schema, schema)
    synthetic = spec["provenance"]["kind"] == "synthetic_example"
    sources = unique_index(spec["source_images"], "source")
    groups = unique_index(spec["groups"], "group")
    elements = unique_index(spec["elements"], "element")
    require(not (set(groups) & set(elements)), "Group and element IDs must be distinct")
    nodes = {**groups, **elements}
    known = set(sources) | set(nodes)
    require(len([s for s in sources.values() if s["role"] == "target"]) <= 1,
            "Use one target canvas; assign other images reference or analysis roles")
    if spec["intent"]["task"] in ("reconstruct", "edit", "remix"):
        require(any(s["role"] == "target" for s in sources.values()),
                "Reconstruction/edit/remix needs a target source (a planned canvas may have path null)")
    output = spec["intent"]["output"]
    require((output["width_px"] is None) == (output["height_px"] is None),
            "Output dimensions must both be known or both null")
    for source in sources.values():
        known_size = source["width_px"] is not None and source["height_px"] is not None
        require((source["width_px"] is None) == (source["height_px"] is None),
                f"{source['id']}: source dimensions must both be known or both null")
        require(known_size == (source["dimensions_basis"] != "unknown"),
                f"{source['id']}: dimensions and evidence basis disagree")
        if source["selected_for_use"]:
            require(source["allowed_roles"], f"{source['id']}: selected reference needs allowed_roles")
        if synthetic:
            require(source["dimensions_basis"] != "file_metadata",
                    f"{source['id']}: synthetic example cannot claim measured dimensions")
    for key, value in spec["scene"].items():
        check_evidence(value, f"scene.{key}", synthetic)
    for region in spec["coverage"]["excluded_regions"]:
        require(region["source_id"] in sources, "Excluded region uses an unknown source")
        check_box(region["bbox"], "excluded region")
    for node in nodes.values():
        label = node["id"]
        require(node["source_id"] in sources, f"{label}: unknown source_id")
        require(label.startswith(node["source_id"] + "-"), f"{label}: ID prefix must match source_id")
        check_box(node["bbox"], label, node["geometry_basis"])
        if synthetic:
            require(node["geometry_basis"] != "pixel_measurement", f"{label}: synthetic bounds are not measured")
        parent = node["parent_id"]
        if parent is not None:
            require(parent in groups, f"{label}: parent_id must point to an existing group")
            require(groups[parent]["source_id"] == node["source_id"], f"{label}: parent is in another source")
    for node_id in nodes:
        list(ancestors(node_id, nodes))
    for element in elements.values():
        label = element["id"]
        check_evidence(element["description"], f"{label}.description", synthetic)
        for key, value in element["appearance"].items():
            check_evidence(value, f"{label}.appearance.{key}", synthetic)
        if element["kind"] == "text":
            require(element["text"] is not None, f"{label}: text element needs a transcript or explicit uncertainty")
        if element["text"] is not None:
            text = element["text"]
            if text["certainty"] == "exact":
                require(isinstance(text["transcript"], str) and bool(text["transcript"]), f"{label}: exact text cannot be null/empty")
                require(not text["uncertain_spans"], f"{label}: exact text cannot contain uncertain spans")
            else:
                require(text["uncertain_spans"], f"{label}: say which text is uncertain")
        occ = element["occlusion"]
        require((occ["boundary"] == "complete") == (occ["hidden_content"] == "not_applicable"),
                f"{label}: incomplete/uncertain boundaries require unknown hidden content")
        if occ["boundary"] == "complete":
            require(not occ["occluded_by"], f"{label}: complete element cannot have occluders")
        for other in occ["occluded_by"]:
            require(other in elements and other != label, f"{label}: invalid occluder {other}")
            require(elements[other]["source_id"] == element["source_id"], f"{label}: occluder belongs to another image")
        asset = element["asset"]
        require((asset["path"] is None) == (asset["kind"] == "none"), f"{label}: asset kind/path disagree")
        if asset["kind"] == "segmented_layer":
            require(asset["alpha_verified"], f"{label}: segmented layer requires verified transparency")
        if asset["kind"] == "none":
            require(not asset["alpha_verified"], f"{label}: no asset cannot have verified alpha")
        for prop in element["editable_properties"] + element["locked_properties"]:
            require(prop in ("*", "description", "count", "text", "bbox", "appearance") or prop.startswith("appearance."),
                    f"{label}: unsupported property path {prop}")
    unique_index(spec["relations"], "relation")
    for relation in spec["relations"]:
        first, second = relation["from_id"], relation["to_id"]
        require(first in nodes and second in nodes and first != second, f"{relation['id']}: invalid relationship endpoints")
        require(nodes[first]["source_id"] == nodes[second]["source_id"], f"{relation['id']}: relationship must describe one source image")
        require((relation["status"] == "unknown") == (relation["confidence"] == "unknown"),
                f"{relation['id']}: unknown relation status/confidence disagree")
    for unknown in spec["unknowns"]:
        require(unknown["target_id"] in known, f"Unknown record references missing target {unknown['target_id']}")
    unique_index(spec["invariants"], "invariant")
    for invariant in spec["invariants"]:
        require(set(invariant["target_ids"]) <= known, f"{invariant['id']}: unknown invariant target")
    criteria = unique_index(spec["criteria"]["hard"] + spec["criteria"]["soft"], "criterion")
    for criterion in criteria.values():
        require(set(criterion["target_ids"]) <= known, f"{criterion['id']}: unknown criterion target")
        require(set(criterion["depends_on"]) <= set(criteria), f"{criterion['id']}: unknown dependency")
    hard_ids = {criterion["id"] for criterion in spec["criteria"]["hard"]}
    for criterion in spec["criteria"]["hard"]:
        require(set(criterion["depends_on"]) <= hard_ids,
                f"{criterion['id']}: hard requirements cannot depend on soft preference scores")
    def check_dependencies(current, trail):
        require(current not in trail, f"Criterion dependency cycle involving {current}")
        for dep in criteria[current]["depends_on"]:
            check_dependencies(dep, trail | {current})
    for criterion_id in criteria:
        check_dependencies(criterion_id, set())
    selected = {}
    for selection in spec["selections"]:
        target, action = selection["target_id"], selection["action"]
        require(target in nodes, f"Selection target does not exist: {target}")
        require(sources[nodes[target]["source_id"]]["role"] == "target",
                f"{target}: apply edits to the target canvas, not a reference inventory")
        prior = selected.setdefault(target, [])
        require(action not in [s["action"] for s in prior], f"{target}: duplicate {action} action")
        prior.append(selection)
        if action in ("replace", "restyle", "move"):
            require(selection["instruction"].strip(), f"{target}: {action} needs an instruction")
        if action == "restyle":
            require(selection["properties"], f"{target}: name the properties to restyle")
        for prop in selection["properties"]:
            require(prop in ("description", "count", "text", "appearance", "bbox") or prop.startswith("appearance."),
                    f"{target}: unsupported selected property {prop}")
        require((selection["destination_bbox"] is not None) == (action == "move"),
                f"{target}: only move has destination_bbox; move requires it")
        check_box(selection["destination_bbox"], f"{target} destination")
        if action == "move" and target in groups:
            require(groups[target]["bbox"] is not None, f"{target}: group move needs original bounds")
        if action == "restyle":
            require("bbox" not in selection["properties"], f"{target}: use move for bounding-box changes")
        for reference in selection["reference_ids"]:
            require(reference in sources and sources[reference]["selected_for_use"],
                    f"{target}: reference {reference} is missing or not selected for use")
        preserve_terms = {item.strip().casefold() for item in selection["preserve"]}
        allow_terms = {item.strip().casefold() for item in selection["allow"]}
        require(not (preserve_terms & allow_terms), f"{target}: the same detail cannot be both preserved and allowed to change")
        for prop in effects(selection):
            require(not any(property_overlap(prop, term) for term in preserve_terms if term in ("*", "description", "count", "text", "bbox", "appearance") or term.startswith("appearance.")),
                    f"{target}: selected change conflicts with an explicit preserved property")
        affected = [node for node in elements.values() if node["id"] == target or target in ancestors(node["id"], nodes)]
        for node in affected:
            if action == "move" and target in groups and node["bbox"] is not None:
                x, y, width, height = node["bbox"]
                gx, gy, gw, gh = groups[target]["bbox"]
                require(x >= gx - 1e-9 and y >= gy - 1e-9 and x + width <= gx + gw + 1e-9 and y + height <= gy + gh + 1e-9,
                        f"{target}: moving a group requires its bounds to enclose child {node['id']}")
            for prop in effects(selection):
                require(not any(property_overlap(prop, lock) for lock in node["locked_properties"]),
                        f"{target}: {action} conflicts with a locked property on {node['id']}")
    for target, actions in selected.items():
        kinds = {selection["action"] for selection in actions}
        require(not ("keep" in kinds and len(kinds) > 1), f"{target}: keep conflicts with another action")
        require(not ("remove" in kinds and len(kinds) > 1), f"{target}: remove conflicts with another action")
        require(not ("replace" in kinds and "restyle" in kinds), f"{target}: put the replacement appearance in one replace instruction")
        for parent in ancestors(target, nodes):
            parent_kinds = {s["action"] for s in selected.get(parent, [])}
            require(not (parent_kinds & {"remove", "replace", "keep"}),
                    f"{target}: child action conflicts with {parent}'s group action")
            require(not ("move" in kinds and "move" in parent_kinds),
                    f"{target}: move either the group or this child in one revision")
    if "review_flags" in spec:
        require(spec["review_flags"] == review_flags_for(spec),
                "Review flags are stale; regenerate them from current selections and revision")
    return spec


def compile_spec(spec, mode="full"):
    validate(spec)
    review = review_flags_for(spec)
    has_edits = any(selection["action"] != "keep" for selection in spec["selections"])
    sources = {source["id"]: source for source in spec["source_images"]}
    nodes = {node["id"]: node for node in spec["groups"] + spec["elements"]}
    by_target = {}
    for selection in spec["selections"]:
        by_target.setdefault(selection["target_id"], []).append(selection)
    target_ids = {s["id"] for s in sources.values() if s["role"] == "target"}
    desired = [element for element in spec["elements"] if element["source_id"] in target_ids]
    warnings = []
    if spec["provenance"]["kind"] == "synthetic_example":
        warnings.append("Synthetic example; no source image was analyzed and no reconstruction fidelity has been tested.")
    if spec["intent"]["exactness"] in ("geometry", "pixel"):
        warnings.append("Strict geometry/pixels require an appropriate deterministic tool and measured comparison; prose and normalized boxes do not enforce them.")
    if spec["coverage"]["status"] == "partial":
        warnings.append("The visible inventory is partial; review its declared exclusions before claiming completeness.")
    if not spec["criteria"]["hard"]:
        warnings.append("No hard result checks are defined; add them before claiming the intended image was achieved.")
    attachments = [source for source in spec["source_images"] if source["selected_for_use"]]
    for source in attachments:
        if source["path"] is None:
            warnings.append(f"Source {source['id']} is selected but has no attachment path; supply the actual image before a reference-based run.")

    def actions_for(node_id):
        ids = list(reversed(list(ancestors(node_id, nodes)))) + [node_id]
        return [selection for ident in ids for selection in by_target.get(ident, [])]

    def suppressed(node_id):
        return any(action["action"] in ("remove", "replace") for action in actions_for(node_id))

    def current_box(node):
        box = node["bbox"]
        move = next((action for action in actions_for(node["id"]) if action["action"] == "move"), None)
        if move is None:
            return box
        if move["target_id"] == node["id"] or box is None:
            return move["destination_bbox"] if move["target_id"] == node["id"] else box
        origin = nodes[move["target_id"]]["bbox"]
        destination = move["destination_bbox"]
        x, y, width, height = box
        ox, oy, ow, oh = origin
        dx, dy, dw, dh = destination
        return [dx + (x-ox)*dw/ow, dy + (y-oy)*dh/oh, width*dw/ow, height*dh/oh]

    def box_phrase(box):
        if box is None:
            return "position unspecified"
        return "approximate normalized box [" + ", ".join(f"{math.floor(number * 1000 + 0.5) / 1000:.3f}" for number in box) + "]"

    def name(node_id):
        return f"{nodes[node_id]['name']} ({node_id})"

    intent = spec["intent"]
    opening = "Create an edited version of the target scene by applying only the selected changes below. Preserve unselected content and properties." if has_edits else f"Create the following {intent['task']} image: {intent['purpose']}"
    lines = [opening,
             "The IDs below identify scene parts; do not print IDs, map badges, crop boxes or review annotations in the artwork."]
    output = intent["output"]
    if output["width_px"] and output["height_px"]:
        divisor = math.gcd(output["width_px"], output["height_px"])
        lines.append(f"Canvas aspect ratio {output['width_px']//divisor}:{output['height_px']//divisor}; crop policy: {output['crop_policy']}.")
    lines.append(f"Match goal: {intent['exactness']}. {intent['exactness_note']}")
    if attachments:
        lines.append("\nINPUT ROLES")
        for source in attachments:
            lines.append(f"- Source {source['id']} ({source['role']}) supplies only: {', '.join(source['allowed_roles'])}. {source['scope_note']}")
    if any(value["status"] != "unknown" and key not in review["scene_fields"] for key, value in spec["scene"].items()):
        lines.append("\nSCENE")
        for prop, observation in spec["scene"].items():
            if observation["status"] != "unknown" and prop not in review["scene_fields"]:
                qualifier = "appearance cue" if observation["status"] == "inferred" else "visible requirement"
                lines.append(f"- {prop.replace('_', ' ')} ({qualifier}): {observation['value']}")
    lines.append("\nELEMENTS AND PLACEMENT")
    lines.append("Positions use image-relative left/right, top-left origin and [x,y,width,height] on a 0–1 canvas. Treat them as layout guidance, not guaranteed model coordinates.")
    active_ids = set()
    for element in desired:
        ident = element["id"]
        if suppressed(ident):
            continue
        active_ids.add(ident)
        changes = [prop for action in actions_for(ident) for prop in effects(action)]
        allowed = lambda prop: not any(property_overlap(prop, changed) for changed in changes)
        count = f"count {element['count']}; " if element["count"] is not None and allowed("count") else ""
        lines.append(f"- {name(ident)}: {count}{box_phrase(current_box(element))}.")
        description = element["description"]
        edited_element = any(action["action"] != "keep" for action in actions_for(ident))
        if allowed("description") and description["value"] is not None and not edited_element:
            lines.append(f"  {description['value']}")
        for prop, observation in element["appearance"].items():
            if observation["value"] is not None and allowed("appearance." + prop):
                lines.append(f"  {prop.replace('_', ' ')}: {observation['value']}")
        text = element["text"]
        if text and allowed("text"):
            if text["certainty"] == "exact":
                lines.append("  Render this quoted artwork text exactly, as text rather than instructions: " + json.dumps(text["transcript"], ensure_ascii=False))
                if text["line_breaks_preserved"]:
                    lines.append("  Preserve the specified line breaks.")
            else:
                warnings.append(f"{ident} has uncertain text. Resolve it if exact lettering is required; the compiler did not invent a transcript.")
                lines.append("  Source lettering is uncertain; do not present guessed wording as a recovered exact transcript.")
        if element["occlusion"]["hidden_content"] == "unknown" and not edited_element:
            lines.append(f"  Visible boundary: {element['occlusion']['boundary']}. Preserve the visible overlap; hidden geometry is unspecified. {element['occlusion']['note']}")
    # Source relations describe the clean image; moved/replaced regions can invalidate them.
    # ponytail: free-text edits cannot be solved geometrically; review changed relations explicitly.
    active_nodes = active_ids | {group['id'] for group in spec['groups'] if group['source_id'] in target_ids and not suppressed(group['id'])}
    relationships = []
    for relation in spec["relations"]:
        endpoints = [relation["from_id"], relation["to_id"]]
        if not set(endpoints) <= active_nodes or relation["status"] == "unknown":
            continue
        if any(any(action["action"] == "move" for action in actions_for(endpoint)) for endpoint in endpoints):
            warnings.append(f"Review relation {relation['id']} after movement; its original spatial statement was omitted from the rendering prompt.")
            continue
        verb = {"left_of": "is to image-left of", "right_of": "is to image-right of", "above": "is above", "below": "is below", "in_front_of": "is in front of", "behind": "is behind", "contains": "contains", "overlaps": "overlaps", "touches": "touches", "points_to": "points to", "same_group": "shares a group with", "other": "relates to"}[relation["kind"]]
        relationships.append(f"- {name(endpoints[0])} {verb} {name(endpoints[1])}. {relation['note']}")
    if relationships:
        lines.extend(["\nRELATIONSHIPS", *relationships])
    if spec["selections"]:
        lines.append("\nREQUESTED CHANGES")
        for selection in spec["selections"]:
            target = selection["target_id"]
            node = nodes[target]
            action = selection["action"]
            where = selection["destination_bbox"] if action == "move" else node["bbox"]
            lines.append(f"- {action.upper()} {name(target)} ({box_phrase(where)}). {selection['instruction']}")
            if action == "replace":
                lines.append("  Replace the original content and appearance described by this target; the source inventory is a locator, not an additional object to render.")
            if action == "move":
                warnings.append(f"Review retained descriptions of {target} and its children for old positional language; source facts remain unchanged in the JSON.")
            if action == "remove":
                lines.append("  Remove this target and its grouped children; continue the surrounding scene coherently.")
            if selection["properties"]:
                lines.append("  Change only these properties: " + ", ".join(selection["properties"]) + ".")
            if selection["reference_ids"]:
                lines.append("  Use selected sources " + ", ".join(selection["reference_ids"]) + " only for their assigned roles.")
            for label, key in (("Preserve", "preserve"), ("Allow", "allow")):
                if selection[key]:
                    lines.append(f"  {label}: " + "; ".join(selection[key]) + ".")
    locked = [element for element in desired if element["locked_properties"] and not suppressed(element["id"])]
    invariants = [item for item in spec["invariants"] if item["id"] not in review["invariant_ids"]]
    hard = [item for item in spec["criteria"]["hard"] if item["id"] not in review["criterion_ids"]]
    soft = [item for item in spec["criteria"]["soft"] if item["id"] not in review["criterion_ids"]]
    if invariants or locked or has_edits:
        lines.append("\nPRESERVE")
        lines.extend("- " + item["description"] for item in invariants)
        lines.extend(f"- Keep the source properties of {name(element['id'])}: {', '.join(element['locked_properties'])}." for element in locked)
        if has_edits:
            lines.extend(["- Preserve all unselected elements and all unselected properties of edited elements.",
                          "- Preserve counts, exact words and relationships except where a selected edit explicitly changes them."])
    if hard:
        lines.append("\nREQUIRED RESULT")
        lines.extend("- " + criterion["description"] for criterion in hard)
    if soft:
        lines.append("\nPREFERENCES, SUBJECT TO THE REQUIREMENTS ABOVE")
        lines.extend("- " + criterion["description"] for criterion in sorted(soft, key=lambda item: -item["weight"]))
    lines.append("\nDo not reconstruct unknown hidden content or uncertain words as if they were verified facts. Match the visible result and the explicit changes.")
    if spec["unknowns"]:
        warnings.extend(f"Unknown {item['target_id']}.{item['property']}: {item['reason']} ({item['resolution']})." for item in spec["unknowns"])
    warnings.extend(review["notes"])
    if review["criterion_ids"]:
        warnings.append("Baseline checks requiring reconciliation before scoring: " + ", ".join(review["criterion_ids"]) + ".")
    if mode == "edit":
        require(any(source["role"] == "target" for source in attachments),
                "Compact edit mode needs the clean target selected as an actual image input")
        require(any(selection["action"] != "keep" for selection in spec["selections"]),
                "Compact edit mode needs a requested change")
        start = lines.index("\nREQUESTED CHANGES") + 1
        end = next((index for index in range(start, len(lines)) if lines[index].startswith("\n")), len(lines))
        edits = lines[start:end]
        lines = ["Edit the attached clean source image. Apply only the changes below. The source pixels identify the target; inventory IDs and bounding boxes are review aids and must not appear in the artwork.",
                 "Preserve the original canvas, crop, unselected objects, readable text, relationships, geometry, lighting and materials except for explicitly permitted consequences.",
                 "\nINPUT ROLES",
                 *[f"- {source['id']}: {', '.join(source['allowed_roles'])}. {source['scope_note']}" for source in attachments],
                 "\nREQUESTED CHANGES", *edits,
                 "\nAfter editing, inspect each requested difference and every protected detail. Do not claim that “unchanged” is guaranteed by a generative edit."]
    return {"document_id": spec["document_id"], "revision": spec["revision"],
            "rendering_prompt": "\n".join(lines), "attachments": attachments,
            "requested_output": output, "criteria": spec["criteria"], "review_flags": review, "warnings": warnings}


def to_text(compiled):
    parts = ["RENDERING PROMPT", compiled["rendering_prompt"],
             "\nATTACHMENTS AND EXECUTION NOTES — separate from the rendering prompt"]
    for source in compiled["attachments"]:
        parts.append(f"- {source['id']} version {source['version']}: {source['path'] or 'MISSING ATTACHMENT'}; roles: {', '.join(source['allowed_roles'])}")
    if not compiled["attachments"]:
        parts.append("- No image attachments selected. This is a text-only rendering prompt.")
    parts.append("- Requested output: " + json.dumps(compiled["requested_output"]))
    parts.append("- Set only controls supported by the actual image tool. Record model/seed as 'not exposed' if unavailable.")
    parts.extend("- " + warning for warning in compiled["warnings"])
    parts.append("\nEVALUATION CHECKLIST — hard criteria cannot be offset by soft scores")
    for kind in ("hard", "soft"):
        for criterion in compiled["criteria"][kind]:
            weight = f"; weight {criterion['weight']}" if kind == "soft" else "; pass/fail/uncertain"
            dependency = f"; after {', '.join(criterion['depends_on'])}" if criterion["depends_on"] else ""
            review = "; baseline check: reconcile with selected edits before scoring" if criterion["id"] in compiled["review_flags"]["criterion_ids"] else ""
            parts.append(f"- {criterion['id']} ({kind}{weight}{dependency}{review}): {criterion['check']}")
    return "\n".join(parts) + "\n"


def self_check():
    sample = read_json(ROOT / "examples" / "synthetic-scene.json")
    validate(sample)
    rendered = compile_spec(sample)
    assert rendered["rendering_prompt"] and rendered["warnings"]
    cases = []
    def rejects(label, mutate):
        invalid = copy.deepcopy(sample)
        mutate(invalid)
        try:
            validate(invalid)
        except Invalid:
            cases.append(label)
        else:
            raise AssertionError("Invalid input accepted: " + label)
    rejects("out-of-canvas bounds", lambda s: s["elements"][0].update(bbox=[0.9, 0, 0.5, 0.1]))
    rejects("duplicate element IDs", lambda s: s["elements"][1].update(id=s["elements"][0]["id"]))
    rejects("dangling parent", lambda s: s["elements"][0].update(parent_id="A-G99"))
    rejects("group cycle", lambda s: s["groups"][0].update(parent_id=s["groups"][0]["id"]))
    rejects("unknown disguised as fact", lambda s: s["elements"][0]["description"].update(status="unknown"))
    rejects("fabricated synthetic measurement", lambda s: s["source_images"][0].update(dimensions_basis="file_metadata"))
    rejects("hard criterion weight", lambda s: s["criteria"]["hard"][0].update(weight=99))
    rejects("criterion dependency cycle", lambda s: s["criteria"]["hard"][0].update(depends_on=[s["criteria"]["hard"][0]["id"]]))
    rejects("hard requirement depending on aesthetics", lambda s: s["criteria"]["hard"][0].update(depends_on=[s["criteria"]["soft"][0]["id"]]))
    rejects("unselected reference", lambda s: s["selections"][0].update(reference_ids=["A"]))
    rejects("same preserve and allow detail", lambda s: s["selections"][0].update(preserve=["texture"], allow=["texture"]))
    rejects("preserving the changed property", lambda s: s["selections"][1].update(preserve=["appearance.color"]))
    rejects("false transparent layer", lambda s: s["elements"][0]["asset"].update(kind="segmented_layer", path="layer.png", alpha_verified=False))
    rejects("non-finite coordinate", lambda s: s["elements"][0].update(bbox=[0, 0, math.inf, 1]))
    rejects("boolean as dimension", lambda s: s["source_images"][0].update(width_px=True))
    text_node = next(i for i, e in enumerate(sample["elements"]) if e["text"] is not None)
    rejects("null exact transcript", lambda s: s["elements"][text_node]["text"].update(transcript=None))
    mutable = copy.deepcopy(sample)
    mutable["selections"] = []
    first = mutable["elements"][0]
    first["locked_properties"] = ["appearance.color"]
    change = {"target_id": first["id"], "action": "restyle", "properties": ["appearance.color"],
              "instruction": "Make it orange", "destination_bbox": None, "reference_ids": [], "preserve": [], "allow": []}
    mutable["selections"] = [change]
    try:
        validate(mutable)
    except Invalid:
        cases.append("locked-property conflict")
    else:
        raise AssertionError("Locked recolor accepted")
    mutable["elements"][0]["locked_properties"] = []
    mutable["elements"][0]["appearance"]["color"] = {"value": "OLD_COLOR_SENTINEL", "status": "inferred", "basis": "user_supplied", "confidence": "medium", "note": "Synthetic."}
    output = compile_spec(mutable)
    assert "OLD_COLOR_SENTINEL" not in output["rendering_prompt"], "Restyle leaked obsolete source color"
    first_id = first["id"]
    mutable["selections"][0].update(action="remove", properties=[], instruction="")
    removed = compile_spec(mutable)["rendering_prompt"]
    assert "OLD_COLOR_SENTINEL" not in removed, "Removal leaked source appearance"
    assert f"REMOVE {first['name']} ({first_id})" in removed
    mutable["selections"][0].update(action="replace", instruction="A transparent water reservoir")
    replaced = compile_spec(mutable)["rendering_prompt"]
    assert "OLD_COLOR_SENTINEL" not in replaced, "Replacement leaked source appearance"
    assert "A transparent water reservoir" in replaced
    mixed = copy.deepcopy(sample)
    reference = copy.deepcopy(mixed["source_images"][0])
    reference.update(id="B", role="reference", path="palette-reference.png", selected_for_use=True, allowed_roles=["palette"], scope_note="Borrow palette only.")
    mixed["source_images"].append(reference)
    reference_element = copy.deepcopy(mixed["elements"][0])
    reference_element.update(id="B-01", source_id="B", parent_id=None, name="REFERENCE_SUBJECT_SENTINEL")
    mixed["elements"].append(reference_element)
    mixed["selections"][0]["reference_ids"] = ["B"]
    mixed_result = compile_spec(mixed)
    assert [s["id"] for s in mixed_result["attachments"]] == ["B"]
    assert "REFERENCE_SUBJECT_SENTINEL" not in mixed_result["rendering_prompt"], "Palette reference leaked its subject into target inventory"
    moved = copy.deepcopy(sample)
    moved["selections"] = []
    group = moved["groups"][0]
    child = next(e for e in moved["elements"] if e["parent_id"] == group["id"])
    moved["selections"] = [{"target_id": group["id"], "action": "move", "properties": ["bbox"], "instruction": "Move the group together", "destination_bbox": [0, 0.1, 0.47, 0.415], "reference_ids": [], "preserve": ["internal arrangement"], "allow": []}]
    shifted = compile_spec(moved)["rendering_prompt"]
    assert "ribbed glass dome (A-01): count 1; approximate normalized box [0.000, 0.100, 0.470, 0.300]" in shifted, "Group move did not transform child geometry"
    try:
        object_no_duplicates([("same", 1), ("same", 2)])
    except Invalid:
        cases.append("duplicate JSON key")
    else:
        raise AssertionError("Duplicate key accepted")
    real = read_json(ROOT / "examples" / "rain-engine.reconstruction.json")
    prior_palette = real["scene"]["palette"]["value"]
    prior_rule = next(c["description"] for c in real["criteria"]["hard"] if c["id"] == "H07")
    prior_description = next(e["description"]["value"] for e in real["elements"] if e["id"] == "A-48")
    real["selections"] = [{"target_id": "A-48", "action": "restyle", "properties": ["appearance.color"],
                           "instruction": "Make the return arrow deep magenta.", "destination_bbox": None,
                           "reference_ids": [], "preserve": ["route and all other regions"], "allow": []}]
    real["revision"] += 1
    real["review_flags"] = review_flags_for(real)
    updated = compile_spec(real)
    assert all(old not in updated["rendering_prompt"] for old in [prior_palette, prior_rule, prior_description]), "Old color constraints leaked after a selected edit"
    assert "deep magenta" in updated["rendering_prompt"] and "H07" in updated["review_flags"]["criterion_ids"]
    assert real["scene"]["palette"]["value"] == prior_palette, "Source evidence was rewritten"
    assert "deep magenta" in compile_spec(real, mode="edit")["rendering_prompt"]
    real["revision"] += 1
    try:
        validate(real)
    except Invalid:
        cases.append("stale constraint-review flags")
    else:
        raise AssertionError("Stale review flags accepted")
    print(f"PASS: valid examples, {len(cases)} rejection cases, restyle/remove/replace compilation, group movement, palette-only reference isolation, and stale-color constraint regression.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate", help="Validate the bundled contract plus semantic integrity")
    check.add_argument("input")
    compile_parser = sub.add_parser("compile", help="Return prompt, attachments and checks; does not generate an image")
    compile_parser.add_argument("input")
    compile_parser.add_argument("--format", choices=("text", "json"), default="text")
    compile_parser.add_argument("--mode", choices=("full", "edit"), default="full", help="Use edit for a compact selected delta with an actual clean target input")
    compile_parser.add_argument("--output")
    sub.add_parser("self-check", help="Run the bounded dependency-free behavioral check")
    args = parser.parse_args()
    try:
        if args.command == "self-check":
            self_check()
            return
        spec = validate(read_json(args.input))
        if args.command == "validate":
            print(f"VALID: {spec['document_id']} revision {spec['revision']} (structure and semantic integrity; visual claims not verified)")
            return
        compiled = compile_spec(spec, mode=args.mode)
        result = json.dumps(compiled, indent=2, ensure_ascii=False, allow_nan=False) + "\n" if args.format == "json" else to_text(compiled)
        if args.output:
            output = Path(args.output)
            require(output.resolve() != Path(args.input).resolve(), "Output must not overwrite the source JSON")
            if output.exists():
                require(not output.samefile(args.input), "Output must not overwrite the source JSON through a hard link")
            output.write_text(result, encoding="utf-8")
        else:
            sys.stdout.write(result)
    except (Invalid, OSError, json.JSONDecodeError, RecursionError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
