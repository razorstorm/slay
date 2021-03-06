from __future__ import annotations

from copy import deepcopy
from typing import List

from slay.tile import Tile


# this only works for 1 turn, instantiate again each time need to use a lil
class Strategy(object):

    def __init__(self, player: 'AI', board: 'Board'):
        # FIXME: this has a bug because now `self.player not in self.board.players`
        # the references are different even though they have the same values
        self.player = deepcopy(player)
        self.board = deepcopy(board)
        self.territories = board.territories_by_player[player]

    def take_turn(self) -> List['Move']:
        results = []
        for territory in self.territories:
            # FIXME: the number of that player's territories can change when this function completes
            results += self._make_moves_for_territory(territory)
        return results

    def _make_moves_for_territory(self, territory: 'Territory') -> List['Move']:
        moves = list()
        moveable_units = [unit for unit in territory.units if unit.has_turn]
        # FIXME: there is a case where combining territories gives this territory more money
        # the AI should spend that money on units
        while territory.can_buy_unit:
            # FIXME: find the location before buying a unit
            location = Tile()
            moveable_units.append(territory.buy_unit(location))

        while moveable_units:
            unit = moveable_units.pop()
            moves.append(self._move(unit))
        return moves

    def _move(self, unit: 'Unit') -> 'Move':
        pass
