#!/usr/bin/env python

"""Advent of Code 2020, Day 12"""

from aoc import solve

from vec2 import Vec2

dirs = [Vec2(1, 0), Vec2(0, 1), Vec2(-1, 0), Vec2(0, -1)]


def turn(dir, n):
    return dirs[(dirs.index(dir) + n) % len(dirs)]


class Ferry:
    def __init__(slf):
        slf.pos = Vec2(0, 0)
        slf.dir = Vec2(1, 0)

    def navigate(slf, instrs):
        for action, value in instrs:
            getattr(slf, action)(value)

    def dist(slf):
        return abs(slf.pos.x) + abs(slf.pos.y)

    def N(slf, value):
        slf.pos += Vec2(0, -value)

    def S(slf, value):
        slf.pos += Vec2(0, value)

    def E(slf, value):
        slf.pos += Vec2(value, 0)

    def W(slf, value):
        slf.pos += Vec2(-value, 0)

    def L(slf, value):
        slf.dir = turn(slf.dir, -value//90)

    def R(slf, value):
        slf.dir = turn(slf.dir, value//90)

    def F(slf, value):
        slf.pos += Vec2(value*slf.dir.x, value*slf.dir.y)


def parse(data):
    return [(instr[0], int(instr[1:])) for instr in data.split('\n')]


def navigate(instrs):
    ferry = Ferry()
    ferry.navigate(instrs)
    return ferry.dist()


if __name__ == "__main__":
    solve(12, parse, navigate)
