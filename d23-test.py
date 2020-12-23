#!/usr/bin/env python

"""Advent of Code 2020, Day 23 (Unit Tests)"""

import unittest

from d23 import parse, crab_cups


class SolverTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(crab_cups(parse('389125467')), '67384529')


if __name__ == "__main__":
    unittest.main()
