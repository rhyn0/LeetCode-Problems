# Standard Library
from collections.abc import Iterator
import doctest
from itertools import pairwise


class Solution:  # noqa: D101
    NEIGHBORS_TUP = (0, 1, 0, -1, 0)

    @classmethod
    def valid_neighbors(
        cls, curr_x: int, curr_y: int, row_max: int, col_max: int
    ) -> Iterator[tuple[int, int]]:
        """Generate in bound neighbors for a given 2D point."""
        for dx, dy in pairwise(cls.NEIGHBORS_TUP):
            temp_x, temp_y = curr_x + dx, curr_y + dy
            if 0 <= temp_x < row_max and 0 <= temp_y < col_max:
                yield temp_x, temp_y

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:  # spec
        """Return a list of all locations that can touch both oceans.

        Given a 2d matrix of heights on an island that is in between two oceans
        find all locations that water can flow from to both oceans.
        Water can flow from a cell to cells that have equal or lower height.
        Any cell that is on the border (touching an ocean) can flow
        into that ocean.

        Args:
            heights (List[List[int]]): Grid of heights above sea level

        Returns:
            List[List[int]]: List of locations that water can flow from to the oceans
        """
        pac_set, atl_set = set(), set()
        n_rows, m_cols = len(heights), len(heights[0])

        def dfs(row: int, col: int, visited: set, prev_height: int) -> None:
            if (row, col) in visited:
                return
            visited.add((row, col))
            for pos_x, pos_y in self.valid_neighbors(row, col, n_rows, m_cols):
                if heights[pos_x][pos_y] >= prev_height:
                    dfs(
                        pos_x,
                        pos_y,
                        visited,
                        heights[pos_x][pos_y],
                    )

        for col in range(m_cols):
            dfs(0, col, pac_set, heights[0][col])
            dfs(n_rows - 1, col, atl_set, heights[-1][col])

        for row in range(n_rows):
            dfs(row, 0, pac_set, heights[row][0])
            dfs(row, m_cols - 1, atl_set, heights[row][-1])

        return [list(pos) for pos in pac_set.intersection(atl_set)]


def main():
    """Pacific Atlantic Water Flow on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],\
            [5,1,1,2,4]])
        [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]

    Example 2:
        >>> sol.pacificAtlantic([[2,1],[1,2]])
        [[1, 0], [1, 1], [0, 0], [0, 1]]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
