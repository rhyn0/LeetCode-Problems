"""Daily Challenge for June 30, 2023 on LeetCode."""

# Standard Library
from collections import deque
import doctest
from itertools import pairwise


class Solution:  # noqa: D101
    def crossable_terrain(self, m: int, n: int, cell_list: list[list[int]]) -> bool:
        """Return whether the given grid is crossable from top to bottom."""
        neighbors = (1, 0, -1, 0, 1)
        water_cells = {(row - 1, col - 1) for row, col in cell_list}
        # print(water_cells)
        visited = set()

        def dfs(curr_row: int, curr_col: int) -> bool:
            # print(f"Checking on pos {curr_row, curr_col}")
            if (
                (curr_row, curr_col) in water_cells
                or (curr_row, curr_col) in visited
                or curr_row < 0
                or curr_col < 0
                or curr_col >= n
            ):
                return False
            if curr_row == m - 1:
                return True
            # print(f"depth searching from pos {curr_row, curr_col}")
            visited.add((curr_row, curr_col))
            return any(
                dfs(curr_row + delta_row, curr_col + delta_col)
                for delta_row, delta_col in pairwise(neighbors)
            )

        return any(dfs(0, j) for j in range(n))

    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        """Return the last day that the given terrain is crossable.

        Terrain is initially all LAND, but for the ith day,
        cells[i] := (row_i, col_i) becomes a WATER cell

        Args:
            row (int): Number of rows in the terrain
            col (int): Number of cols in the terrain
            cells (list[list[int]]): Order in which each cell will become WATER

        Returns:
            int: Last day that the terrain is crossable
        """
        left, right = 1, row * col
        while left < right:
            mid = right - (right - left) // 2
            # print(f"checking if crossable for day {mid}")
            if self.crossable_terrain(row, col, cells[:mid]):
                # print(f"was crossable for day {mid}")
                left = mid
            else:
                right = mid - 1
        return left

    def crossable_terrain_grid(
        self,
        m: int,
        n: int,
        cell_list: list[list[int]],
    ) -> bool:
        """Return same as `crossable_terrain` but use a grid instead of sets."""
        neighbors = (1, 0, -1, 0, 1)
        grid = [[0] * n for _ in range(m)]
        for row, col in cell_list:
            grid[row - 1][col - 1] = 1
        q = deque()
        q.extend((0, j) for j in range(n) if grid[0][j] == 0)
        while q:
            curr_row, curr_col = q.popleft()
            if (
                not (0 <= curr_row < m)
                or not (0 <= curr_col < n)
                or grid[curr_row][curr_col] != 0
            ):
                continue
            if curr_row == m - 1:
                return True
            grid[curr_row][curr_col] = -1
            q.extend(
                (curr_row + delta_row, curr_col + delta_col)
                for delta_row, delta_col in pairwise(neighbors)
            )
        return False

    def latestDayToCrossBfs(self, row: int, col: int, cells: list[list[int]]) -> int:
        """Return same as above using a different path searching method."""
        left, right = 1, row * col
        while left < right:
            mid = right - (right - left) // 2
            # print(f"checking if crossable for day {mid}")
            if self.crossable_terrain_grid(row, col, cells[:mid]):
                # print(f"was crossable for day {mid}")
                left = mid
            else:
                right = mid - 1
        return left


def main() -> None:
    """1970. Last Day Where You Can Still Cross on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 2, 2, [[1,1],[2,1],[1,2],[2,2]]
        >>> example_case_2 = 2, 2, [[1,1],[1,2],[2,1],[2,2]]
        >>> example_case_3 = 3, 3, [[1,2],[2,1],[3,3],[2,2],\
            [1,1],[1,3],[2,3],[3,2],[3,1]]

    Example 1:
        >>> sol.latestDayToCross(*example_case_1)
        2
        >>> sol.latestDayToCrossBfs(*example_case_1)
        2

    Example 2:
        >>> sol.latestDayToCross(*example_case_2)
        1
        >>> sol.latestDayToCrossBfs(*example_case_2)
        1

    Example 3:
        >>> sol.latestDayToCross(*example_case_3)
        3
        >>> sol.latestDayToCrossBfs(*example_case_3)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
