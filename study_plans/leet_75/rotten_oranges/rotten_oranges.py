# Standard Library
from collections import deque
from collections.abc import Generator
import doctest
from enum import IntEnum
from itertools import pairwise


class OrangeFarmCell(IntEnum):
    """State of a cell on the grid of the given orange farm."""

    NOTHING = 0
    RIPE = 1
    ROTTEN = 2


class Solution:  # noqa: D101
    def orangesRotting(self, grid: list[list[int]]) -> int:  # spec
        """Return the amount of time to convert all fresh oranges to rotten ones.

        Given a 2D grid of cells containing either:
        nothing, fresh oranges, or rotten oranges.
        Key for the state of a cell is described in Enum OrangeFarmCell.
        Rottenness spreads to ripe oranges every minute in the 4 cardinal directions.

        Args:
            grid (List[List[int]]): Grid showing the situation of oranges

        Returns:
            int: the number of minutes to convert all oranges to rotten ones.
        """

        def _in_bound(row: int, col: int) -> Generator[tuple[int, int], None, None]:
            yield from (
                (row + add_i, col + add_j)
                for add_i, add_j in pairwise((0, 1, 0, -1, 0))
                if 0 <= row + add_i < m and 0 <= col + add_j < n
            )

        m, n = len(grid), len(grid[0])
        que, num_oranges, minute_max = deque(), 0, 0
        for row_num, row in enumerate(grid):
            for col_num, cell in enumerate(row):
                if cell == OrangeFarmCell.RIPE:
                    num_oranges += 1
                elif cell == OrangeFarmCell.ROTTEN:
                    que.append(((row_num, col_num), 1))  # cell location, minute
        while que and num_oranges:
            curr = que.popleft()
            minute_max = max(minute_max, curr[1])
            for pos_x, pos_y in _in_bound(*curr[0]):
                if grid[pos_x][pos_y] == OrangeFarmCell.RIPE:
                    grid[pos_x][pos_y] = OrangeFarmCell.ROTTEN.value
                    num_oranges -= 1
                    que.append(((pos_x, pos_y), curr[1] + 1))
        return minute_max if num_oranges == 0 else -1


def main() -> None:
    """Rotting Oranges on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
        4

    Example 2:
        >>> sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
        -1

    Example 3:
        >>> sol.orangesRotting([[0, 2]])
        0
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
