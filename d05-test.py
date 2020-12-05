#!/usr/bin/env python

"""Advent of Code 2020, Day 5 (Unit Tests)"""

import unittest

from d05 import seat_id, seat_coord


class SeatIdTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(seat_id(*seat_coord('FBFBBFFRLR')), 357)

    def test_example2(slf):
        slf.assertEqual(seat_id(*seat_coord('BFFFBBFRRR')), 567)

    def test_example3(slf):
        slf.assertEqual(seat_id(*seat_coord('FFFBBBFRRR')), 119)

    def test_example4(slf):
        slf.assertEqual(seat_id(*seat_coord('BBFFBBFRLL')), 820)


if __name__ == "__main__":
    unittest.main()
