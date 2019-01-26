from slay.entity.structure import Structure
from slay.player.nature_player import NaturePlayer
from slay.tile import Tile


class PineTree(Structure):

    cost = 0

    def __init__(self, location: Tile, owner: NaturePlayer):
        super().__init__(location, owner)

    def is_valid_move(self, new_location: Tile) -> bool:
        pass

    def move(self, new_location: Tile) -> None:
        pass

    def draw(self) -> None:
        pass
