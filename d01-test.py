#!/usr/bin/env python

"""Advent of Code 2020, Day 1 (Unit Tests)"""

import unittest

from d01 import find_sum_2020

example1 = [1721, 979, 366, 299, 675, 1456]


class FindSum2020Tests(unittest.TestCase):
    def test_example1_2(slf):
        slf.assertEqual(
            find_sum_2020(example1, 2),
            514579
        )

    def test_example2_3(slf):
        slf.assertEqual(
            find_sum_2020(example1, 3),
            241861950
        )


if __name__ == "__main__":
    unittest.main()
