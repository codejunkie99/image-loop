"""Pure review policy shared by the CLI and offline tests."""
import json


def coverage_errors(brief, report):
    expected = [c['id'] for c in brief['criteria']]
    actual = [c['id'] for c in report['criteria']]
    if len(expected) != len(set(expected)):
        return ['Brief criterion IDs must be unique.']
    if len(actual) != len(set(actual)) or set(actual) != set(expected):
        return ['Review must cover every criterion exactly once, with no invented IDs.']
    if any(not c['evidence'].strip() for c in report['criteria']):
        return ['Every verdict needs visible evidence or a reason it is uncertain.']
    return []


def decide(brief, report, checks, repairs_used=0, max_repairs=3, previous=None):
    errors = coverage_errors(brief, report)
    if previous is not None:
        errors += coverage_errors(brief, previous)
    if errors:
        return {'action': 'stop_invalid_review', 'reason': ' '.join(errors)}
    if repairs_used < 0 or max_repairs < 0:
        raise ValueError('Repair counts must be nonnegative.')
    failing = [c for c in report['criteria'] if c['status'] == 'fail']
    uncertain = [c for c in report['criteria'] if c['status'] == 'uncertain']
    if uncertain:
        return {'action': 'escalate', 'reason': 'Uncertain evidence requires stronger inspection.',
                'ids': [c['id'] for c in uncertain]}
    if not checks['passed']:
        return {'action': 'stop_file_checks', 'reason': 'Resolve output-file failures before acceptance or further generative edits.',
                'failures': checks['failures']}
    if not failing:
        return {'action': 'accepted_by_checks', 'reason': 'All requested and protected criteria and file checks passed.'}
    if repairs_used >= max_repairs:
        return {'action': 'stop_budget', 'reason': 'Repair limit reached.', 'ids': [c['id'] for c in failing]}
    if previous is not None and repairs_used > 0:
        old = {c['id'] for c in previous['criteria'] if c['status'] == 'fail'}
        if old == {c['id'] for c in failing}:
            return {'action': 'escalate', 'reason': 'Same failure set persisted after a repair.', 'ids': sorted(old)}
    protected = {c['id'] for c in brief['criteria'] if c['kind'] == 'protected'}
    return {'action': 'repair', 'reason': 'Repair only the failed requirements; recheck all criteria.',
            'ids': [c['id'] for c in failing],
            'protected_failed': [c['id'] for c in failing if c['id'] in protected]}


def repair_prompt(brief, report, decision):
    if decision['action'] != 'repair':
        return ''
    failed = set(decision['ids'])
    lookup = {c['id']: c for c in report['criteria']}
    lines = ['Edit the supplied clean image according to this brief:', brief['intent'],
             '', 'Correct these observed failures:']
    for c in brief['criteria']:
        if c['id'] in failed:
            r = lookup[c['id']]
            lines += [f"- {c['id']} ({c['target']}): {c['requirement']}",
                      f"  Reviewer observation: {r['evidence']}",
                      f"  Suggested minimal fix: {r['suggested_fix']}"]
    lines += ['', 'Maintain every requirement below; do not introduce unrelated improvements:']
    lines += [f"- {c['id']}: {c['requirement']}" for c in brief['criteria']]
    lines += ['', 'Output file requirements: '+json.dumps(brief['file_checks']),
              'Do not add review badges, numbering, or annotation arrows.',
              'If source and candidate are both supplied, use the source for preserved appearance and the stated edit for changes.']
    return '\n'.join(lines)+'\n'
