from __future__ import annotations

from enum import Enum


class Rank(Enum):
    TREE = 0
    GRAVE = 0
    PEASANT = 1
    VILLAGE = 1
    SPEARMAN = 2
    CASTLE = 2
    KNIGHT = 3
    BARON = 4

    @property
    def value(self) -> int:
        return super().value()
