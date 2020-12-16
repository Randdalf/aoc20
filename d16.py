#!/usr/bin/env python

"""Advent of Code 2020, Day 16"""

from functools import reduce
from operator import mul
import re

from aoc import solve


class Document:
    def __init__(slf, data):
        parts = data.split('\n\n')
        rule_pattern = re.compile(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)')

        # Rules
        slf.fields = {}
        for line in parts[0].split('\n'):
            gs = rule_pattern.match(line).groups()
            slf.fields[gs[0]] = [
                (int(gs[1]), int(gs[2])),
                (int(gs[3]), int(gs[4]))
            ]

        # My ticket
        slf.ticket = [int(x) for x in parts[1].strip('your ticket:\n').split(',')]

        # Nearby tickets
        slf.nearby = []
        for line in parts[2].strip('nearby tickets:\n').split('\n'):
            slf.nearby.append([int(x) for x in line.split(',')])


def parse(data):
    return Document(data)


def valid(doc, v):
    return any(lo <= v <= hi for rules in doc.fields.values() for lo, hi in rules)


def error_rate(doc):
    error_rate = 0
    for ticket in doc.nearby:
        for v in ticket:
            if not valid(doc, v):
                error_rate += v
    return error_rate


def identify(doc):
    tickets = [t for t in doc.nearby if all(valid(doc, v) for v in t)]
    fields = set(doc.fields.keys())
    positions = set(range(len(doc.ticket)))
    assigned = {}
    while len(fields) > 0:
        for field in list(fields):
            rules = doc.fields[field]
            possible = []
            for p in positions:
                n = sum(lo <= t[p] <= hi for t in tickets for lo, hi in rules)
                if n == len(tickets):
                    possible.append(p)
            if len(possible) == 1:
                position = possible.pop()
                assigned[field] = position
                fields.remove(field)
                positions.remove(position)
    return reduce(mul, (doc.ticket[assigned[f]] for f in assigned if f.startswith('departure')))

if __name__ == "__main__":
    solve(16, parse, error_rate, identify)
