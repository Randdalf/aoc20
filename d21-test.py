#!/usr/bin/env python

"""Advent of Code 2020, Day 21 (Unit Tests)"""

import unittest

from d21 import parse, num_inert, danger_list

example1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


class NumInertTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(num_inert(parse(example1)), 5)


class DangerListTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(danger_list(parse(example1)), 'mxmxvkd,sqjhc,fvjkl')


if __name__ == "__main__":
    unittest.main()
