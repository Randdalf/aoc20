#!/usr/bin/env python

"""Advent of Code 2020, Day 12 (Unit Tests)"""

import unittest

from d12 import parse, navigate1, navigate2

example1 = """F10
N3
F7
R90
F11"""


class Navigate1Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(navigate1(parse(example1)), 25)


class Navigate2Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(navigate2(parse(example1)), 286)


if __name__ == "__main__":
    unittest.main()
