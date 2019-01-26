from slay.entity.structure import Structure
from slay.player.nature_player import NaturePlayer
from slay.tile import Tile


class Grave(Structure):

    cost = 0

    def __init__(self, location: Tile, owner: NaturePlayer):
        super().__init__(location, owner)

    def draw(self) -> None:
        pass
