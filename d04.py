#!/usr/bin/env python

"""Advent of Code 2020, Day 4"""

from aoc import solve

required_fields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
])


def parse(data):
    for batch in data.split('\n\n'):
        passport = {}
        for pair in batch.split():
            key, value = pair.split(':')
            passport[key] = value
        yield passport


def num_valid_passports(passports):
    num = 0
    for passport in passports:
        num += set(passport.keys()) >= required_fields
    return num


if __name__ == "__main__":
    solve(4, parse, num_valid_passports)
