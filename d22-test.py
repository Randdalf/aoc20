#!/usr/bin/env python

"""Advent of Code 2020, Day 22 (Unit Tests)"""

import unittest

from d22 import parse, combat, recursive_combat

example1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


class CombatTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(combat(parse(example1)), 306)


class RecursiveCombatTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(recursive_combat(parse(example1)), 291)


if __name__ == "__main__":
    unittest.main()
