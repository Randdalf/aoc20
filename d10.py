#!/usr/bin/env python

"""Advent of Code 2020, Day 10"""

from functools import reduce
from itertools import groupby

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def compute_diffs(adapters):
    jolts = [0] + sorted(adapters) + [3 + max(adapters)]
    return [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]


def jolt_1_3(adapters):
    diffs = compute_diffs(adapters)
    return diffs.count(1) * diffs.count(3)


def num_combos(n):
    return 1 if n == 0 else sum(num_combos(n-k) for k in range(1, min(n, 3)+1))


def arrangements(adapters):
    diffs = compute_diffs(adapters)
    runs = [len(list(g)) for k, g in groupby(diffs, lambda x: x == 1) if k]
    return reduce(lambda x, y: x*y, (num_combos(n) for n in runs))


if __name__ == "__main__":
    solve(10, parse, jolt_1_3, arrangements)
