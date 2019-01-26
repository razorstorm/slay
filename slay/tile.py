from __future__ import annotations

from typing import Any, Set, Optional


class Tile(object):

    def __init__(self, active: bool, neighbors: Set['Tile'], owner: 'Player', occupant: Optional['Entity']):
        self.active = active
        self.neighbors = neighbors
        self.owner = owner
        self.occupant = occupant

    def draw(self, screen: Any):
        if self.occupant is not None:
            self.occupant.draw(screen)
        # TODO: draw self
