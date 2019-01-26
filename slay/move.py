from slay.entities.unit import Unit
from slay.tile import Tile


class Move(object):

    def __init__(self, unit: Unit, location: Tile):
        self.unit = unit
        self.location = location
