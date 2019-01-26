from slay.entities.structure import Structure
from slay.nature_player import NaturePlayer
from slay.tile import Tile


class PineTree(Structure):

    def __init__(self, location: Tile, owner: NaturePlayer):
        super().__init__(location, owner)

    @property
    def cost(self):
        return 0

    def is_valid_move(self, new_location: Tile) -> bool:
        pass

    def move(self, new_location: Tile) -> None:
        pass

    def draw(self) -> None:
        pass
