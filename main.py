import curses
from argparse import ArgumentParser
from curses import wrapper
from typing import Any

from slay.player.ai_player import AIPlayer
from slay.game import Game
from slay.player.human_player import HumanPlayer


def main(screen: Any, total_players: int, human_players: int):
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    ai_players = total_players - human_players
    players = [
        *[HumanPlayer() for _ in range(human_players)],
        *[AIPlayer() for _ in range(ai_players)],
    ]
    game = Game(players)
    while game.winner is None:
        game.next_turn()

    curses.endwin()


if __name__ == '__main__':
    parser = ArgumentParser(description="")
    parser.add_argument("--total_players", type=int, help="total number of players")
    parser.add_argument("--human_players", type=int, help="total number of human players")
    args = parser.parse_args()
    screen = curses.initscr()
    wrapper(main, screen, args.total_players, args.human_players)
