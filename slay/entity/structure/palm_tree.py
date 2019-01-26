from slay.entity.structure import Structure
from slay.player.nature_player import NaturePlayer
from slay.tile import Tile


class PalmTree(Structure):

    cost = 0

    def __init__(self, location: Tile, owner: NaturePlayer):
        super().__init__(location, owner)
