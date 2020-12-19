#!/usr/bin/env python

"""Advent of Code 2020, Day 19"""

import re

from aoc import solve


class Input:
    def __init__(slf, data):
        parts = data.split('\n\n')
        slf.rules = {}
        for line in parts[0].split('\n'):
            id, body = line.split(': ')
            slf.rules[id] = body.replace('"', '').split(' ')
        slf.messages = parts[1].split('\n')


def parse(data):
    return Input(data)


def build_regex(rules, root='0'):
    expanded = rules[root]
    while True:
        new = []
        for c in expanded:
            if c in rules:
                new.append('(')
                new.extend(rules[c])
                new.append(')')
            else:
                new.append(c)
        if len(new) == len(expanded):
            return re.compile('^' + ''.join(new) + '$')
        expanded = new


def matches(input):
    pattern = build_regex(input.rules)
    return sum(pattern.match(msg) is not None for msg in input.messages)


if __name__ == "__main__":
    solve(19, parse, matches)
