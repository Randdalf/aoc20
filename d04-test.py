#!/usr/bin/env python

"""Advent of Code 2020, Day 4 (Unit Tests)"""

import unittest

from d04 import parse, num_valid_passports

example1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


class NumValidPassportsTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(num_valid_passports(parse(example1)), 2)


if __name__ == "__main__":
    unittest.main()
