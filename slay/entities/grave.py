from slay.entities.structure import Structure
from slay.nature_player import NaturePlayer
from slay.tile import Tile


class Grave(Structure):
    def __init__(self, location: Tile, owner: NaturePlayer):
        super().__init__(location, owner)

    @property
    def cost(self):
        return 0
