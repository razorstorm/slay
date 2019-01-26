from abc import abstractmethod

from slay.entities.entity import Entity
from slay.tile import Tile


class Structure(Entity):
    def __init__(self, location: Tile):
        super().__init__(location, False)

    @property
    def upkeep(self):
        return 0

    @property
    @abstractmethod
    def cost(self):
        pass
