from argparse import ArgumentParser
from typing import Any

from slay.ai_player import AIPlayer
from slay.board import Board
from slay.game import Game
from slay.human_player import HumanPlayer
import curses
from curses import wrapper


def main(screen: Any, total_players: int, human_players: int, ai_difficulty: int):
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    ai_players = total_players - human_players
    players = [
        *[HumanPlayer() for human in range(human_players)],
        *[AIPlayer(ai_difficulty) for ai in range(ai_players)],
    ]
    game = Game(players)
    while game.winner is None:
        game.next_turn()

    curses.endwin()


if __name__ == '__main__':
    parser = ArgumentParser(description="")
    parser.add_argument("--total_players", type=int, help="total number of players")
    parser.add_argument("--human_players", type=int, help="total number of human players")
    parser.add_argument("--ai_difficulty", type=int, help="ai difficulty (from 1 to 4, default: 1)")
    args = parser.parse_args()
    screen = curses.initscr()
    wrapper(main, screen, args.total_players, args.human_players, args.ai_difficulty)
