#!/usr/bin/env python

"""Advent of Code 2020, Day 10"""

from collections import defaultdict

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def jolt_diffs(adapters):
    jolts = [0] + sorted(adapters) + [3 + max(adapters)]
    diffs = defaultdict(int)
    for i in range(1, len(jolts)):
        diffs[jolts[i] - jolts[i-1]] += 1
    return diffs[1] * diffs[3]


if __name__ == "__main__":
    solve(10, parse, jolt_diffs)
