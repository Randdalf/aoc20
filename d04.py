#!/usr/bin/env python

"""Advent of Code 2020, Day 4"""

import re

from aoc import solve

height_pattern = re.compile(r'^(\d+)(cm|in)$')
hair_color_pattern = re.compile(r'^#[0-9a-f]{6}$')
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
passport_id_pattern = re.compile(r'^[0-9]{9}$')


def validate_height(x):
    match = height_pattern.match(x)
    if match:
        height = int(match.group(1))
        if match.group(2) == 'cm':
            return 150 <= height <= 193
        else:
            return 59 <= height <= 76
    return False


validators = {
    'byr': lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
    'iyr': lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
    'eyr': lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
    'hgt': validate_height,
    'hcl': lambda x: hair_color_pattern.match(x) is not None,
    'ecl': lambda x: x in eye_colors,
    'pid': lambda x: passport_id_pattern.match(x) is not None,
    'cid': lambda x: True
}

required_fields = set(validators.keys()) - {'cid'}


def parse(data):
    for batch in data.split('\n\n'):
        passport = {}
        for pair in batch.split():
            key, value = pair.split(':')
            passport[key] = value
        yield passport


def has_required_fields(passport):
    return passport.keys() >= required_fields


def num_valid_passports(passports):
    return sum(has_required_fields(p) for p in passports)


def num_valid_passports_strict(passports):
    num = 0
    for passport in passports:
        if has_required_fields(passport):
            num += sum(
                validators[field](value) for field, value in passport.items()
            ) == len(passport)
    return num


if __name__ == "__main__":
    solve(4, parse, num_valid_passports, num_valid_passports_strict)
