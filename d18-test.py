#!/usr/bin/env python

"""Advent of Code 2020, Day 18 (Unit Tests)"""

import unittest

from d18 import parse, evaluate

example1 = "1 + 2 * 3 + 4 * 5 + 6"
example2 = "1 + (2 * 3) + (4 * (5 + 6))"
example3 = "2 * 3 + (4 * 5)"
example4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
example5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
example6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


class EvaluateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(evaluate(parse(example1)), 71)

    def test_example2(slf):
        slf.assertEqual(evaluate(parse(example2)), 51)
    
    def test_example3(slf):
        slf.assertEqual(evaluate(parse(example3)), 26)

    def test_example4(slf):
        slf.assertEqual(evaluate(parse(example4)), 437)

    def test_example5(slf):
        slf.assertEqual(evaluate(parse(example5)), 12240)

    def test_example6(slf):
        slf.assertEqual(evaluate(parse(example6)), 13632)


if __name__ == "__main__":
    unittest.main()
