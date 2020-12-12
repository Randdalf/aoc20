#!/usr/bin/env python

"""Advent of Code 2020, Day 12 (Unit Tests)"""

import unittest

from d12 import parse, navigate

example1 = """F10
N3
F7
R90
F11"""


class NavigateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(navigate(parse(example1)), 25)


if __name__ == "__main__":
    unittest.main()
