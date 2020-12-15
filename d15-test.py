#!/usr/bin/env python

"""Advent of Code 2020, Day 15 (Unit Tests)"""

import unittest

from d15 import parse, memory_game


class MemoryGameTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(memory_game([0, 3, 6]), 436)

    def test_example2(slf):
        slf.assertEqual(memory_game([1, 3, 2]), 1)

    def test_example3(slf):
        slf.assertEqual(memory_game([2, 1, 3]), 10)

    def test_example4(slf):
        slf.assertEqual(memory_game([1, 2, 3]), 27)

    def test_example5(slf):
        slf.assertEqual(memory_game([2, 3, 1]), 78)

    def test_example6(slf):
        slf.assertEqual(memory_game([3, 2, 1]), 438)

    def test_example7(slf):
        slf.assertEqual(memory_game([3, 1, 2]), 1836)


if __name__ == "__main__":
    unittest.main()
