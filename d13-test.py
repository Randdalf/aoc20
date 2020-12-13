#!/usr/bin/env python

"""Advent of Code 2020, Day 13 (Unit Tests)"""

import unittest

from d13 import parse, earliest_bus, contest

example1 = """939
7,13,x,x,59,x,31,19"""

example2 = """0
17,x,13,19"""

example3 = """0
67,7,59,61"""

example4 = """0
67,x,7,59,61"""

example5 = """0
67,7,x,59,61"""

example6 = """0
1789,37,47,1889"""


class EarliestBusTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(earliest_bus(parse(example1)), 295)


class ContestTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(contest(parse(example1)), 1068781)

    def test_example2(slf):
        slf.assertEqual(contest(parse(example2)), 3417)

    def test_example3(slf):
        slf.assertEqual(contest(parse(example3)), 754018)

    def test_example4(slf):
        slf.assertEqual(contest(parse(example4)), 779210)

    def test_example5(slf):
        slf.assertEqual(contest(parse(example5)), 1261476)

    def test_example6(slf):
        slf.assertEqual(contest(parse(example6)), 1202161486)


if __name__ == "__main__":
    unittest.main()
