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
    num = 0
    if n > 2:
        num += num_combos(n - 3)
    if n > 1:
        num += num_combos(n - 2)
    if n > 0:
        num += num_combos(n - 1)
    if n == 0:
        num += 1
    return num


def arrangements(adapters):
    diffs = compute_diffs(adapters)
    counts = [len(list(g)) for k, g in groupby(diffs, lambda x: x == 3) if not k]
    return reduce(lambda x, y: x*y, (num_combos(n) for n in counts))


if __name__ == "__main__":
    solve(10, parse, jolt_1_3, arrangements)
