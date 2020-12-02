#!/usr/bin/env python

"""Advent of Code 2020, Day 2 (Unit Tests)"""

import unittest

from d02 import parse, num_valid_passwords_right, num_valid_passwords_wrong

example1 = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


class NumValidPasswordsWrong(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(num_valid_passwords_wrong(parse(example1)), 2)


class NumValidPasswordsRight(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(num_valid_passwords_right(parse(example1)), 1)


if __name__ == "__main__":
    unittest.main()
