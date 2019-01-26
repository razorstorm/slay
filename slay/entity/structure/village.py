from typing import Any

from slay.entity.structure import Structure
from slay.rank import Rank


class Village(Structure):

    cost = 0
    rank = Rank.VILLAGE

    def draw(self, screen: Any):
        pass
