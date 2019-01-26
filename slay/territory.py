from __future__ import annotations

from random import choice
from typing import Optional, Any, Set, Union, Callable, Dict

from slay.entity.structure import Structure
from slay.entity.structure.castle import Castle
from slay.entity.structure.palm_tree import PalmTree
from slay.entity.structure.pine_tree import PineTree
from slay.entity.structure.village import Village
from slay.entity.unit import Unit
from slay.player import Player
from slay.rank import Rank
from slay.tile import Tile


class Territory(object):

    INCOME_PER_TILE = 2

    def __init__(self, owner: Player, tiles: Set[Tile], village: Optional[Village], savings: int = 0):
        self.owner = owner
        self.tiles = tiles
        # FIXME: this currently counts trees as part of structures
        self.structures = {
            tile.occupant for tile in self.tiles
            if tile.occupant is not None and isinstance(tile.occupant, Structure)
        }
        self.units = {
            tile.occupant for tile in self.tiles
            if tile.occupant is not None and isinstance(tile.occupant, Unit)
        }
        self.village = village
        self.savings = savings

    @property
    def wages(self) -> int:
        return sum(unit.upkeep for unit in self.units)

    @property
    def income(self) -> int:
        return self.INCOME_PER_TILE * sum(
            tile.occupant is None or isinstance(tile.occupant, (PineTree, PalmTree)) for tile in self.tiles
        )

    def create_village(self) -> Optional[Territory]:
        if self.village is not None:
            return
        positions = {tile for tile in self.tiles if tile.occupant is None}
        return self + Village(choice(positions), self)

    @classmethod
    def _add_territory(cls, self: Territory, other: Territory) -> Optional[Territory]:
        smaller = min(self, other, key=lambda territory: len(territory.tiles))
        larger = max(self, other, key=lambda territory: len(territory.tiles))
        # TODO: implement subtract
        # does this work? feels messy because of cleaning up references everywhere
        # how do I remove all references to the smaller territory?
        smaller -= smaller.village
        # smaller.village.tile.occupant = None
        # smaller.village = None
        larger.savings += smaller.savings
        self += [tile for tile in other.tiles]
        return self

    @classmethod
    def _add_tile(cls, self: Territory, other: Tile) -> Optional[Territory]:
        self.tiles += other
        other.owner = self.owner
        if other.occupant is not None:
            self += other.occupant
        return self

    @classmethod
    def _add_village(cls, self: Territory, other: Village) -> Optional[Territory]:
        if self.village is not None:
            return
        self.village = other
        self += other.location
        return self

    @classmethod
    def _add_funcs(cls) -> Dict[type, Callable[[Territory, Any], Optional[Territory]]]:
        return {
            Territory: cls._add_territory,
            Tile: cls._add_tile,
            Village: cls._add_village,
        }

    def __add__(self, other: Union[Territory, Tile, Village]) -> Optional[Territory]:
        add_func = self._add_funcs()[type(other)]
        return add_func(self, other)

    @property
    def can_buy(self) -> bool:
        return self.can_buy_unit or self.can_buy_structure

    @property
    def can_buy_unit(self) -> bool:
        return self.savings >= Unit.cost

    @property
    def can_buy_structure(self) -> bool:
        return self.savings >= Castle.cost

    def buy_unit(self, location: Tile) -> Unit:
        self.savings -= Unit.cost
        return Unit(location, self, Rank.PEASANT, has_move=True)

    def buy_castle(self, location: Tile) -> Castle:
        self.savings -= Castle.cost
        return Castle(location, self)

    def draw(self, screen: Any):
        [tile.draw(screen) for tile in self.tiles]
