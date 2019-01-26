from abc import abstractmethod

from slay.entities.entity import Entity
from slay.player import Player
from slay.tile import Tile


class Unit(Entity):
    def __init__(self, location: Tile, owner: Player):
        super().__init__(location, True, owner)

    @property
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def upkeep(self):
        pass
