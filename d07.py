#!/usr/bin/env python

"""Advent of Code 2020, Day 7"""

import re

from aoc import solve


def parse(data):
    bag_pattern = re.compile(r'(\d+) (\w+ \w+) bags?')
    rules = {}
    for rule in data.split('\n'):
        color, bags = rule.split(' bags contain ')
        rules[color] = {c: int(n) for n, c in bag_pattern.findall(bags)}
    return rules


def num_colors_that_fit(rules, target='shiny gold'):
    has_target = {color for color, rule in rules.items() if target in rule}
    no_target = rules.keys() - has_target
    changes = {''}
    while len(changes) > 0:
        changes = {
            color for color in no_target
            if not rules[color].keys().isdisjoint(has_target)
        }
        has_target |= changes
        no_target -= changes
    return len(has_target)


if __name__ == "__main__":
    solve(7, parse, num_colors_that_fit)
