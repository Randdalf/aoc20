#!/usr/bin/env python

"""Advent of Code 2020, Day 16 (Unit Tests)"""

import unittest

from d16 import parse, error_rate

example1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


class ErrorRateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(error_rate(parse(example1)), 71)


if __name__ == "__main__":
    unittest.main()
