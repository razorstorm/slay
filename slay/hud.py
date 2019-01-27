from __future__ import annotations

from typing import Any, List


class Hud(object):

    def __init__(self, players: List['Player'], window: Any):
        self.players = players
        self.window = window
        # TODO: truncate
        self.window.addstr(1, 1, "HUD")
        self.window.refresh()
