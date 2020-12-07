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


def has_target(rules, color, target):
    rule = rules[color]
    return target in rule or any(has_target(rules, c, target) for c in rule.keys())


def num_colors_that_fit(rules, target='shiny gold'):
    return sum(has_target(rules, color, target) for color in rules.keys())


def bags_within(rules, target='shiny gold'):
    return sum(n*(1 + bags_within(rules, color)) for color, n in rules[target].items())


if __name__ == "__main__":
    solve(7, parse, num_colors_that_fit, bags_within)
