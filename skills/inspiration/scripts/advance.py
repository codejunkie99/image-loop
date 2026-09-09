#!/usr/bin/env python3
"""Gate an agent-orchestrated inspiration round; never generates or judges images."""
import argparse
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decide(state):
    require(isinstance(state, dict), 'State must be an object.')
    require(state.get('mode') in ('batch', 'loop'), 'Invalid mode.')
    require(state.get('judge') in ('human', 'llm', 'hybrid'), 'Invalid judge.')
    for key in ('rounds_completed', 'max_rounds', 'images_used', 'max_images', 'no_improvement_rounds'):
        lower = 0 if key == 'no_improvement_rounds' else 1
        require(type(state.get(key)) is int and state[key] >= lower, f'Invalid {key}.')
    require('judgment' in state, 'judgment is required; use null while awaiting input.')
    candidates = state.get('candidates')
    require(isinstance(candidates, list) and candidates, 'Candidates required.')
    ids, eligible = set(), []
    for c in candidates:
        require(isinstance(c, dict) and isinstance(c.get('id'), str) and c['id'].strip(), 'Invalid candidate.')
        require(c['id'] not in ids, 'Duplicate candidate ID.')
        require(c.get('checks') in ('pass', 'fail', 'uncertain'), 'Invalid checks.')
        ids.add(c['id'])
        if c['checks'] == 'pass':
            eligible.append(c['id'])
    require('incumbent_id' in state, 'incumbent_id is required; null on the first round.')
    incumbent = state['incumbent_id']
    require(incumbent is None or isinstance(incumbent, str) and incumbent in eligible,
            'Incumbent must be an eligible candidate.')
    require(state['rounds_completed'] == 1 or incumbent is not None or not eligible,
            'Later rounds with eligible candidates require the previous eligible incumbent.')
    judgment = state['judgment']
    if judgment is not None:
        require(isinstance(judgment, dict) and judgment.get('by') in ('human', 'llm'), 'Invalid judgment origin.')
        require('improved' in judgment, 'improved is required; null means not established.')
        require(type(judgment.get('stop')) is bool, 'stop must be a boolean.')
        require(judgment.get('improved') is None or type(judgment['improved']) is bool, 'Invalid improved value.')
        for key in ('reason', 'feedback'):
            require(isinstance(judgment.get(key), str), f'Invalid {key}.')
        require(bool(judgment['reason'].strip()), 'Judgment needs evidence or a human reason.')
        if judgment['stop'] and judgment['by'] == 'human':
            return {'action': 'stop_human', 'eligible': eligible}
    if not eligible:
        return {'action': 'stop_no_eligible', 'eligible': []}
    if judgment is None:
        return {'action': 'awaiting_human' if state['judge'] in ('human', 'hybrid') else 'awaiting_llm',
                'eligible': eligible}
    if state['judge'] in ('human', 'hybrid') and judgment['by'] != 'human':
        return {'action': 'awaiting_human', 'eligible': eligible}
    if judgment['stop']:
        return {'action': 'stop_judge', 'eligible': eligible}
    ranking = judgment.get('ranking')
    require(isinstance(ranking, list) and ranking and all(isinstance(x, str) for x in ranking)
            and len(ranking) == len(set(ranking)) and set(ranking) <= set(eligible),
            'Ranking must use unique eligible IDs; failed/uncertain candidates cannot win.')
    require(judgment['by'] == 'human' or set(ranking) == set(eligible),
            'An LLM ranking must cover every eligible ID exactly once.')
    winner = ranking[0]
    if incumbent is not None and judgment['improved'] is not None:
        require((winner != incumbent) == judgment['improved'],
                'Improvement must agree with selection: retain the incumbent when there is no improvement.')
    result = {'winner_id': winner, 'judged_by': judgment['by'], 'eligible': eligible}
    if state['mode'] == 'batch':
        return dict(result, action='complete_batch')
    if state['rounds_completed'] >= state['max_rounds'] or state['images_used'] >= state['max_images']:
        return dict(result, action='stop_budget')
    if state['rounds_completed'] > 1 and judgment['improved'] is None:
        return dict(result, action='stop_uncertain_comparison')
    stalled = 0 if judgment['improved'] is True else state['no_improvement_rounds'] + int(judgment['improved'] is False)
    if stalled >= 2:
        return dict(result, action='stop_no_improvement', no_improvement_rounds=stalled)
    return dict(result, action='iterate', parent_id=winner, no_improvement_rounds=stalled,
                remaining_images=state['max_images'] - state['images_used'],
                remaining_rounds=state['max_rounds'] - state['rounds_completed'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('state', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    try:
        result = decide(json.loads(a.state.read_text()))
        with a.out.open('x') as f:
            json.dump(result, f, indent=2, allow_nan=False)
            f.write('\n')
    except (OSError, ValueError) as exc:
        p.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
