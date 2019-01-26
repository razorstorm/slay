from typing import List, Dict

from slay.move import Move
from slay.player import Player
from slay.tile import Tile


class Board(object):

    def __init__(self, players: List[Player]):
        self.players = players
        self.tiles = self._generate_tiles()

    def _generate_tiles(self) -> Dict[Tile]:
        pass

    def apply(self, moves: List[Move]):
        pass
