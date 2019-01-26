from slay.entities.structure import Structure
from slay.nature_player import NaturePlayer
from slay.tile import Tile


class PalmTree(Structure):
    def __init__(self, location: Tile, owner: NaturePlayer):
        super().__init__(location)

    @property
    def cost(self):
        return 0
