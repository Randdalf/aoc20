#!/usr/bin/env python

"""Advent of Code 2020, Day 11 (Unit Tests)"""

import unittest

from d11 import parse, occupied_seats1, occupied_seats2

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


class OccupiedSeats1Tests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(occupied_seats1(parse(example1)), 37)


class OccupiedSeats2Tests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(occupied_seats2(parse(example1)), 26)


if __name__ == "__main__":
    unittest.main()
