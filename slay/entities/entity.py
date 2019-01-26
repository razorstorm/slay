from abc import abstractmethod
from collections import defaultdict
from enum import Enum
from typing import Optional

from slay.move import Move
from slay.player import Player
from slay.tile import Tile


class Rank(Enum):
    PEASANT = 1
    VILLAGE = 1
    SPEARMAN = 2
    CASTLE = 2
    KNIGHT = 3
    BARON = 4

    @property
    def upkeep(self):
        return RANK_TO_UPKEEP_MAP.get(self)


RANK_TO_UPKEEP_MAP = defaultdict(
    int,
    {
        Rank.PEASANT: 2,
        Rank.SPEARMAN: 6,
        Rank.KNIGHT: 18,
        Rank.BARON: 56,
    }
)


class Entity(object):
    def __init__(self, location: Tile, owner: Player):
        # This is a reference to a tile object
        self.location = location
        self.owner = owner

    @property
    @abstractmethod
    def cost(self) -> int:
        pass

    @property
    @abstractmethod
    def upkeep(self) -> int:
        pass

    @abstractmethod
    def is_valid_move(self, new_location: Tile) -> bool:
        pass

    @abstractmethod
    def move(self, new_location: Tile) -> Optional[Move]:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
