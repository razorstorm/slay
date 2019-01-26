from argparse import ArgumentParser

from slay.ai_player import AIPlayer
from slay.board import Board
from slay.human_player import HumanPlayer


def main(total_players: int, human_players: int, ai_difficulty: int):
    ai_players = total_players - human_players
    players = [
        *[HumanPlayer() for human in range(human_players)],
        *[AIPlayer() for ai in range(ai_players)]
    ]
    board = Board(players)
    while board.winner is None:
        board.play()


if __name__ == '__main__':
    parser = ArgumentParser(description="")
    parser.add_argument("--total_players", type=int, help="total number of players")
    parser.add_argument("--human_players", type=int, help="total number of human players")
    parser.add_argument("--ai_difficulty", type=int, help="ai difficulty (from 1 to 4, default: 1)")
    args = parser.parse_args()
    main(args.total_players, args.human_players, args.ai_difficulty)
