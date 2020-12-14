#!/usr/bin/env python

"""Advent of Code 2020, Day 14"""

from collections import defaultdict
import re

from aoc import solve


def parse(data):
    mask_pattern = re.compile(r'^mask = ([10X]+)$')
    mem_pattern = re.compile(r'^mem\[(\d+)\] = (\d+)$')
    program = []
    for line in data.split('\n'):
        mask_match = mask_pattern.match(line)
        mem_match = mem_pattern.match(line)
        if mask_match:
            program.append(('mask', mask_match.group(1)))
        elif mem_match:
            program.append((int(mem_match.group(1)), int(mem_match.group(2))))
    return program


def initialize(program):
    mem = defaultdict(int)
    for a, b in program:
        if a == 'mask':
            mask_out = int(b.replace('1', '0').replace('X', '1'), 2)
            mask_in = int(b.replace('X', '0'), 2)
        else:
            mem[a] = (b & mask_out) | mask_in
    return sum(mem.values())


def initialize_v2(program):
    mem = defaultdict(int)
    for a, b in program:
        if a == 'mask':
            c = b.count('X')
            mask_in = int(b.replace('X', '0'), 2)
            masks = []
            for n in range(1 << b.count('X')):
                mask = b.replace('1', '0')
                for bit in f'{n:0{c}b}':
                    mask = mask.replace('X', bit, 1)
                masks.append(int(mask, 2) | mask_in)
        else:
            for mask in masks:
                mem[(a & ~masks[-1]) | mask] = b
    return sum(mem.values())


if __name__ == "__main__":
    solve(14, parse, initialize, initialize_v2)
