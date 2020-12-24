#!/usr/bin/env python

"""Advent of Code 2020, Day 24"""

import re

from aoc import solve
from vec2 import Vec2

dirs = {
    'e': Vec2(2, 0),
    'w': Vec2(-2, 0),
    'se': Vec2(1, 1),
    'sw': Vec2(-1, 1),
    'ne': Vec2(1, -1),
    'nw': Vec2(-1, -1)
}


def parse(data):
    pattern = re.compile(r'e|w|se|sw|ne|nw')
    return [pattern.findall(x) for x in data.split('\n')]


def flip_tiles(instrs):
    black = set()
    for instr in instrs:
        tile = Vec2(0, 0)
        for dir in instr:
            tile += dirs[dir]
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)
    return len(black)


if __name__ == "__main__":
    solve(24, parse, flip_tiles)
