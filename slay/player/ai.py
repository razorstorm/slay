from __future__ import annotations

from typing import List, Any

from slay.player.base import Player
from slay.strategy.base import Strategy


class AI(Player):

    def __init__(self):
        self.strategy = None

    def take_turn(self, board: 'Board', screen: Any) -> List['Move']:
        self.strategy = Strategy(self, board)
        return self.strategy.take_turn()

    def draw(self, screen: Any):
        pass
