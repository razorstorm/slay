from abc import abstractmethod

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
    def __init__(self, location: Tile, can_move: bool, owner: Player):
        # This is a reference to a tile object
        self.location = location
        self.can_move = can_move
        self.owner = owner

    @property
    @abstractmethod
    def cost(self):
        return None

    @property
    @abstractmethod
    def upkeep(self):
        return None
