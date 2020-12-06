#!/usr/bin/env python

"""Advent of Code 2020, Day 6 (Unit Tests)"""

import unittest

from d06 import parse, anyone_answers, everyone_answers

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


class AnyoneAnswersTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(anyone_answers(parse(example1)), 6)

    def test_example2(slf):
        slf.assertEqual(anyone_answers(parse(example2)), 11)


class EveryoneAnswersTests(unittest.TestCase):
    def test_example2(slf):
        slf.assertEqual(everyone_answers(parse(example2)), 6)


if __name__ == "__main__":
    unittest.main()
