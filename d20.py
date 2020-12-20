#!/usr/bin/env python

"""Advent of Code 2020, Day 20"""

from functools import reduce
from operator import mul

from aoc import solve
from vec2 import Vec2


class Tile:
    def __init__(slf, data):
        lines = data.split('\n')
        slf.id = int(lines[0].strip('Tile: '))
        slf.w = slf.h = len(lines[1])
        slf.image = {}
        for y, row in enumerate(lines[1:]):
            for x, col in enumerate(row):
                slf.image[Vec2(x, y)] = col
        slf.codes = []
        slf.compute_codes(Vec2(0, 0), Vec2(1, 0))
        slf.compute_codes(Vec2(0, 0), Vec2(0, 1))
        slf.compute_codes(Vec2(slf.w - 1, 0), Vec2(0, 1))
        slf.compute_codes(Vec2(0, slf.h - 1), Vec2(1, 0))

    def compute_codes(slf, pos, dir):
        cells = []
        while pos in slf.image:
            cells.append(slf.image[pos])
            pos += dir
        fwd = ''.join(cells).replace('#', '1').replace('.', '0')
        bwd = fwd[::-1]
        slf.codes.append(int(fwd, 2))
        slf.codes.append(int(bwd, 2))


def parse(data):
    return [Tile(x) for x in data.split('\n\n')]


def corner_ids(tiles):
    corners = []
    for tile in tiles:
        codes = {c for t in tiles if t != tile for c in t.codes}
        if sum(code in codes for code in tile.codes) == 4:
            corners.append(tile)
    return reduce(mul, (corner.id for corner in corners))


if __name__ == "__main__":
    solve(20, parse, corner_ids)
