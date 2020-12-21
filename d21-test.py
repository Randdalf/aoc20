#!/usr/bin/env python

"""Advent of Code 2020, Day 21 (Unit Tests)"""

import unittest

from d21 import parse, no_allergens

example1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


class NoAllergensTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(no_allergens(parse(example1)), 5)


if __name__ == "__main__":
    unittest.main()
