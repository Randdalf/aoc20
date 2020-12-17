#!/usr/bin/env python

"""Advent of Code 2020, Day 17 (Unit Tests)"""

import unittest

from d17 import parse, sim3, sim4

example1 = """.#.
..#
###"""


class Sim3Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sim3(parse(example1)), 112)


class Sim4Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sim4(parse(example1)), 848)


if __name__ == "__main__":
    unittest.main()
