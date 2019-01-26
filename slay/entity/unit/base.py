from __future__ import annotations

from abc import ABC
from typing import Optional, Any

from slay.entity.base import Entity
from slay.entity.structure.palm_tree import PalmTree
from slay.entity.structure.pine_tree import PineTree


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
        return all([
            new_location.active,  # can't move into a water tile
            self._can_defeat_tile_defender(new_location),
            self._tile_is_internal_or_adjacent(new_location),
            self._tile_does_not_contain_friendly_unit(new_location)
        ])

    def move(self, new_location: 'Tile') -> Optional['Move']:
        pass

    def draw(self, screen: Any):
        pass

    def _can_defeat_tile_defender(self, new_location: 'Tile') -> bool:
        self_and_neighbors = [tile for tile in new_location.neighbors if tile.owner == new_location.owner] + [new_location]
        defender_ranks = [neighbor.occupant.rank for neighbor in self_and_neighbors if neighbor.occupant is not None]
        max_defender_rank = max(defender_ranks) if defender_ranks else None
        return max_defender_rank is None or max_defender_rank < self.rank

    def _tile_is_internal_or_adjacent(self, new_location: 'Tile'):
        return self.territory.contains(new_location) or self.territory.has_neighbor(new_location)

    def _tile_does_not_contain_friendly_unit(self, new_location: 'Tile'):
        if (
            new_location.owner == self.territory.owner and
            new_location.occupant is not None and
            not isinstance(new_location.occupant, (PineTree, PalmTree))
        ):
            return False
        return True
