#!/usr/bin/env python

"""Advent of Code 2020, Day 16"""

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


def valid(doc, value):
    for rules in doc.fields.values():
        for lo, hi in rules:
            if lo <= value <= hi:
                return True
    return False


def error_rate(doc):
    error_rate = 0
    for ticket in doc.nearby:
        for value in ticket:
            if not valid(doc, value):
                error_rate += value
    return error_rate


if __name__ == "__main__":
    solve(16, parse, error_rate)
