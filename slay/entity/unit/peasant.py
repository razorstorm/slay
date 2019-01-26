from __future__ import annotations

from typing import Any

from slay.entity.unit.base import Unit


class Peasant(Unit):

    upkeep = 2

    def draw(self, screen: Any):
        pass
