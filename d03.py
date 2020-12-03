#!/usr/bin/env python

"""Advent of Code 2020, Day 3"""

from aoc import solve
from vec2 import Vec2


class Terrain:
    def __init__(slf, data):
        rows = data.split('\n')
        slf.w = len(rows[0])
        slf.h = len(rows)
        slf.tiles = {}
        for y, row in enumerate(rows):
            for x, col in enumerate(row):
                slf.tiles[Vec2(x, y)] = col

    def get(slf, pos):
        return slf.tiles[Vec2(pos.x % slf.w, pos.y)]


def parse(data):
    return Terrain(data)


def count_trees(terrain, pos=Vec2(0, 0), slope=Vec2(3, 1)):
    num_trees = 0
    while pos.y < terrain.h:
        num_trees += terrain.get(pos) == '#'
        pos += slope
    return num_trees


if __name__ == "__main__":
    solve(3, parse, count_trees)
