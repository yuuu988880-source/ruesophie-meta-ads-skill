#!/usr/bin/env python3
"""Check declared fields of one A/B pair; no claims about actual delivery."""
import argparse
import json
from pathlib import Path

TEXT_FIELDS = ('overlay', 'primary_text', 'headline', 'description', 'cta')
REQUIRED = set(TEXT_FIELDS) | {'image', 'layout', 'landing_page', 'settings'}


def check(data):
    errors = []
    if not isinstance(data, dict):
        return {'valid': False, 'errors': ['Root must be an object.']}
    variable = data.get('variable')
    a, b = data.get('a'), data.get('b')
    if not isinstance(a, dict) or not isinstance(b, dict):
        return {'valid': False, 'errors': ['a and b must be objects.']}
    for name, row in [('a', a), ('b', b)]:
        missing = REQUIRED - row.keys()
        if missing:
            errors.append(f'{name}: missing fields {sorted(missing)}')
        for field in TEXT_FIELDS:
            if field in row and not isinstance(row[field], str):
                errors.append(f'{name}.{field}: expected string')
    if not isinstance(variable, str) or variable not in REQUIRED:
        errors.append('variable must name one supported field.')
    if a.keys() != b.keys():
        errors.append('a and b must have identical field sets.')
    changed = sorted(k for k in a.keys() | b.keys() if k not in a or k not in b or a[k] != b[k])
    if changed != [variable]:
        errors.append(f'Expected only {variable!r} to change; found {changed}.')
    counts = {name: {k: {'characters': len(row[k]), 'words': len(row[k].split())}
                     for k in TEXT_FIELDS if isinstance(row.get(k), str)}
              for name, row in [('a', a), ('b', b)]}
    return {'valid': not errors, 'changed_fields': changed, 'errors': errors,
            'text_counts': counts,
            'scope': 'Listed fields only. Does not verify images, real account settings, or causality.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pair', type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.pair.read_text(encoding='utf-8')))
    except (OSError, ValueError) as error:
        result = {'valid': False, 'errors': [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
