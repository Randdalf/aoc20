#!/usr/bin/env python

"""Advent of Code 2020, Day 25"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def encryption_key(keys):
    n = 1
    encryption_key = 1
    while n != keys[0]:
        n = (n * 7) % 20201227
        encryption_key = (encryption_key * keys[1]) % 20201227
    return encryption_key


if __name__ == "__main__":
    solve(25, parse, encryption_key)
