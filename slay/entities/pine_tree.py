from slay.entities.structure import Structure
from slay.tile import Tile


class PineTree(Structure):
    def __init__(self, location: Tile):
        super().__init__(location)

    @property
    def cost(self):
        return 0
