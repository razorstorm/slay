from abc import abstractmethod, ABC
from typing import Any

from slay.rank import Rank
from slay.territory import Territory
from slay.tile import Tile


class Entity(ABC):

    cost: int = NotImplemented
    rank: Rank = NotImplemented

    def __init__(self, location: Tile, territory: Territory):
        self.location = location
        self.territory = territory
        self.owner = territory.owner

    @abstractmethod
    def draw(self, screen: Any):
        # TODO: order matters, should use painter's algorithm
        pass
