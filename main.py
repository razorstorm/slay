from argparse import ArgumentParser
from curses import (noecho, cbreak, endwin, wrapper)
from typing import Any

from slay.game import Game
from slay.player.ai import AI
from slay.player.human import Human


def main(screen: Any, total_players: int, human_players: int):
    noecho()
    cbreak()
    screen.keypad(True)

    ai_players = total_players - human_players
    players = [
        *[Human() for _ in range(human_players)],
        *[AI() for _ in range(ai_players)],
    ]
    game = Game(players)
    while game.winner is None:
        game.next_turn()
        game.board.draw(screen)

    endwin()


if __name__ == '__main__':
    parser = ArgumentParser(description="")
    parser.add_argument("--total_players", type=int, help="total number of players")
    parser.add_argument("--human_players", type=int, help="total number of human players")
    args = parser.parse_args()
    wrapper(main, args.total_players, args.human_players)
