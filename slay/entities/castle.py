from slay.entities.structure import Structure
from slay.player import Player
from slay.tile import Tile


class Castle(Structure):
    def __init__(self, location: Tile, owner: Player):
        super().__init__(location, owner)

    @property
    def cost(self):
        return 10
