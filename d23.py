#!/usr/bin/env python

"""Advent of Code 2020, Day 23"""

from aoc import solve


def parse(data):
    return [int(x) for x in data]


def print_cups(cups, curr):
    print('cups: ', end='')
    for cup in cups:
        if cup == curr:
            print(f'({cup})', end='')
        else:
            print(f' {cup} ', end='')
    print()


def crab_cups(cups, moves=100, verbose=False):
    lo = min(cups)
    hi = max(cups)
    n = len(cups)
    curr = cups[0]
    for move in range(moves):
        if verbose:
            print(f'-- move {move+1} --')
            print_cups(cups, curr)
        pickup = [cups.pop((cups.index(curr)+1) % len(cups)) for i in range(3)]
        dest = curr
        while dest in pickup or dest == curr:
            dest = hi if dest == lo else dest - 1
        if verbose:
            print('pick up:', ', '.join(map(str, pickup)))
            print('destination:', dest)
            print()
        dest_idx = cups.index(dest) + 1
        cups = cups[:dest_idx] + pickup + cups[dest_idx:]
        curr = cups[(cups.index(curr) + 1) % n]
    if verbose:
        print('-- final --')
        print_cups(cups, curr)
    start = (cups.index(1) + 1) % n
    return ''.join(str(cups[(start+i) % n]) for i in range(n-1))


if __name__ == "__main__":
    solve(23, parse, crab_cups)
