#!/usr/bin/env python

"""Advent of Code 2020, Day 21"""

from functools import reduce
from operator import and_

from aoc import solve


def parse(data):
    foods = []
    for line in data.split('\n'):
        ings, alls = line.split(' (contains ')
        foods.append((set(ings.split(' ')), set(alls[:-1].split(', '))))
    return foods


def find_inert(foods):
    dangerous = set()
    for a in {a for _, alls in foods for a in alls}:
        dangerous |= reduce(and_, (ings for ings, alls in foods if a in alls))
    return {i for ings, _ in foods for i in ings} - dangerous


def num_inert(foods):
    inert = find_inert(foods)
    return sum(i in inert for ings, _ in foods for i in ings)


def danger_list(foods):
    ignore = find_inert(foods)
    open = {a for _, alls in foods for a in alls}
    map = {}
    while open:
        for a in list(open):
            contains = reduce(and_, (ings - ignore for ings, alls in foods if a in alls))
            if len(contains) == 1:
                ing = contains.pop()
                map[a] = ing
                open.remove(a)
                ignore.add(ing)
    return ','.join(map[k] for k in sorted(map.keys()))


if __name__ == "__main__":
    solve(21, parse, num_inert, danger_list)
