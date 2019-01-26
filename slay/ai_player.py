from typing import List

from slay.ai.ai import AI
from slay.move import Move
from slay.player import Player


class AIPlayer(Player):

    def __init__(self, board):
        super().__init__(board)
        self.ai = None

    def make_moves(self) -> List[Move]:
        self.ai = AI(self)
        return self.ai.make_moves()
