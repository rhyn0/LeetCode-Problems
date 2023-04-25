"""Intro Problem to Matrix Pattern for Essentials of Dynamic Programming Study Plan."""
# Standard Library
import doctest
from itertools import accumulate


class Solution:  # noqa: D101
    def minPathSum(self, grid: list[list[int]]) -> int:
        """Return the minimum cost of a path from start to end.

        Matrix start is top left corner.
        Matrix end is bottom right corner.
        Only valid moves are to move down and to move right.

        Args:
            grid (list[list[int]]): Representation of cost to move to that cell

        Returns:
            int: Minimum cost to go from start to end
        """
        dp = list(accumulate(grid[0]))
        for curr_weight_row in grid[1:]:
            # intentionally lag behind idx to get left value at i - 1
            for idx, top_val in enumerate(dp):
                if idx == 0:
                    dp[idx] += curr_weight_row[idx]
                else:
                    dp[idx] = min(top_val, dp[idx - 1]) + curr_weight_row[idx]

        return dp[-1]


def main():
    """64. Minimum Path Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1,3,1],[1,5,1],[4,2,1]]
        >>> example_case_2 = [[1,2,3],[4,5,6]]

    Example 1:
        >>> sol.minPathSum(example_case_1)
        7

    Example 2:
        >>> sol.minPathSum(example_case_2)
        12
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
