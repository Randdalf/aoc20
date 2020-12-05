#!/usr/bin/env python

"""Advent of Code 2020, Day 5"""

from aoc import solve


def parse(data):
    yield from data.split('\n')


def bsp(d0, d1, s):
    return int(s.replace(d0, '0').replace(d1, '1'), 2)


def seat_coord(seat):
    return (bsp('F', 'B', seat[:7]), bsp('L', 'R', seat[7:]))


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
