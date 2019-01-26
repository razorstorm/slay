from typing import List

from slay.player import Player
from slay.tile import Tile


class Territory(object):
    def __init__(self, owner: Player, tiles: List(Tile)):
        self.owner = owner
        self.tiles = tiles
