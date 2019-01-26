from abc import abstractmethod, ABC
from typing import Optional

from slay.move import Move
from slay.player import Player
from slay.tile import Tile


class Entity(ABC):

    cost: int = NotImplemented
    upkeep: int = NotImplemented

    def __init__(self, location: Tile, owner: Player):
        # This is a reference to a tile object
        self.location = location
        self.owner = owner

    @abstractmethod
    def is_valid_move(self, new_location: Tile) -> bool:
        pass

    @abstractmethod
    def move(self, new_location: Tile) -> Optional[Move]:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
