from typing import Any

from slay.entity.structure import Structure
from slay.rank import Rank


class PineTree(Structure):

    cost = 0
    rank = Rank.TREE

    def draw(self, screen: Any):
        pass
