#!/usr/bin/env python

"""Advent of Code 2020, Day 6"""

from functools import reduce

from aoc import solve


def parse(data):
    return [[set(p) for p in g.split('\n')] for g in data.split('\n\n')]


def anyone_answers(groups):
    return sum(len(reduce(lambda x, y: x | y, g)) for g in groups)


def everyone_answers(groups):
    return sum(len(reduce(lambda x, y: x & y, g)) for g in groups)


if __name__ == "__main__":
    solve(6, parse, anyone_answers, everyone_answers)
