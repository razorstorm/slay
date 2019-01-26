from __future__ import annotations

from typing import List, Any

from slay.player.base import Player


class Nature(Player):

    def take_turn(self, board: 'Board', screen: Any) -> List['Move']:
        pass

    def draw(self, screen: Any):
        pass
