#!/usr/bin/env python

"""Advent of Code 2020, Day 17"""

from functools import reduce
from itertools import product

from aoc import solve


def parse(data):
    rows = data.split('\n')
    w = h = len(rows)
    off = w // 2
    active = set()
    for x, row in enumerate(rows):
        for y, col in enumerate(row):
            if col == '#':
                active.add((x-off, y-off, 0))
    return active


def combine(a, b, op):
    return (op(a[0], b[0]), op(a[1], b[1]), op(a[2], b[2]))


offsets = [f for f in product(range(-1, 2), repeat=3) if f != (0, 0, 0)]


def count_neighbors(active, pos):
    count = 0
    for offset in offsets:
        neighbor = (pos[0]+offset[0], pos[1]+offset[1], pos[2]+offset[2])
        count += neighbor in active
    return count


def simulate(active, cycles=6):
    for cycle in range(cycles):
        cmin = reduce(lambda a, b: combine(a, b, min), active)
        cmax = reduce(lambda a, b: combine(a, b, max), active)
        new = set()
        for x in range(cmin[0] - 1, cmax[0] + 2):
            for y in range(cmin[1] - 1, cmax[1] + 2):
                for z in range(cmin[2] - 1, cmax[2] + 2):
                    pos = (x, y, z)
                    n = count_neighbors(active, pos)
                    if pos in active and n in [2, 3]:
                        new.add(pos)
                    elif pos not in active and n == 3:
                        new.add(pos)
        active = new
    return len(active)


if __name__ == "__main__":
    solve(17, parse, simulate)
