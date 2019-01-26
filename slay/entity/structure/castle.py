from __future__ import annotations

from typing import Any

from slay.entity.structure.base import Structure
from slay.rank import Rank


class Castle(Structure):

    cost = 15
    rank = Rank.CASTLE

    def draw(self, screen: Any):
        pass
