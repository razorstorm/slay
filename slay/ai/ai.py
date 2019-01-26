from copy import deepcopy
from typing import List

from slay.entity.unit import Unit

from slay.board import Board
from slay.move import Move
from slay.player.ai_player import AIPlayer
from slay.territory import Territory


# this only works for 1 turn, instantiate again each time need to use a lil
class AI(object):

    def __init__(self, player: AIPlayer, board: Board):
        # FIXME: this has a bug because now `self.player not in self.board.players`
        # the references are different even though they have the same values
        self.player = deepcopy(player)
        self.board = deepcopy(board)
        self.territories = [territory for territory in self.board.territories if territory.owner == self.player]

    def take_turn(self) -> List[Move]:
        results = []
        for territory in self.territories:

            # FIXME: the number of that player's territories can change when this function completes
            results += self._make_moves_for_territory(territory)
        return results

    def _make_moves_for_territory(self, territory: Territory) -> List[Move]:
        moves = list()
        moveable_units = [unit for unit in territory.units if unit.has_turn]

        # FIXME: there is a case where combining territories gives this territory more money
        # the AI should spend that money on units
        while territory.can_buy_unit:
            moveable_units.append(territory.buy_unit())

        while moveable_units:
            unit = moveable_units.pop()
            moves.append(self._move(unit))
        return moves

    def _move(self, unit: Unit) -> Move:
        pass
