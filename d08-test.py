#!/usr/bin/env python

"""Advent of Code 2020, Day 8 (Unit Tests)"""

import unittest

from d08 import parse, exec, repair

example1 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class ExecTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(exec(parse(example1)), 5)


class RepairTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(repair(parse(example1)), 8)


if __name__ == "__main__":
    unittest.main()
