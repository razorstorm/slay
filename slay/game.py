from __future__ import annotations

from typing import List, Any

from slay.board import Board
from slay.hud import Hud
from slay.player.nature import Nature


class Game(object):

    def __init__(self, players: List['Player']):
        self.players = players
        self.nature = Nature()
        self.hud = Hud(players)
        self.winner = None
        self.current_turn = 0
        self.player_moves = list()
        self.board = Board(self.players)
        self.board_history = [self.board]

    def _increment_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def next_turn(self, screen: Any):
        player = self.players[self.current_turn]
        moves = player.take_turn(self.board, screen)
        self.board_history.append(self.board)
        self.player_moves.append(moves)
        self.board = self.board.apply(moves)
        self.nature.take_turn(self.board, screen)
        self._increment_turn()

    def draw(self, screen: Any):
        self.board.draw(screen)
        self.hud.draw(screen)
