#!/usr/bin/env python

"""Advent of Code 2020, Day 12"""

from aoc import solve

from vec2 import Vec2, manhattan


class Ship1:
    def __init__(slf):
        slf.pos = Vec2(0, 0)
        slf.dir = Vec2(1, 0)

    def N(slf, value):
        slf.pos += Vec2(0, -value)

    def S(slf, value):
        slf.pos += Vec2(0, value)

    def E(slf, value):
        slf.pos += Vec2(value, 0)

    def W(slf, value):
        slf.pos += Vec2(-value, 0)

    def L(slf, value):
        for i in range(value//90):
            slf.dir = slf.dir.rot90left()

    def R(slf, value):
        for i in range(value//90):
            slf.dir = slf.dir.rot90right()

    def F(slf, value):
        slf.pos += value * slf.dir


class Ship2:
    def __init__(slf):
        slf.pos = Vec2(0, 0)
        slf.waypoint = Vec2(10, -1)

    def N(slf, value):
        slf.waypoint += Vec2(0, -value)

    def S(slf, value):
        slf.waypoint += Vec2(0, value)

    def E(slf, value):
        slf.waypoint += Vec2(value, 0)

    def W(slf, value):
        slf.waypoint += Vec2(-value, 0)

    def L(slf, value):
        for i in range(value//90):
            slf.waypoint = slf.waypoint.rot90left()

    def R(slf, value):
        for i in range(value//90):
            slf.waypoint = slf.waypoint.rot90right()

    def F(slf, value):
        slf.pos += value * slf.waypoint


def parse(data):
    return [(instr[0], int(instr[1:])) for instr in data.split('\n')]


def navigate(ship, instrs):
    for action, value in instrs:
        getattr(ship, action)(value)
    return manhattan(ship.pos, Vec2(0, 0))


def navigate1(instrs):
    return navigate(Ship1(), instrs)


def navigate2(instrs):
    return navigate(Ship2(), instrs)


if __name__ == "__main__":
    solve(12, parse, navigate1, navigate2)
