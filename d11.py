#!/usr/bin/env python

"""Advent of Code 2020, Day 11"""

from itertools import product

from aoc import solve
from vec2 import Vec2

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'

dirs = [
    Vec2(-1, -1),
    Vec2(-1, 0),
    Vec2(-1, +1),
    Vec2(0, -1),
    Vec2(0, +1),
    Vec2(+1, -1),
    Vec2(+1, 0),
    Vec2(+1, +1)
]


class SeatLayout:
    def __init__(slf, seats={}, data=''):
        slf.seats = seats
        for y, row in enumerate(data.split('\n')):
            for x, col in enumerate(row):
                slf.seats[Vec2(x, y)] = col

    def __eq__(slf, otr):
        return slf.seats == otr.seats

    def adjacencies(slf, pos):
        return [
            slf.seats[pos + dir] for dir in dirs if (pos + dir) in slf.seats
        ]

    def step1(slf):
        changed = False
        new_seats = {}
        for pos, seat in slf.seats.items():
            adjacencies = slf.adjacencies(pos)
            if seat == EMPTY_SEAT and adjacencies.count(OCCUPIED_SEAT) == 0:
                seat = OCCUPIED_SEAT
                changed = True
            elif seat == OCCUPIED_SEAT and adjacencies.count(OCCUPIED_SEAT) >= 4:
                seat = EMPTY_SEAT
                changed = True
            new_seats[pos] = seat
        slf.seats = new_seats
        return changed

    def vision(slf, pos):
        for dir in dirs:
            test = pos + dir
            while test in slf.seats and slf.seats[test] == FLOOR:
                test += dir
            if test in slf.seats:
                yield slf.seats[test]

    def step2(slf):
        changed = False
        new_seats = {}
        for pos, seat in slf.seats.items():
            vision = list(slf.vision(pos))
            if seat == EMPTY_SEAT and vision.count(OCCUPIED_SEAT) == 0:
                seat = OCCUPIED_SEAT
                changed = True
            elif seat == OCCUPIED_SEAT and vision.count(OCCUPIED_SEAT) >= 5:
                seat = EMPTY_SEAT
                changed = True
            new_seats[pos] = seat
        slf.seats = new_seats
        return changed

    def occupied(slf):
        return list(slf.seats.values()).count(OCCUPIED_SEAT)


def parse(data):
    return SeatLayout(data=data)


def occupied_seats1(layout):
    while layout.step1():
        pass
    return layout.occupied()


def occupied_seats2(layout):
    while layout.step2():
        pass
    return layout.occupied()


if __name__ == "__main__":
    solve(11, parse, occupied_seats1, occupied_seats2)
