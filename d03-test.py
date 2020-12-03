#!/usr/bin/env python

"""Advent of Code 2020, Day 3 (Unit Tests)"""

import unittest

from d03 import parse, count_trees, check_slopes

example1 = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


class CountTreesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(count_trees(parse(example1)), 7)


class CheckSlopesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(check_slopes(parse(example1)), 336)


if __name__ == "__main__":
    unittest.main()
