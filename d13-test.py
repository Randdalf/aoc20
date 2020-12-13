#!/usr/bin/env python

"""Advent of Code 2020, Day 13 (Unit Tests)"""

import unittest

from d13 import parse, earliest_bus

example1 = """939
7,13,x,x,59,x,31,19"""


class EarliestBusTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(earliest_bus(parse(example1)), 295)


if __name__ == "__main__":
    unittest.main()
