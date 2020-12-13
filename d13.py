#!/usr/bin/env python

"""Advent of Code 2020, Day 13"""

from aoc import solve


class Notes:
    def __init__(slf, data):
        lines = data.split('\n')
        slf.timestamp = int(lines[0])
        slf.bus_ids = [int(x) for x in lines[1].split(',') if x != 'x']


def parse(data):
    return Notes(data)


def earliest_bus(notes):
    bus = min(
        ((id - notes.timestamp % id, id) for id in notes.bus_ids),
        key=lambda x: x[0]
    )
    return bus[0] * bus[1]


if __name__ == "__main__":
    solve(13, parse, earliest_bus)
