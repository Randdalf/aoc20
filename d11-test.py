#!/usr/bin/env python

"""Advent of Code 2020, Day 11 (Unit Tests)"""

import unittest

from d11 import parse, occupied_seats

example1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


class OccupiedSeatsTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(occupied_seats(parse(example1)), 37)


if __name__ == "__main__":
    unittest.main()
