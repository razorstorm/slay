from __future__ import annotations

from typing import Optional, Any

from slay.entity import Entity
from slay.move import Move
from slay.rank import Rank
from slay.territory import Territory
from slay.tile import Tile


class Unit(Entity):

    cost = 10

    def __init__(self, location: Tile, territory: Territory, rank: Rank, has_move: bool):
        super().__init__(location, territory)
        self.rank = rank
        self.has_move = has_move

    @property
    def upkeep(self):
        return self.rank.upkeep

    def __add__(self, other: Unit) -> Optional[Unit]:
        if (self.rank + other.rank).value > 4 or self.territory != other.territory:
            return None
        return Unit(self.location, self.owner, self.rank + other.rank, self.has_move and other.has_move)

    def is_valid_move(self, new_location: Tile) -> bool:
        pass

    def move(self, new_location: Tile) -> Optional[Move]:
        pass

    def draw(self, screen: Any):
        pass
