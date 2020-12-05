#!/usr/bin/env python

"""Advent of Code 2020, Day 5"""

from aoc import solve


def parse(data):
    yield from data.split('\n')


def bsp(left, s):
    lo = 0
    hi = (2 << (len(s) - 1)) - 1
    for c in s:
        mid = (lo + hi) // 2
        if c == left:
            hi = mid
        else:
            lo = mid + 1
    return min(lo, hi)


def seat_coord(seat):
    return (bsp('F', seat[:7]), bsp('L', seat[7:]))


def seat_id(row, col):
    return row * 8 + col


def high_seat_id(seats):
    return max(seat_id(*seat_coord(seat)) for seat in seats)


def find_my_seat(seats):
    filled = set(seat_coord(seat) for seat in seats)
    for row in range(9, 120):
        for col in range(8):
            if (row, col) not in filled:
                return seat_id(row, col)


if __name__ == "__main__":
    solve(5, parse, high_seat_id, find_my_seat)
