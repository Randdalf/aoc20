#!/usr/bin/env python

"""Advent of Code 2020, Day 6 (Unit Tests)"""

import unittest

from d06 import parse, count_answers

example1 = """abcx
abcy
abcz"""

example2 = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class CountAnswersTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(count_answers(parse(example1)), 6)

    def test_example2(slf):
        slf.assertEqual(count_answers(parse(example2)), 11)


if __name__ == "__main__":
    unittest.main()
