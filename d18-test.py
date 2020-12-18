#!/usr/bin/env python

"""Advent of Code 2020, Day 18 (Unit Tests)"""

import unittest

from d18 import parse, part1, part2

example1 = "1 + 2 * 3 + 4 * 5 + 6"
example2 = "1 + (2 * 3) + (4 * (5 + 6))"
example3 = "2 * 3 + (4 * 5)"
example4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
example5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
example6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


class Part1Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(part1(parse(example1)), 71)

    def test_example2(slf):
        slf.assertEqual(part1(parse(example2)), 51)

    def test_example3(slf):
        slf.assertEqual(part1(parse(example3)), 26)

    def test_example4(slf):
        slf.assertEqual(part1(parse(example4)), 437)

    def test_example5(slf):
        slf.assertEqual(part1(parse(example5)), 12240)

    def test_example6(slf):
        slf.assertEqual(part1(parse(example6)), 13632)


class Part2Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(part2(parse(example1)), 231)

    def test_example2(slf):
        slf.assertEqual(part2(parse(example2)), 51)

    def test_example3(slf):
        slf.assertEqual(part2(parse(example3)), 46)

    def test_example4(slf):
        slf.assertEqual(part2(parse(example4)), 1445)

    def test_example5(slf):
        slf.assertEqual(part2(parse(example5)), 669060)

    def test_example6(slf):
        slf.assertEqual(part2(parse(example6)), 23340)


if __name__ == "__main__":
    unittest.main()
