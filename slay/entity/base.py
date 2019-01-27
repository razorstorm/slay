from __future__ import annotations

from abc import ABC

from slay.rank import Rank


class Entity(ABC):

    cost: int = NotImplemented
    rank: Rank = NotImplemented

    def __init__(self, location: 'Tile', territory: 'Territory'):
        self.location = location
        self.territory = territory
        self.owner = territory.owner
