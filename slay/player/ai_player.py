from typing import List

from slay.ai.ai import AI
from slay.board import Board
from slay.move import Move
from slay.player import Player


class AIPlayer(Player):

    def __init__(self):
        self.ai = None

    def take_turn(self, board: Board) -> List[Move]:
        self.ai = AI(self)
        return self.ai.take_turn()
