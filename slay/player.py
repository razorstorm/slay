from abc import abstractmethod
from typing import List

from slay.move import Move


class Player(object):

    def __init__(self, board):
        self.board = board

    @abstractmethod
    def make_moves(self) -> List[Move]:
        pass
