from abc import abstractmethod, ABC
from typing import Optional

from slay.entities.entity import Entity
from slay.move import Move
from slay.player import Player
from slay.tile import Tile


class Structure(Entity, ABC):
    def __init__(self, location: Tile, owner: Player):
        super().__init__(location, owner)

    @property
    def upkeep(self) -> int:
        return 0

    @property
    @abstractmethod
    def cost(self):
        pass

    def is_valid_move(self, new_location: Tile) -> bool:
        return False

    def move(self, new_location: Tile) -> Optional[Move]:
        return None
