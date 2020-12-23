#!/usr/bin/env python

"""Advent of Code 2020, Day 23"""

from collections import deque

from aoc import solve


def parse(data):
    return [int(x) for x in data]


def print_cups(next, curr):
    print('cups: ', end='')
    cup = curr
    for i in range(len(next) - 1):
        if cup == curr:
            print(f'({cup})', end='')
        else:
            print(f' {cup} ', end='')
        cup = next[cup]
    print()


def simulate(cups, moves, verbose=False):
    # Store some basic parameters.
    lo = min(cups)
    hi = max(cups)
    n = len(cups)

    # Initialise circular linked list.
    prev = [None for i in range(n+1)]
    next = [None for i in range(n+1)]
    for i, cup in enumerate(cups):
        prev[cup] = cups[(i-1) % n]
        next[cup] = cups[(i+1) % n]

    # Play the game.
    head = cups[0]
    for move in range(moves):
        curr = head
        head = next[head]

        if verbose:
            print(f'-- move {move+1} --')
            print_cups(next, curr)

        # Pick up three cups clockwise.
        pickup = []
        for i in range(3):
            pick = head
            head = next[head]
            pick_next = next[pick]
            pick_prev = prev[pick]
            next[pick_prev] = pick_next
            prev[pick_next] = pick_prev
            prev[pick] = None
            next[pick] = None
            pickup.append(pick)

        # Select a destination cup.
        dest = hi if curr == lo else curr - 1
        while dest in pickup:
            dest = hi if dest == lo else dest - 1

        if verbose:
            print('pick up:', ', '.join(map(str, pickup)))
            print('destination:', dest)
            print()

        # Place the picked up cups clockwise of the destination cup.
        for cup in pickup:
            dest_next = next[dest]
            prev[cup] = dest
            next[cup] = dest_next
            next[dest] = cup
            prev[dest_next] = cup
            dest = cup

    if verbose:
        print('-- final --')
        print_cups(next, head)

    return next


def crab_cups_100(cups):
    next = simulate(cups, 100)
    result = ''
    cup = next[1]
    for i in range(len(cups)-1):
        result += str(cup)
        cup = next[cup]
    return result


def crab_cups_10m(cups):
    cups.extend(range(max(cups)+1, 1000001))
    next = simulate(cups, 10000000)
    return next[1] * next[next[1]]


if __name__ == "__main__":
    solve(23, parse, crab_cups_100, crab_cups_10m)
