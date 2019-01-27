from __future__ import annotations

from random import choice, getrandbits
from typing import List, Any, Set, Optional, Dict

from slay.territory import Territory
from slay.tile import Tile


class Board(object):

    def __init__(self, players: List['Player'], size: int, window: Any):
        self.players = players
        self.size = size
        self.window = window
        # TODO: truncate
        self.window.addstr(1, 1, "Board")
        self.window.refresh()
        self.tiles = self._generate_tiles(self.players, self.size)
        self.territories_by_player = {
            player: self._players_territories_from_tiles(player, self.tiles) for player in players
        }

    @classmethod
    def _generate_tile(cls, player: 'Player'):
        return Tile(bool(getrandbits(1)), set(), player, None)

    @classmethod
    def _generate_tiles(cls, players: List['Player'], board_size: int) -> Set['Tile']:
        tiles = {(x, y): cls._generate_tile(choice(players)) for x in range(board_size) for y in range(board_size)}
        for (x, y) in tiles.keys():
            current = tiles[(x, y)]
            # current.neighbors += []
        return set(tiles.values())

    @classmethod
    def _first_territory_in_neighbors(
        cls,
        territories_by_tile: Dict['Tile', 'Territory'],
        neighbors: Set['Tile'],
    ) -> Optional['Territory']:
        for neighbor in neighbors:
            if neighbor in territories_by_tile.keys():
                return territories_by_tile[neighbor]

    @classmethod
    def _players_territories_from_tiles(cls, player: 'Player', tiles: Set['Tile']) -> Set['Territory']:
        territories_by_tile = dict()
        frontier = {tile for tile in tiles if tile.owner == player}
        while frontier:
            current = frontier.pop()
            territory = cls._first_territory_in_neighbors(territories_by_tile, current.neighbors)
            if not territory:
                territory = Territory(player, {current}, None)
            territory += current
            territories_by_tile[current] = territory

        territories = set(territories_by_tile.values())
        for territory in territories:
            territory.create_village()
        return set(territories_by_tile.values())

    def apply(self, moves: List['Move']):
        pass
