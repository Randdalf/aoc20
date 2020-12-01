#!/usr/bin/env python

"""Generate a skeleton program for Advent of Code"""

import datetime
import pathlib


solution_template = '''#!/usr/bin/env python

"""Advent of Code {year}, Day {day}"""

from aoc import solve


def parse(data):
    pass


if __name__ == "__main__":
    solve({day}, parse)'''


test_template = '''#!/usr/bin/env python

"""Advent of Code {year}, Day {day} (Unit Tests)"""

import unittest


class SolverTests(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
'''


def write_skeleton(day, year, template, filename_format):
    skeleton = template.format(day=day, year=year)
    filename = filename_format.format(day=day, year=year)
    if not pathlib.Path(filename).exists():
        with open(filename, 'w+') as file:
            file.write(skeleton)
            print(f'Created {filename}')
    else:
        print(f'{filename} already exists')


def main():
    now = datetime.datetime.now()
    write_skeleton(now.day, now.year, solution_template, 'd{day:02d}.py')
    write_skeleton(now.day, now.year, test_template, 'd{day:02d}-test.py')


if __name__ == "__main__":
    main()
