#!/usr/bin/env python

"""Advent of Code 2020, Day 24 (Unit Tests)"""

import unittest

from d24 import parse, flip_tiles, art_exhibit

example1 = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""


class FlipTilesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(flip_tiles(parse(example1)), 10)


class ArtExhibitTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(art_exhibit(parse(example1)), 2208)


if __name__ == "__main__":
    unittest.main()
