#!/usr/bin/env python

"""Advent of Code 2020, Day 8"""

from aoc import solve


def parse(data):
    return [line.split(' ') for line in data.split('\n')]


class BadTerminationError(Exception):
    pass


def exec(prog, error=False):
    acc = 0
    pc = 0
    visited = set()
    while pc not in visited and pc < len(prog):
        visited.add(pc)
        instr, val = prog[pc]
        if instr == 'acc':
            acc += int(val)
            pc += 1
        elif instr == 'jmp':
            pc += int(val)
        else:
            pc += 1
    if error and (pc in visited or pc > len(prog)):
        raise BadTerminationError()
    return acc


def repair(prog):
    for pc, (instr, val) in enumerate(prog):
        if instr == 'nop':
            prog[pc] = ('jmp', val)
        elif instr == 'jmp':
            prog[pc] = ('nop', val)
        try:
            return exec(prog, True)
        except BadTerminationError:
            prog[pc] = (instr, val)


if __name__ == "__main__":
    solve(8, parse, exec, repair)
