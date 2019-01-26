from abc import abstractmethod
from enum import Enum

from slay.player import Player
from slay.tile import Tile

UPKEEP_MAP = [2, 6, 18, 56]


class Rank(Enum):
    PEASANT = 1,
    SPEARMAN = 2,
    KNIGHT = 3,
    BARON = 4

    @property
    def upkeep(self):
        return UPKEEP_MAP.get(self.value)


class Entity(object):
    def __init__(self, location: Tile, owner: Player):
        # This is a reference to a tile object
        self.location = location
        self.owner = owner

    @property
    @abstractmethod
    def cost(self):
        return None

    @property
    @abstractmethod
    def upkeep(self):
        return None

    @abstractmethod
    def is_valid_move(self, new_location: Tile) -> bool:
        pass

    @abstractmethod
    def move(self, new_location: Tile) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
