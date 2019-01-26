from __future__ import annotations

from abc import abstractmethod, ABC
from typing import List, Any


class Player(ABC):

    @abstractmethod
    def take_turn(self, board: 'Board', screen: Any) -> List['Move']:
        pass

    @abstractmethod
    def draw(self, screen: Any):
        pass
