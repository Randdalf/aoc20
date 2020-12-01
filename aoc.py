#!/usr/bin/env python

"""Advent of Code 2020"""

import aocd
from time import perf_counter


def run_solver(day, level, solver, input):
    start = perf_counter()
    answer = solver(input)
    end = perf_counter()
    print(f'{answer:<30} ({end - start:.4f}s)')


def solve(day, parse, *solvers):
    data = aocd.get_data(day=day, year=2020)
    for i, solver in enumerate(solvers):
        run_solver(day, i+1, solver, parse(data))
