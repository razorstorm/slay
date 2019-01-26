from typing import List, Dict

from slay.move import Move
from slay.player import Player
from slay.tile import Tile


class Board(object):

    def __init__(self, players: List[Player]):
        self.players = players
        self.tiles = self._generate_tiles()
        self.winner = None
        self.current_turn = 0
        self.player_moves = list()

    def _generate_tiles(self) -> Dict[Tile]:
        pass

    def _increment_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def play(self):
        player = self.players[self.current_turn]
        moves = player.make_moves()
        self.player_moves.append(moves)
        self.apply(moves)
        self._increment_turn()

    def apply(self, moves: List[Move]):
        pass
