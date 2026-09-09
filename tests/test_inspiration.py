import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'skills/inspiration/scripts'/f'{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


combine = module('combine')
advance = module('advance')


class InspirationTests(unittest.TestCase):
    def setUp(self):
        self.board = json.loads((ROOT/'examples/inspiration/board.json').read_text())
        self.state = dict(mode='loop', judge='llm', rounds_completed=1, max_rounds=3,
                          images_used=2, max_images=8, no_improvement_rounds=0, incumbent_id=None,
                          candidates=[dict(id='C1', checks='pass'), dict(id='C2', checks='pass')],
                          judgment=dict(by='llm', ranking=['C2', 'C1'], reason='More legible headline.',
                                        feedback='Keep type, cool the background.', stop=False, improved=None))

    def test_plan_is_reproducible_and_distinct_with_provenance(self):
        result = combine.plan(self.board, 4)
        self.assertEqual(result, combine.plan(self.board, 4))
        recipes = [c['recipe'] for c in result['combinations']]
        self.assertEqual(len(recipes), 4)
        self.assertEqual(len({tuple(t['id'] for t in r.values()) for r in recipes}), 4)
        for recipe in recipes:
            for axis, tid in self.board['fixed'].items():
                self.assertEqual(recipe[axis]['id'], tid)
            self.assertTrue(all(t['source'] for t in recipe.values()))

    def test_conflicts_and_shortfalls_are_explicit(self):
        self.board['incompatible'] = [['R1:layout', 'R2:palette']]
        result = combine.plan(self.board, 4)
        self.assertEqual(len(result['combinations']), 3)
        self.assertIn('Fewer', result['note'])
        for c in result['combinations']:
            self.assertFalse({'R1:layout', 'R2:palette'} <= {t['id'] for t in c['recipe'].values()})

    def test_invalid_provenance_fixed_axis_and_unknown_traits(self):
        for mutation in ('source', 'fixed', 'unknown', 'duplicate'):
            b = copy.deepcopy(self.board)
            if mutation == 'source':
                b['axes']['lighting'][0]['source_id'] = 'missing'
            elif mutation == 'fixed':
                b['fixed']['palette'] = 'R1:light'
            elif mutation == 'unknown':
                b['axes']['lighting'][0]['confidence'] = 'unknown'
            else:
                b['axes']['lighting'][0]['id'] = 'R1:type'
            with self.assertRaises(ValueError):
                combine.plan(b)

    def test_planner_search_is_bounded_for_large_space(self):
        b = copy.deepcopy(self.board)
        template = b['axes']['lighting'][0]
        b['axes'] = {f'a{i}': [dict(template, id=f'a{i}:t{j}') for j in range(30)] for i in range(10)}
        b['fixed'] = {}
        result = combine.plan(b, 8)
        self.assertEqual(result['space_size'], 30**10)
        self.assertLessEqual(result['evaluated'], 5000)
        self.assertEqual(len(result['combinations']), 8)

    def test_batch_never_iterates(self):
        self.state['mode'] = 'batch'
        self.assertEqual(advance.decide(self.state)['action'], 'complete_batch')
        self.state['judgment'] = None
        self.assertEqual(advance.decide(self.state)['action'], 'awaiting_llm')

    def test_human_and_hybrid_wait_for_actual_input(self):
        for judge in ('human', 'hybrid'):
            self.state['judge'] = judge
            self.assertEqual(advance.decide(self.state)['action'], 'awaiting_human')
            s = copy.deepcopy(self.state)
            s['judgment'] = None
            self.assertEqual(advance.decide(s)['action'], 'awaiting_human')
        self.state['judgment']['by'] = 'human'
        self.state['judgment']['ranking'] = ['C1']
        result = advance.decide(self.state)
        self.assertEqual(result['action'], 'iterate')
        self.assertEqual(result['parent_id'], 'C1')

    def test_ineligible_incomplete_or_duplicate_ranking_cannot_win(self):
        for ranking in (['C1'], ['C1', 'C1'], ['unknown', 'C1']):
            self.state['judgment']['ranking'] = ranking
            with self.assertRaises(ValueError):
                advance.decide(self.state)
        self.state['judgment']['ranking'] = ['C2', 'C1']
        for status in ('fail', 'uncertain'):
            self.state['candidates'][1]['checks'] = status
            with self.assertRaises(ValueError):
                advance.decide(self.state)

    def test_budget_and_parent(self):
        result = advance.decide(self.state)
        self.assertEqual(result['parent_id'], 'C2')
        self.assertEqual(result['remaining_images'], 6)
        for key in ('images_used', 'rounds_completed'):
            s = copy.deepcopy(self.state)
            s[key] = 8
            if key == 'rounds_completed':
                s['incumbent_id'] = 'C1'
            self.assertEqual(advance.decide(s)['action'], 'stop_budget')

    def test_no_improvement_and_uncertain_comparison_stop(self):
        self.state['rounds_completed'] = 2
        self.state['incumbent_id'] = 'C1'
        self.assertEqual(advance.decide(self.state)['action'], 'stop_uncertain_comparison')
        self.state['no_improvement_rounds'] = 1
        self.state['judgment']['improved'] = False
        self.state['judgment']['ranking'] = ['C1', 'C2']
        self.assertEqual(advance.decide(self.state)['action'], 'stop_no_improvement')
        self.state['judgment']['improved'] = True
        self.state['judgment']['ranking'] = ['C2', 'C1']
        self.assertEqual(advance.decide(self.state)['no_improvement_rounds'], 0)

    def test_cannot_replace_incumbent_without_improvement(self):
        self.state.update(rounds_completed=2, incumbent_id='C1')
        self.state['judgment']['improved'] = False
        with self.assertRaises(ValueError):
            advance.decide(self.state)
        self.state['incumbent_id'] = None
        with self.assertRaises(ValueError):
            advance.decide(self.state)

    def test_human_stop_and_no_eligible_candidate(self):
        self.state['judgment'].update(by='human', stop=True, ranking=[])
        self.assertEqual(advance.decide(self.state)['action'], 'stop_human')
        self.state['judgment'] = None
        for c in self.state['candidates']:
            c['checks'] = 'fail'
        self.assertEqual(advance.decide(self.state)['action'], 'stop_no_eligible')

    def test_invalid_state_fails_closed(self):
        for key, value in (('mode', 'forever'), ('images_used', -1), ('max_images', True),
                           ('max_rounds', '3'), ('judgment', {'by': 'pretend'})):
            s = copy.deepcopy(self.state)
            s[key] = value
            with self.assertRaises(ValueError):
                advance.decide(s)

    def test_cli_refuses_to_overwrite_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)/'plan.json'
            cmd = [sys.executable, str(ROOT/'skills/inspiration/scripts/combine.py'),
                   str(ROOT/'examples/inspiration/board.json'), '--out', str(out)]
            self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 0)
            first = out.read_bytes()
            self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)
            self.assertEqual(out.read_bytes(), first)


if __name__ == '__main__':
    unittest.main()
