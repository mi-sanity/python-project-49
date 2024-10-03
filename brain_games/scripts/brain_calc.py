#!/usr/bin/env python3

from brain_games.games import calc
from brain_games import game_engine


def main():
    game_engine.start_game(calc)


if __name__ == '__main__':
    main()
