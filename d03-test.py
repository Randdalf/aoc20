#!/usr/bin/env python

"""Advent of Code 2020, Day 3 (Unit Tests)"""

import unittest

from d03 import parse, count_trees

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


if __name__ == "__main__":
    unittest.main()
