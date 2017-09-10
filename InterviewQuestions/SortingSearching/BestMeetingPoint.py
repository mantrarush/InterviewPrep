"""
A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2D grid of values 0 or 1, where each
1 marks the home of someone in the group.
The distance is calculated using Manhattan Distance,
where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):
0,400,220
1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (0,2) is an ideal meeting point, as the
total travel distance of 2+2+2=6 is minimal. So return 6.
"""
from typing import List, Dict, NewType

Distance = NewType("Distance", int)


HOME_LOCATION_FLAG = 1
UNKNOWN = -147


class Board:
    def __init__(self, from_list: List[List[int]] = None):
        self.rows: int = UNKNOWN
        self.cols: int = UNKNOWN
        self.home_tiles: List[Tile] = []
        if from_list is not None and len(from_list) > 0:
            self.cols = len(from_list[0])
            self.rows = len(from_list)
            for row_index in range(len(from_list)):
                while True:
                    row = from_list[row_index]
                    try:
                        column = row.index(HOME_LOCATION_FLAG)
                        self.home_tiles.append(Tile(x=column, y=row_index))
                        row[column] = 0
                    except:
                        break

    @property
    def center(self):
        return Tile(x=int(self.cols/2), y=int(self.rows/2))


class Tile:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def compute_distance(self, other_tile) -> Distance:
        """
        Returns the distance between a tile and another tile
        :param other_tile: tile fo compute distance.
        :return: int
        """
        return abs(self.x - other_tile.x ) + abs(self.y - other_tile.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x ^ self.y


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        board = Board(grid)
        results: Dict[Distance: [Tile]] = {}
        if len(board.home_tiles) == board.rows * board.cols:
            return Solution.calc_distance(home_locs=board.home_tiles, loc_interest=board.center)
        for row in range(board.rows):
            for column in range(board.cols):
                loc_interest = Tile(x=column, y=row)
                total_distance = Solution.calc_distance(board.home_tiles, loc_interest)
                if total_distance in results:
                    results[total_distance].append(loc_interest)
                else:
                    results[total_distance] = [loc_interest]

        distances = list(results.keys())
        distances.sort()
        return distances[0]

    @staticmethod
    def calc_distance(home_locs: [Tile], loc_interest: Tile) -> int:
        total_distance = 0
        for home_tile in home_locs:
            total_distance = total_distance + home_tile.compute_distance(loc_interest)
        return total_distance

