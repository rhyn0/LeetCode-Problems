"""Matrix Pattern of Dynamic Programming Essentials Study Plan."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    OBSTACLE = 1

    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        """Return number of unique paths from top left to bottom for a given grid.

        Each cell in the grid is given as 0 or 1 - where 1 represents the presence
        of an obstacle. Cells with obstacles can never be inhabited by the
        traversing entity. Traversing entity can only move down or right.

        Args:
            grid (list[list[int]]): m x n grid with valid values for obstacle or not

        Returns:
            int: Unique paths from top left to bottom right
        """
        dp, obstacle_hit = [], False
        for val in grid[0]:
            dp.append(int(val != self.OBSTACLE and not obstacle_hit))
            obstacle_hit |= val == self.OBSTACLE
        for row in grid[1:]:
            for curr_col, cell_val in enumerate(row):
                # handle first index differently, avoid wrap around
                if curr_col == 0:
                    dp[curr_col] = dp[curr_col] if cell_val != self.OBSTACLE else 0
                    continue

                dp[curr_col] = (
                    dp[curr_col] + dp[curr_col - 1] if cell_val != self.OBSTACLE else 0
                )

        return dp[-1]


def main() -> None:
    """63. Unique Paths II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[0,0,0],[0,1,0],[0,0,0]]
        >>> example_case_2 = [[0,1],[0,0]]
        >>> test_case_1 = [[1, 0]]

    Example 1:
        >>> sol.uniquePathsWithObstacles(example_case_1)
        2

    Example 2:
        >>> sol.uniquePathsWithObstacles(example_case_2)
        1

    Test 1:
        >>> sol.uniquePathsWithObstacles(test_case_1)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
