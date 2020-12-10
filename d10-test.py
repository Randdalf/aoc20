#!/usr/bin/env python

"""Advent of Code 2020, Day 10 (Unit Tests)"""

import unittest

from d10 import parse, jolt_diffs

example1 = """16
10
15
5
1
11
7
19
6
12
4"""

example2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


class JoltDiffsTest(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(jolt_diffs(parse(example1)), 35)

    def test_example2(slf):
        slf.assertEqual(jolt_diffs(parse(example2)), 220)


if __name__ == "__main__":
    unittest.main()
