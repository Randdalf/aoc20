#!/usr/bin/env python

"""Advent of Code 2020, Day 9 (Unit Tests)"""

import unittest

from d09 import parse, invalid, weakness

example1 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


class InvalidTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(invalid(parse(example1), 5), 127)


class WeaknessTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(weakness(parse(example1), 5), 62)


if __name__ == "__main__":
    unittest.main()
