#!/usr/bin/env python

"""Advent of Code 2020, Day 14 (Unit Tests)"""

import unittest

from d14 import parse, initialize, initialize_v2

example1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

example2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


class InitializeTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(initialize(parse(example1)), 165)


class InitializeV2Tests(unittest.TestCase):
    def test_example2(slf):
        slf.assertEqual(initialize_v2(parse(example2)), 208)


if __name__ == "__main__":
    unittest.main()
