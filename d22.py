#!/usr/bin/env python

"""Advent of Code 2020, Day 22"""

from aoc import solve


def parse(data):
    return [[int(x) for x in part.split('\n')[1:]] for part in data.split('\n\n')]


def combat(decks, verbose=False):
    round = 1
    while all(len(deck) > 0 for deck in decks):
        if verbose:
            print(f"-- Round {round} --")
            print(f"Player 1's deck:", ', '.join(map(str, decks[0])))
            print(f"Player 2's deck:", ', '.join(map(str, decks[1])))
        plays = [deck.pop(0) for deck in decks]
        winner = max(enumerate(plays), key=lambda x: x[1])[0]
        if verbose:
            print(f"Player 1 plays: {plays[0]}")
            print(f"Player 2 plays: {plays[1]}")
            print(f"Player {winner+1} wins the round!")
            print()
        decks[winner].extend(sorted(plays, reverse=True))
        round += 1

    if verbose:
        print()
        print(f"== Post-game results ==")
        print(f"Player 1's deck:", ', '.join(map(str, decks[0])))
        print(f"Player 2's deck:", ', '.join(map(str, decks[1])))

    deck = max(decks, key=lambda x: len(x))
    deck.reverse()
    return sum((i+1)*x for i, x in enumerate(deck))


game_counter = 0


def recursive_combat(decks, verbose=False):
    global game_counter
    game_counter += 1
    game = game_counter
    if verbose:
        print(f"== Game {game} ==")

    round = 1
    seen = set()
    while all(len(deck) > 0 for deck in decks):
        if verbose:
            print()
            print(f"-- Round {round} (Game {game}) --")
            print(f"Player 1's deck:", ', '.join(map(str, decks[0])))
            print(f"Player 2's deck:", ', '.join(map(str, decks[1])))

        state = tuple(tuple(deck) for deck in decks)
        if state in seen:
            return 0
        seen.add(state)

        plays = [deck.pop(0) for deck in decks]
        if verbose:
            print(f"Player 1 plays: {plays[0]}")
            print(f"Player 2 plays: {plays[1]}")

        if all(play <= len(deck) for play, deck in zip(plays, decks)):
            if verbose:
                print("Playing a sub-game to determine the winner...")
                print()
            winner = recursive_combat([deck[:play] for play, deck in zip(plays, decks)], verbose=verbose)
            if verbose:
                print(f"...anyway, back to game {game}.")
        else:
            winner = max(enumerate(plays), key=lambda x: x[1])[0]

        if verbose:
            print(f"Player {winner+1} wins round {round} of game {game}!")

        decks[winner].append(plays[winner])
        decks[winner].append(plays[1 - winner])
        round += 1

    if verbose:
        print(f"The winner of game {game} is player {winner+1}!")
        print()

    if game == 1:
        if verbose:
            print()
            print(f"== Post-game results ==")
            print(f"Player 1's deck:", ', '.join(map(str, decks[0])))
            print(f"Player 2's deck:", ', '.join(map(str, decks[1])))
        deck = max(decks, key=lambda x: len(x))
        deck.reverse()
        return sum((i+1)*x for i, x in enumerate(deck))
    else:
        return winner


if __name__ == "__main__":
    solve(22, parse, combat, recursive_combat)
