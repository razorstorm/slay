from __future__ import annotations

from typing import Any

from slay.entity.structure.base import Structure
from slay.rank import Rank


class Grave(Structure):

    cost = 0
    rank = Rank.GRAVE

    def draw(self, screen: Any):
        pass
