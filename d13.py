#!/usr/bin/env python

"""Advent of Code 2020, Day 13"""

from functools import reduce
from operator import mul

from aoc import solve


class Notes:
    def __init__(slf, data):
        lines = data.split('\n')
        slf.timestamp = int(lines[0])
        slf.buses = [
            (i, int(id)) for i, id in enumerate(lines[1].split(','))
            if id != 'x'
        ]


def parse(data):
    return Notes(data)


def earliest_bus(notes):
    bus = min(
        ((id - notes.timestamp % id, id) for off, id in notes.buses),
        key=lambda x: x[0]
    )
    return bus[0] * bus[1]


def contest(notes):
    step = t = 1
    for n in range(0, len(notes.buses)):
        while not all((t + off) % id == 0 for off, id in notes.buses[:n+1]):
            t += step
        step *= notes.buses[n][1]
    return t


if __name__ == "__main__":
    solve(13, parse, earliest_bus, contest)
