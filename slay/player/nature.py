from typing import List, Any

from slay.board import Board
from slay.move import Move
from slay.player import Player


class Nature(Player):

    def take_turn(self, board: Board, screen: Any) -> List[Move]:
        pass

    def draw(self, screen: Any):
        pass
