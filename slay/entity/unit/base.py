from __future__ import annotations

from abc import ABC
from typing import Optional

from slay.entity.base import Entity


class Unit(Entity, ABC):

    cost = 10
    upkeep: int = NotImplemented

    def __init__(self, location: 'Tile', territory: 'Territory', rank: 'Rank', has_move: bool):
        super().__init__(location, territory)
        self.rank = rank
        self.has_move = has_move

    def __add__(self, other: 'Unit') -> Optional['Unit']:
        # TODO: move this to rule
        # TODO: fix rank + rank (currently undefined behavior)
        if self.rank.value + other.rank.value > 4 or self.territory != other.territory:
            return None
        return Unit(self.location, self.owner, self.rank + other.rank, self.has_move and other.has_move)

    def is_valid_move(self, new_location: 'Tile') -> bool:
        # TODO: move to rule-based engine
        pass

    def move(self, new_location: 'Tile') -> Optional['Move']:
        pass
