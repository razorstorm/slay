from abc import abstractmethod, ABC
from typing import List, Any

from slay.board import Board
from slay.move import Move


class Player(ABC):

    @abstractmethod
    def take_turn(self, board: Board, screen: Any) -> List[Move]:
        pass

    @abstractmethod
    def draw(self, screen: Any):
        pass
