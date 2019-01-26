from __future__ import annotations


class Move(object):

    def __init__(self, unit: 'Unit', location: 'Tile'):
        self.unit = unit
        self.location = location
