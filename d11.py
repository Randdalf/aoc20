#!/usr/bin/env python

"""Advent of Code 2020, Day 11"""

from aoc import solve
from vec2 import Vec2

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'


class SeatLayout:
    def __init__(slf, seats={}, data=''):
        slf.seats = seats
        for y, row in enumerate(data.split('\n')):
            for x, col in enumerate(row):
                slf.seats[Vec2(x, y)] = col

    def __eq__(slf, otr):
        return slf.seats == otr.seats

    def adjacencies(slf, pos):
        for x in [-1, 0, +1]:
            for y in [-1, 0, +1]:
                adj = pos + Vec2(x, y)
                if adj != pos and adj in slf.seats:
                    yield slf.seats[adj]

    def step(slf):
        new_seats = {}
        for pos, seat in slf.seats.items():
            adjacencies = list(slf.adjacencies(pos))
            if seat == EMPTY_SEAT and adjacencies.count(OCCUPIED_SEAT) == 0:
                seat = OCCUPIED_SEAT
            elif seat == OCCUPIED_SEAT and adjacencies.count(OCCUPIED_SEAT) >= 4:
                seat = EMPTY_SEAT
            new_seats[pos] = seat
        return SeatLayout(seats=new_seats)


def parse(data):
    return SeatLayout(data=data)


def occupied_seats(layout):
    while True:
        new = layout.step()
        if new == layout:
            return list(layout.seats.values()).count(OCCUPIED_SEAT)
        layout = new


if __name__ == "__main__":
    solve(11, parse, occupied_seats)
