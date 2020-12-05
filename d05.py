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


def seat_id(seat):
    row = bsp('F', seat[:7])
    col = bsp('L', seat[7:])
    return row * 8 + col


def high_seat_id(seats):
    return max(seat_id(seat) for seat in seats)


if __name__ == "__main__":
    solve(5, parse, high_seat_id)
