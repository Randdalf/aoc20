#!/usr/bin/env python

"""Advent of Code 2020, Day 23 (Unit Tests)"""

import unittest

from d23 import parse, crab_cups_100, crab_cups_10m


class CrabCups100Tests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(crab_cups_100(parse('389125467')), '67384529')


class CrabCups10mTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(crab_cups_10m(parse('389125467')), 149245887792)


if __name__ == "__main__":
    unittest.main()
