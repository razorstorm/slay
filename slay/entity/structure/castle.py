from slay.entity.structure import Structure

from slay.player import Player
from slay.tile import Tile


class Castle(Structure):

    cost = 15

    def __init__(self, location: Tile, owner: Player):
        super().__init__(location, owner)

    def draw(self):
        pass
