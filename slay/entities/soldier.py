from slay.entities.entity import Rank
from slay.entities.unit import Unit
from slay.tile import Tile


class Soldier(Unit):
    def __init__(self, location: Tile, rank: Rank):
        super().__init__(location)
        self.rank = rank

    @property
    def cost(self):
        return 10

    @property
    def upkeep(self):
        return self.rank.upkeep

    def __add__(self, other):
        if self.rank + other.rank > 4:
            return None
        return Soldier(self.location, self.rank + other.rank)
