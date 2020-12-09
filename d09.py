#!/usr/bin/env python

"""Advent of Code 2020, Day 9"""

from itertools import combinations

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def invalid(numbers, preamble=25):
    for i, n in enumerate(numbers[preamble:]):
        if n not in {a+b for a, b in combinations(numbers[i:i+preamble], 2)}:
            return n


def weakness(numbers, preamble=25):
    v = invalid(numbers, preamble)
    s = [sum(numbers[:i]) for i in range(len(numbers))]
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] - s[i] == v:
                r = numbers[i:j]
                return min(r) + max(r)


if __name__ == "__main__":
    solve(9, parse, invalid, weakness)
