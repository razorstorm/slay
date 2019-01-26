from __future__ import annotations

from abc import ABC
from typing import Any

from slay.entity.base import Entity


class Structure(Entity, ABC):
    def draw(self, screen: Any):
        pass
