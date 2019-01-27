from argparse import ArgumentParser
from curses import (noecho, cbreak, endwin, wrapper, start_color, use_default_colors)
from random import seed as random_seed, random
from typing import Any

from slay.game import Game
from slay.player.ai import AI
from slay.player.human import Human


def main(screen: Any, total_players: int, human_players: int, board_size: int, seed: int):
    noecho()
    cbreak()
    start_color()
    use_default_colors()
    screen.keypad(True)
    screen.border()

    random_seed(seed)

    ai_players = total_players - human_players
    players = [
        *[Human() for _ in range(human_players)],
        *[AI() for _ in range(ai_players)],
    ]
    game = Game(players, board_size, screen)
    while game.winner is None:
        game.next_turn()

    endwin()


if __name__ == '__main__':
    parser = ArgumentParser(description="")
    parser.add_argument(
        "--total_players",
        type=int,
        default=1,
        help="total number of players",
    )
    parser.add_argument(
        "--human_players",
        type=int,
        default=1,
        help="total number of human players",
    )
    parser.add_argument(
        "--board_size",
        type=int,
        default=10,
        help="N * N board size",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=random(),
        help="random.seed value (to get deterministic games)",
    )
    args = parser.parse_args()
    wrapper(main, args.total_players, args.human_players, args.board_size, args.seed)
