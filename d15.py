#!/usr/bin/env python

"""Advent of Code 2020, Day 15"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split(',')]


def memory_game(start, max_turns=2020):
    spoken = {n: i for i, n in enumerate(start[:-1])}
    prev = start[-1]
    for turn in range(len(start), max_turns):
        n = turn - spoken[prev] - 1 if prev in spoken else 0
        spoken[prev] = turn - 1
        prev = n
    return prev


if __name__ == "__main__":
    solve(15, parse, memory_game)
