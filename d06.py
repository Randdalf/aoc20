#!/usr/bin/env python

"""Advent of Code 2020, Day 6"""

from aoc import solve


def parse(data):
    for group in data.split('\n\n'):
        yield group.split('\n')


def count_answers(groups):
    return sum(len({a for p in g for a in p}) for g in groups)


if __name__ == "__main__":
    solve(6, parse, count_answers)
