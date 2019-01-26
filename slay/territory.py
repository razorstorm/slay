from __future__ import annotations

from typing import List, Optional

from slay.entity.structure.village import Village
from slay.entity.unit import Unit
from slay.player import Player
from slay.rank import Rank
from slay.tile import Tile


class Territory(object):

    def __init__(self, owner: Player, tiles: List[Tile], village: Village):
        self.owner = owner
        self.tiles = tiles
        self.units = [tile.occupant for tile in self.tiles if tile.occupant is not None]
        self.income = 0
        self.wages = 0
        self.savings = 0
        self.village = village

    def __add__(self, other: Territory) -> Optional[Territory]:
        pass

    @property
    def can_buy_unit(self) -> bool:
        return self.savings >= Unit.cost

    def buy_unit(self, location: Tile) -> Unit:
        self.savings -= Unit.cost
        return Unit(location, self.owner, Rank.PEASANT, has_move=True)
