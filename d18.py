#!/usr/bin/env python

"""Advent of Code 2020, Day 18"""

from operator import mul, add

from aoc import solve


def parse(data):
    return [list(line.replace(' ', '')) for line in data.split('\n')]


def eval(expr):
    n = []
    op = None
    while expr:
        c = expr.pop(0)
        if c == '(':
            n.append(eval(expr))
        elif c == ')':
            break
        elif c == '*':
            op = mul
        elif c == '+':
            op = add
        else:
            n.append(ord(c) - ord('0'))
        if op and len(n) > 1:
            n.append(op(n.pop(), n.pop()))
    return n[0]


def evaluate(exprs):
    return sum(eval(x) for x in exprs)


if __name__ == "__main__":
    solve(18, parse, evaluate)
