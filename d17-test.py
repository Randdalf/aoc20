#!/usr/bin/env python

"""Advent of Code 2020, Day 17 (Unit Tests)"""

import unittest

from d17 import parse, simulate

example1 = """.#.
..#
###"""


class SimulateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(simulate(parse(example1)), 112)


if __name__ == "__main__":
    unittest.main()
