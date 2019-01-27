from __future__ import annotations

from curses import newwin
from typing import List, Any

from slay.board import Board
from slay.hud import Hud
from slay.player.nature import Nature


class Game(object):

    def __init__(self, players: List['Player'], board_size: int, window: Any):
        self.players = players
        self.nature = Nature()
        self.winner = None
        self.current_turn = 0
        self.player_moves = list()
        self.hud = Hud(players, self._setup_hud_window(window))
        self.board = Board(self.players, board_size, self._setup_board_window(window))
        self.board_history = [self.board]

    @classmethod
    def _setup_hud_window(cls, parent: Any) -> Any:
        height, width = parent.getmaxyx()
        window_start_x = 2 * width // 3
        window_start_y = 0
        window_width = width // 3
        window_height = height
        window = newwin(window_height, window_width, window_start_y, window_start_x)
        window.border()
        return window

    @classmethod
    def _setup_board_window(cls, parent: Any) -> Any:
        height, width = parent.getmaxyx()
        window_start_x = 0
        window_start_y = 0
        window_width = 2 * width // 3
        window_height = height
        window = newwin(window_height, window_width, window_start_y, window_start_x)
        window.border()
        return window

    def _increment_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def next_turn(self):
        player = self.players[self.current_turn]
        # moves = player.take_turn(self.board, screen)
        # self.board_history.append(self.board)
        # self.player_moves.append(moves)
        # self.board = self.board.apply(moves)
        # self.nature.take_turn(self.board, screen)
        self._increment_turn()
