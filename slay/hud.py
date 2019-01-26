from __future__ import annotations

from typing import Any, List


class Hud(object):

    def __init__(self, players: List['Player']):
        self.players = players

    def draw(self, screen: Any):
        [player.draw(screen) for i, player in enumerate(self.players)]
        height, width = screen.getmaxyx()
        title = "curses example"[:width - 1]
        screen.addstr(0, 0, title)
