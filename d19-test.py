#!/usr/bin/env python

"""Advent of Code 2020, Day 19 (Unit Tests)"""

import unittest

from d19 import parse, matches

example1 = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""


class SolverTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(matches(parse(example1)), 2)


if __name__ == "__main__":
    unittest.main()
