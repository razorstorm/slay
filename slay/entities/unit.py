from abc import abstractmethod

from slay.entities.entity import Entity
from slay.tile import Tile


class Unit(Entity):
    def __init__(self, location: Tile):
        super().__init__(location, True)

    @property
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def upkeep(self):
        pass
