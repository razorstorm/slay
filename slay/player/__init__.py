from abc import abstractmethod
from typing import List

from slay.board import Board
from slay.move import Move


class Player(object):

    @abstractmethod
    def take_turn(self, board: Board) -> List[Move]:
        pass
