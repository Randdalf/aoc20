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


def flip_tiles(instrs, num=True):
    black = set()
    for instr in instrs:
        tile = Vec2(0, 0)
        for dir in instr:
            tile += dirs[dir]
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)
    return len(black) if num else black


def adjacencies(tile):
    yield from (tile + dir for dir in dirs.values())


def art_exhibit(instrs, days=100, verbose=False):
    black = flip_tiles(instrs, num=False)
    for day in range(1, days+1):
        new_black = set()
        for tile in {adj for tile in black for adj in adjacencies(tile)}:
            n = sum(adj in black for adj in adjacencies(tile))
            if tile in black and 1 <= n <= 2:
                new_black.add(tile)
            elif tile not in black and n == 2:
                new_black.add(tile)
        black = new_black
        if verbose and (day <= 10 or day % 10 == 0):
            print(f'Day {day}: {len(black)}')
            if day == 10:
                print()
    return len(black)


if __name__ == "__main__":
    solve(24, parse, flip_tiles, art_exhibit)
