from __future__ import annotations

from typing import List

from slay.entity import Entity


class Tile(object):

    def __init__(self, occupant: Entity, neighbors: List[Tile]):
        self.occupant = occupant
        self.neighbors = neighbors
