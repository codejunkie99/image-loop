#!/usr/bin/env python3
"""Plan bounded, diverse visual recipes from a reference board; no image calls."""
import argparse
import json
import math
import random
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(board):
    require(isinstance(board, dict), 'Board must be an object.')
    require(nonempty(board.get('brief')), 'A nonempty brief is required.')
    refs = board.get('references')
    require(isinstance(refs, list) and refs, 'References must be a nonempty list.')
    sources = {}
    for ref in refs:
        require(isinstance(ref, dict) and nonempty(ref.get('id')) and nonempty(ref.get('source')),
                'Each reference needs an id and source.')
        require(ref['id'] not in sources, 'Duplicate reference ID.')
        sources[ref['id']] = ref['source']
    axes = board.get('axes')
    require(isinstance(axes, dict) and 1 <= len(axes) <= 10, 'Use 1 to 10 active axes.')
    traits = {}
    for axis, options in axes.items():
        require(nonempty(axis) and isinstance(options, list) and 1 <= len(options) <= 30,
                'Each named axis needs 1 to 30 traits.')
        for t in options:
            require(isinstance(t, dict) and all(nonempty(t.get(k)) for k in
                    ('id', 'source_id', 'element', 'description')), 'Incomplete trait.')
            require(t['id'] not in traits, 'Duplicate trait ID.')
            require(t['source_id'] in sources, 'Unknown trait source.')
            require(t.get('confidence') in ('high', 'medium', 'low', 'unknown'), 'Invalid confidence.')
            traits[t['id']] = (axis, t)
    fixed = board.get('fixed')
    require(isinstance(fixed, dict), 'fixed must be an object.')
    for axis, tid in fixed.items():
        require(isinstance(tid, str) and tid in traits and traits[tid][0] == axis,
                'Fixed trait must belong to its axis.')
        require(traits[tid][1]['confidence'] != 'unknown', 'Cannot fix an unknown trait.')
    pairs = board.get('incompatible')
    require(isinstance(pairs, list), 'incompatible must be a list.')
    for pair in pairs:
        require(isinstance(pair, list) and len(pair) == 2 and
                all(isinstance(t, str) and t in traits for t in pair) and pair[0] != pair[1],
                'Each incompatible pair needs two distinct known trait IDs.')
    return sources


def plan(board, count=4, seed=7):
    sources = validate(board)
    require(type(count) is int and 1 <= count <= 8, 'count must be 1 to 8.')
    require(type(seed) is int, 'seed must be an integer.')
    names = sorted(board['axes'])
    options = [[t for t in board['axes'][a] if t['confidence'] != 'unknown'
                and (a not in board['fixed'] or t['id'] == board['fixed'][a])] for a in names]
    require(all(options), 'Every active axis needs a known usable trait.')
    total = math.prod(map(len, options))
    rng = random.Random(seed)
    indices = rng.sample(range(total), min(total, 5000))
    pool = []
    evaluated = 0
    for index in indices:
        choice = []
        for opts in options:
            index, remainder = divmod(index, len(opts))
            choice.append(opts[remainder])
        evaluated += 1
        ids = {t['id'] for t in choice}
        if any(set(pair) <= ids for pair in board['incompatible']):
            continue
        pool.append(choice)
        if len(pool) == 512:
            break
    selected = []
    while pool and len(selected) < count:
        def distance(candidate):
            return min((sum(a['id'] != b['id'] for a, b in zip(candidate, other))
                        for other in selected), default=len(names))
        chosen = max(range(len(pool)), key=lambda i: distance(pool[i]))
        selected.append(pool.pop(chosen))
    combinations = []
    for i, choice in enumerate(selected, 1):
        recipe = {a: dict(t, source=sources[t['source_id']]) for a, t in zip(names, choice)}
        assignments = '\n'.join(f"- {a}: {t['description']} (borrow only this property from "
                                f"{t['source_id']}, element {t['element']})." for a, t in recipe.items())
        combinations.append({'id': f'C{i:03d}', 'recipe': recipe,
                             'prompt': board['brief'] + '\nVisual recipe:\n' + assignments})
    return {'seed': seed, 'requested': count, 'space_size': total, 'evaluated': evaluated,
            'combinations': combinations,
            'note': 'Requested count found.' if len(selected) == count else
                    'Fewer valid combinations found in the bounded search; do not duplicate images.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('board', type=Path)
    p.add_argument('--count', type=int, default=4)
    p.add_argument('--seed', type=int, default=7)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    try:
        result = plan(json.loads(a.board.read_text()), a.count, a.seed)
        with a.out.open('x') as f:
            json.dump(result, f, indent=2, allow_nan=False)
            f.write('\n')
    except (OSError, ValueError) as exc:
        p.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
