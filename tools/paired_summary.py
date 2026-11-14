#!/usr/bin/env python3
"""Descriptive paired binary error comparison; see docs/evaluation.md."""
import argparse
import csv


def summarize(rows):
    pairs = []
    for row in rows:
        try:
            a, b = row['baseline_error'], row['candidate_error']
        except KeyError as exc:
            raise ValueError('CSV requires baseline_error and candidate_error columns') from exc
        if a not in ('0', '1') or b not in ('0', '1'):
            raise ValueError('error values must be 0 or 1')
        pairs.append((int(a), int(b)))
    n = len(pairs)
    if n < 2:
        raise ValueError('at least two rows are required')
    fixed = sum(a == 1 and b == 0 for a, b in pairs)
    broken = sum(a == 0 and b == 1 for a, b in pairs)
    diffs = [a - b for a, b in pairs]
    mean = sum(diffs) / n
    return n, fixed, broken, mean


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path')
    args = parser.parse_args()
    try:
        with open(args.csv_path, newline='', encoding='utf-8') as f:
            result = summarize(csv.DictReader(f))
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f'error: {exc}\n')
    n, fixed, broken, mean = result
    print(f'rows={n} fixed={fixed} broken={broken} net_fixed={fixed - broken}')
    print(f'mean error reduction={mean:.6f}')
    print('Descriptive only: rows may not be independent. No uncertainty or statistical test is computed; see docs/evaluation.md.')


if __name__ == '__main__':
    main()
