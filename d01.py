#!/usr/bin/env python

"""Advent of Code 2020, Day 1"""

from functools import reduce
from itertools import product

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def find_sum_2020(expenses, n):
    for p in product(expenses, repeat=n):
        if sum(p) == 2020:
            return reduce(lambda x, y: x*y, p)


if __name__ == "__main__":
    solve(1,  parse, lambda x: find_sum_2020(x, 2), lambda x: find_sum_2020(x, 3))
