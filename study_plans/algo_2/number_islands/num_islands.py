# Standard Library
from collections.abc import Iterator
import doctest
from itertools import pairwise


class Solution:  # noqa: D101
    DIRECTIONS = (0, 1, 0, -1, 0)

    def numIslands(self, grid: list[list[str]]) -> int:
        """Return number of disparate islands in given grid.

        String 1 demarks land, the grid is surrounded by water

        Args:
            grid (List[List[str]]): Grid representing land water cells

        Returns:
            int: Number of islands in the given grid.
        """

        def is_land(row: int, col: int) -> bool:
            try:
                return row >= 0 and col >= 0 and grid[row][col] == "1"
            except IndexError:
                return False

        def delete_island(row: int, col: int) -> None:
            if not is_land(row, col):
                return
            grid[row][col] = "0"
            moves = pairwise((0, 1, 0, -1, 0))
            for move in moves:
                delete_island(row + move[0], col + move[1])

        num_islands = 0
        for i in range(len(grid)):
            for j_col in range(len(grid[0])):
                if grid[i][j_col] == "1":
                    num_islands += 1
                    delete_island(i, j_col)

        return num_islands

    @classmethod
    def valid_neighbors(
        cls,
        row: int,
        col: int,
        row_max: int,
        col_max: int,
    ) -> Iterator[tuple[int, int]]:
        """Generate valid cardinal neighbors that are in bounds."""
        for delta_r, delta_c in pairwise(cls.DIRECTIONS):
            new_row, new_col = row + delta_r, col + delta_c
            if 0 <= new_row < row_max and 0 <= new_col < col_max:
                yield new_row, new_col

    def numIslandsUF(self, grid: list[list[str]]) -> int:
        """Use UnionFind structure to return number of islands in grid."""
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(grid)
        for i_row in range(rows):
            for j_col in range(cols):
                if grid[i_row][j_col] != "1":
                    continue
                for new_i, new_j in self.valid_neighbors(i_row, j_col, rows, cols):
                    if grid[new_i][new_j] == "1":
                        uf.union(i_row * cols + j_col, (new_i) * cols + (new_j))
        return uf.count


class UnionFind:
    """UnionFind tree structure in an array."""

    def __init__(self, grid: list[list[str]]) -> None:  # noqa: D107
        _count = 0
        rows, cols = len(grid), len(grid[0])
        self.parents = [0] * (rows * cols)
        self.rank = [0] * (rows * cols)
        for i, row in enumerate(grid):
            for j_col, cell_val in enumerate(row):
                if cell_val == "1":
                    self.parents[i * cols + j_col] = i * cols + j_col
                    _count += 1
        self.count = _count

    def find(self, cell: int) -> int:
        """Find top level parent of a cell."""
        if self.parents[cell] != cell:
            self.parents[cell] = self.find(self.parents[cell])
        return self.parents[cell]

    def union(self, x_cell: int, y_cell: int) -> None:
        """Combine two trees."""
        root_x, root_y = self.find(x_cell), self.find(y_cell)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parents[root_x] = root_y
        else:
            self.parents[root_y] = root_x
            self.rank[root_x] += 1
        self.count -= 1


def main() -> None:
    """Number of Islands on LeetCode.

    ====================================================

    Setup:
        >>> from copy import deepcopy
        >>> sol = Solution()
        >>> test_case_1 = [["1","1","1","1","0"],["1","1","0","1","0"],\
            ["1","1","0","0","0"],["0","0","0","0","0"]]
        >>> test_case_2 = [["1","1","0","0","0"],["1","1","0","0","0"],\
            ["0","0","1","0","0"],["0","0","0","1","1"]]

    Example 1:
        >>> sol.numIslands(deepcopy(test_case_1))
        1
        >>> sol.numIslandsUF(test_case_1)
        1

    Example 2:
        >>> sol.numIslands(deepcopy(test_case_2))
        3
        >>> sol.numIslandsUF(test_case_2)
        3
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
