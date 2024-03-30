"""Daily Challenge for June 18, 2023 on LeetCode."""

# Standard Library
import doctest
from itertools import pairwise
from itertools import product


class Solution:  # noqa: D101
    NEIGHBORS = (1, 0, -1, 0, 1)

    def countPaths(self, grid: list[list[int]]) -> int:
        """Return number of strictly increasing paths starting and ending anywhere.

        Path can start and end anywhere in grid for any length.
        Can traverse to any cell in the cardinal directions.
        Answer must be returned modulo 10^9 + 7

        Args:
            grid (list[list[int]]): grid to find paths in

        Returns:
            int: Number of strictly increasing paths, modulo'd
        """
        m, n = len(grid), len(grid[0])
        leet_mod = 10**9 + 7

        def valid_cell(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n

        dp = [[1 for _ in range(n)] for _ in range(m)]
        cell_list = list(product(range(m), range(n)))
        cell_list.sort(key=lambda cell: grid[cell[0]][cell[1]])
        for row, col in cell_list:
            grid_val = grid[row][col]
            for d_row, d_col in pairwise(self.NEIGHBORS):
                new_row, new_col = row + d_row, col + d_col
                if (
                    not valid_cell(new_row, new_col)
                    or grid[new_row][new_col] <= grid_val
                ):
                    continue
                dp[new_row][new_col] += dp[row][col]
                dp[new_row][new_col] %= leet_mod
        return sum(sum(row) % leet_mod for row in dp) % leet_mod


def main() -> None:
    """2328. Number of Increasing Paths in a Grid on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1,1],[3,4]]
        >>> example_case_2 = [[1],[2]]

    Example 1:
        >>> sol.countPaths(example_case_1)
        8

    Example 2:
        >>> sol.countPaths(example_case_2)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
