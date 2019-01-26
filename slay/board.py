from __future__ import annotations

from random import choice
from typing import List, Any, Set, Optional, Dict

from slay.territory import Territory
from slay.tile import Tile


class Board(object):

    def __init__(self, players: List['Player'], size: int = 10):
        self.players = players
        self.size = size
        self.tiles = self._generate_tiles(self.players, self.size)
        self.territories_by_player = {
            player: self._players_territories_from_tiles(player, self.tiles) for player in players
        }

    @classmethod
    def _generate_tiles(cls, players: List['Player'], board_size: int) -> Set['Tile']:
        tiles = {(i, j): Tile(set(), choice(players), None) for i in range(board_size) for j in range(board_size)}
        for (i, j) in tiles.keys():
            current = tiles[(i, j)]
            current.neighbors += []
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

    def draw(self, screen: Any):
        [territory.draw(screen) for territory in self.territories_by_player.values()]
