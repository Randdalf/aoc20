#!/usr/bin/env python

"""Advent of Code 2020, Day 21"""

from functools import reduce
from operator import and_ as intersect

from aoc import solve


def parse(data):
    foods = []
    for line in data.split('\n'):
        ingredients, allergens = line.split(' (contains ')
        foods.append((set(ingredients.split(' ')), set(allergens[:-1].split(', '))))
    return foods


def no_allergens(foods):
    allergens = {a for _, alls in foods for a in alls}
    ingredients = {i for ings, _ in foods for i in ings}
    has_allergens = set()
    for a in allergens:
        has_allergens |= reduce(intersect, (ings for ings, alls in foods if a in alls))
    no_allergens = ingredients - has_allergens
    return sum(i in no_allergens for ings, _ in foods for i in ings)


if __name__ == "__main__":
    solve(21, parse, no_allergens)
