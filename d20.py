#!/usr/bin/env python

"""Advent of edge 2020, Day 20"""

from functools import reduce
from itertools import product
from math import sqrt
from operator import mul

from aoc import solve
from vec2 import Vec2


class DIR:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


orientations = list(product([False, True], [False, True], [0, 1, 2, 3]))
flipped = {}


def orient(pos, size, vflip, hflip, rotations):
    for i in range(rotations):
        t = pos.y
        pos.y = size - pos.x - 1
        pos.x = t
    if vflip:
        pos.y = size - pos.y - 1
    if hflip:
        pos.x = size - pos.x - 1
    return pos


class Tile:
    def __init__(slf, data):
        lines = data.split('\n')
        slf.id = int(lines[0].strip('Tile: '))
        slf.size = len(lines[1])
        slf.image = {}
        for y, row in enumerate(lines[1:]):
            for x, col in enumerate(row):
                slf.image[Vec2(x, y)] = col
        slf.edges = []
        slf.compute_edges(Vec2(0, 0), Vec2(1, 0))
        slf.compute_edges(Vec2(slf.size - 1, 0), Vec2(0, 1))
        slf.compute_edges(Vec2(slf.size - 1, slf.size - 1), Vec2(-1, 0))
        slf.compute_edges(Vec2(0, slf.size - 1), Vec2(0, -1))
        slf.orientation = 0

    def compute_edges(slf, pos, dir):
        cells = []
        while pos in slf.image:
            cells.append(slf.image[pos])
            pos += dir
        fwd = ''.join(cells).replace('#', '1').replace('.', '0')
        bwd = fwd[::-1]
        slf.edges.append(int(fwd, 2))
        slf.edges.append(int(bwd, 2))
        flipped[slf.edges[-1]] = slf.edges[-2]
        flipped[slf.edges[-2]] = slf.edges[-1]

    def edge(slf, dir):
        vflip, hflip, rotations = orientations[slf.orientation]
        rev = False
        dir = (dir - rotations) % 4
        if vflip:
            rev = not rev
            if dir % 2 == 0:
                dir = (dir - 2) % 4
        if hflip:
            rev = not rev
            if dir % 2 == 1:
                dir = (dir - 2) % 4
        return slf.edges[dir * 2 + rev]

    def get(slf, x, y):
        pos = orient(Vec2(x, y), slf.size, *orientations[slf.orientation])
        return slf.image[pos]


def parse(data):
    return [Tile(x) for x in data.split('\n\n')]


def find_corners(tiles):
    corners = []
    for tile in tiles:
        edges = {c for t in tiles if t != tile for c in t.edges}
        if sum(edge in edges for edge in tile.edges) == 4:
            corners.append(tile)
    return corners


def corner_ids(tiles):
    return reduce(mul, (corner.id for corner in find_corners(tiles)))


def assemble(tiles):
    tiles = list(tiles)
    corners = find_corners(tiles)
    size = int(sqrt(len(tiles)))
    grid = {}

    # Start by locking a corner tile into the top-left, and rotating it until
    # its non-connected edges are facing outwards.
    corner = corners[0]
    tiles.remove(corner)
    edges = {c: t for t in tiles for c in t.edges}
    while corner.edge(DIR.EAST) not in edges or corner.edge(DIR.SOUTH) not in edges:
        corner.orientation += 1
    grid[Vec2(0, 0)] = corner

    # Find all tiles on the top row by matching east/west edges, and empty
    # edges along the top.
    for x in range(1, size):
        east = flipped[grid[Vec2(x - 1, 0)].edge(DIR.EAST)]
        tile = edges[east]
        tiles.remove(tile)
        edges = {c: t for t in tiles for c in t.edges}
        while tile.edge(DIR.WEST) != east or tile.edge(DIR.NORTH) in edges:
            tile.orientation += 1
        grid[Vec2(x, 0)] = tile

    # Find all tiles on the left row by matching south/north edges, and empty
    # edges along the left.
    for y in range(1, size):
        south = flipped[grid[Vec2(0, y - 1)].edge(DIR.SOUTH)]
        tile = edges[south]
        tiles.remove(tile)
        edges = {c: t for t in tiles for c in t.edges}
        while tile.edge(DIR.WEST) in edges or tile.edge(DIR.NORTH) != south:
            tile.orientation += 1
        grid[Vec2(0, y)] = tile

    # Fill in all remaining tiles by matching east/west and south/north edges.
    for y in range(1, size):
        for x in range(1, size):
            south = flipped[grid[Vec2(x, y - 1)].edge(DIR.SOUTH)]
            east = flipped[grid[Vec2(x - 1, y)].edge(DIR.EAST)]
            tile = edges[south]
            tiles.remove(tile)
            edges = {c: t for t in tiles for c in t.edges}
            while tile.edge(DIR.WEST) != east or tile.edge(DIR.NORTH) != south:
                tile.orientation += 1
            grid[Vec2(x, y)] = tile

    return grid, size


def reconstruct(grid, size):
    image = {}
    for pos, tile in grid.items():
        offset = pos * (tile.size - 2)
        for y in range(1, tile.size-1):
            for x in range(1, tile.size-1):
                image[Vec2(x-1, y-1) + offset] = tile.get(x, y)
    return image, max(pos.x for pos in image) + 1


sea_monster_image = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """


def get_sea_monster():
    rows = sea_monster_image.split('\n')
    w = len(rows[0])
    h = len(rows)
    monster = set()
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if col == '#':
                monster.add(Vec2(x, y))
    return monster, w, h


def find_monsters(image, size, monster, w, h):
    for orientation in orientations:
        oriented = {}
        for y in range(size):
            for x in range(size):
                pos = orient(Vec2(x, y), size, *orientation)
                oriented[Vec2(x, y)] = image[pos]

        monsters = set()
        for y in range(size - h):
            for x in range(size - w):
                matches = set()
                for off in monster:
                    pos = Vec2(x, y) + off
                    if oriented[pos] == '#':
                        matches.add(pos)
                if len(matches) == len(monster):
                    monsters.update(matches)
        if len(monsters) > 0:
            return sum(c == '#' for pos, c in oriented.items() if pos not in monsters)


def water_roughness(tiles, print_image=False):
    grid, size = assemble(tiles)
    image, size = reconstruct(grid, size)

    if print_image:
        print()
        for y in range(size):
            for x in range(size):
                pos = Vec2(x, y)
                if pos in image:
                    print(image[pos], end='')
                else:
                    print(' ', end='')
            print()

    monster, w, h = get_sea_monster()
    return find_monsters(image, size, monster, w, h)


if __name__ == "__main__":
    solve(20, parse, corner_ids, water_roughness)
