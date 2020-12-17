#!/usr/bin/env python

"""Advent of Code 2020, Day 17"""

from functools import reduce
from itertools import product

from aoc import solve


def parse(data):
    rows = data.split('\n')
    w = h = len(rows)
    off = w // 2
    init = set()
    for x, row in enumerate(rows):
        for y, col in enumerate(row):
            if col == '#':
                init.add((x-off, y-off))
    return init


def combine(a, b, op):
    return tuple(op(x, y) for x, y in zip(a, b))


def simulate(init, dim, cycles=6):
    app = tuple(0 for x in range(dim - 2))
    active = set(tuple(i + app) for i in init)
    offsets = [x for x in product(range(-1, 2), repeat=dim)]
    offsets.remove(tuple(0 for x in range(dim)))
    for cycle in range(cycles):
        neighbors = set()
        for pos in active:
            for offset in offsets:
                neighbors.add(tuple(a + b for a, b in zip(pos, offset)))
        new = set()
        for pos in neighbors:
            n = 0
            for offset in offsets:
                neighbor = tuple(a + b for a, b in zip(pos, offset))
                n += neighbor in active
            if pos in active and n in [2, 3]:
                new.add(pos)
            elif pos not in active and n == 3:
                new.add(pos)
        active = new
    return len(active)


def sim3(init):
    return simulate(init, dim=3)


def sim4(init):
    return simulate(init, dim=4)


if __name__ == "__main__":
    solve(17, parse, sim3, sim4)
