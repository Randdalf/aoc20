#!/usr/bin/env python

"""Advent of Code 2020, Day 19"""

from itertools import repeat
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


def to_regex(rules, root='0', fix=False, n11=1):
    expanded = rules[root]
    while True:
        new = []
        for c in expanded:
            if c in rules:
                if fix and c == '8':
                    new.extend(['(', '42', '+', ')'])
                elif fix and c == '11':
                    new.append('(')
                    new.extend(repeat('42', n11))
                    new.extend(repeat('31', n11))
                    new.append(')')
                else:
                    new.append('(')
                    new.extend(rules[c])
                    new.append(')')
            else:
                new.append(c)
        if len(new) == len(expanded):
            return  re.compile('^' + ''.join(new) + '$')
        expanded = new


def part1(input):
    pattern = to_regex(input.rules)
    return sum(pattern.match(msg) is not None for msg in input.messages)

def part2(input):
    patterns = [to_regex(input.rules, fix=True, n11=i) for i in range(1, 10)]
    matches = set()
    for pattern in patterns:
        for msg in input.messages:
            if pattern.match(msg):
                matches.add(msg)
    return len(matches)


if __name__ == "__main__":
    solve(19, parse, part1, part2)
