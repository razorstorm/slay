from abc import abstractmethod

from slay.entities.entity import Entity
from slay.player import Player
from slay.tile import Tile


class Unit(Entity):
    def __init__(self, location: Tile, owner: Player, has_turn: bool):
        super().__init__(location, owner)
        self.can_move = has_turn

    @property
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def upkeep(self):
        pass
