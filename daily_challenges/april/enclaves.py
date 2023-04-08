"""LeetCode Daily Challenge for April 7, 2023."""
# Standard Library
from collections import deque
from collections.abc import Iterator
import doctest
from enum import IntEnum
from itertools import pairwise


class Solution:  # noqa: D101
    class GridValues(IntEnum):
        """Possible values for cells in the given grid."""

        SEA = 0
        LAND = 1

    # pairwise iterator for cardinal neighbors
    NEIGHBORS = (1, 0, -1, 0, 1)

    @classmethod
    def in_bound_neighbors(
        cls, max_row: int, max_col: int, row: int, col: int
    ) -> Iterator[tuple[int, int]]:
        """Return cardinal neighbors that are on the grid."""
        for d_row, d_col in pairwise(cls.NEIGHBORS):
            new_row, new_col = row + d_row, col + d_col
            if 0 <= new_row < max_row and 0 <= new_col < max_col:
                yield new_row, new_col

    @classmethod
    def untouched_land(cls, grid: list[list[int]]) -> int:
        """Return number of land in the grid."""
        return sum(sum(line) for line in grid)

    def numEnclaves(self, grid: list[list[int]]) -> int:
        """Return number of land cells that are unreachable from border.

        This solution uses Depth-First Search to remove lands from the grid
        that can reach the border of the grid.

        Args:
            grid (list[list[int]]): grid denoting the state of the land and sea cells

        Returns:
            int: Number of land cells
        """
        n, m = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> None:
            # print(row, col, grid[row][col])
            if grid[row][col] == self.GridValues.SEA:
                return
            grid[row][col] = self.GridValues.SEA.value
            for cardinal_neighbor in self.in_bound_neighbors(n, m, row, col):
                dfs(*cardinal_neighbor)

        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)
        for j in range(n):
            dfs(j, 0)
            dfs(j, m - 1)

        return self.untouched_land(grid)

    def numEnclavesBFS(self, grid: list[list[int]]) -> int:
        """Return same as above using BFS."""
        n, m = len(grid), len(grid[0])

        def bfs(row: int, col: int) -> None:
            if grid[row][col] != self.GridValues.LAND:
                return
            queue = deque()
            queue.append((row, col))
            grid[row][col] = self.GridValues.SEA.value
            while queue:
                curr_row, curr_col = queue.popleft()
                for new_row, new_col in self.in_bound_neighbors(
                    n, m, curr_row, curr_col
                ):
                    if grid[new_row][new_col] != self.GridValues.LAND:
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = self.GridValues.SEA.value

        for i in range(m):
            bfs(0, i)
            bfs(n - 1, i)
        for j in range(n):
            bfs(j, 0)
            bfs(j, m - 1)

        return self.untouched_land(grid)


def main():
    """Number of Enclaves on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
        >>> example_case_2 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

    Example 1:
        >>> sol.numEnclaves(example_case_1)
        3
        >>> sol.numEnclavesBFS(example_case_1)
        3

    Example 2:
        >>> sol.numEnclaves(example_case_2)
        0
        >>> sol.numEnclavesBFS(example_case_2)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
