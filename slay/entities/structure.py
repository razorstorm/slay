from abc import abstractmethod

from slay.entities.entity import Entity
from slay.player import Player
from slay.tile import Tile


class Structure(Entity):
    def __init__(self, location: Tile, owner: Player):
        super().__init__(location, False, owner)

    @property
    def upkeep(self):
        return 0

    @property
    @abstractmethod
    def cost(self):
        pass
