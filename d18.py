#!/usr/bin/env python

"""Advent of Code 2020, Day 18"""

from aoc import solve


def parse(data):
    return data.split('\n')


def shunting_yard(expr, prec):
    q = []
    ops = []
    for c in expr:
        if '1' <= c <= '9':
            q.append(ord(c) - ord('0'))
        elif c in prec:
            while ops and ops[-1] != '(' and prec[ops[-1]] >= prec[c]:
                q.append(ops.pop())
            ops.append(c)
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops[-1] != '(':
                q.append(ops.pop())
            ops.pop()
    while ops:
        q.append(ops.pop())
    return q


def eval(q):
    n = []
    for c in q:
        if c == '+':
            n.append(n.pop() + n.pop())
        elif c == '*':
            n.append(n.pop() * n.pop())
        else:
            n.append(c)
    return n[0]


def sum_eval(exprs, prec):
    return sum(eval(shunting_yard(x, prec)) for x in exprs)


def part1(exprs):
    return sum_eval(exprs, prec={'+': 0, '*': 0})


def part2(exprs):
    return sum_eval(exprs, prec={'+': 1, '*': 0})


if __name__ == "__main__":
    solve(18, parse, part1, part2)
