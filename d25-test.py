#!/usr/bin/env python

"""Advent of Code 2020, Day 25 (Unit Tests)"""

import unittest

from d25 import parse, encryption_key


class EncryptionKeyTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(encryption_key([5764801, 17807724]), 14897079)


if __name__ == "__main__":
    unittest.main()
