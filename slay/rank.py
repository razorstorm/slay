from __future__ import annotations

from collections import defaultdict
from enum import Enum


class Rank(Enum):
    PEASANT = 1
    VILLAGE = 1
    SPEARMAN = 2
    CASTLE = 2
    KNIGHT = 3
    BARON = 4

    @property
    def upkeep(self):
        return RANK_TO_UPKEEP_MAP.get(self)

    def __add__(self, other: Rank) -> Rank:
        return VALUE_TO_RANKS.get(self.value + other.value)


VALUE_TO_RANKS = {rank.value: rank for rank in Rank}
RANK_TO_UPKEEP_MAP = defaultdict(
    int,
    {
        Rank.PEASANT: 2,
        Rank.SPEARMAN: 6,
        Rank.KNIGHT: 18,
        Rank.BARON: 56,
    }
)
