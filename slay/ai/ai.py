from typing import List

from slay.ai_player import AIPlayer
from slay.entities.unit import Unit
from slay.territory import Territory


# this only works for 1 turn, instantiate again each time need to use a lil
from slay.tile import Tile


class AI(object):
    def __init__(self, player: AIPlayer):
        self.player = player.deepcopy()
        self.board = self.player.board
        self.territories = self.player.territories

    def make_moves(self) -> List(Move):
        results = []
        for territory in self.territories:
            results += self._make_moves_for_territory(territory)

    def _make_moves_for_territory(self, territory: Territory) -> List(Move):
        moveable_units = [unit for unit in territory.units if unit.has_turn]
        while can_buy_unit():
            moveable_units.append(buy_unit())

        while moveable_units:
            unit = moveable_units.pop()
            _do_turn(unit)

    def _do_turn(self, unit: Unit) -> Tile:
        pass
