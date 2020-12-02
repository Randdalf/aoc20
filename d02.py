#!/usr/bin/env python

"""Advent of Code 2020, Day 2"""

import re

from aoc import solve


def parse(data):
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    for line in data.split('\n'):
        match = pattern.match(line)
        yield (
            int(match.group(1)),
            int(match.group(2)),
            match.group(3),
            match.group(4)
        )


def num_valid_passwords_wrong(passwords):
    return sum(
        low <= sum(int(c == repeated) for c in password) <= high
        for low, high, repeated, password in passwords
    )


def num_valid_passwords_right(passwords):
    return sum(
        (password[a-1] == once) ^ (password[b-1] == once)
        for a, b, once, password in passwords
    )


if __name__ == "__main__":
    solve(2, parse, num_valid_passwords_wrong, num_valid_passwords_right)
