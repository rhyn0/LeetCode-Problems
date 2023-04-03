# Standard Library
import doctest
from math import comb


class Solution:  # noqa: D101
    def uniquePaths(self, num_row: int, num_col: int) -> int:  # spec
        """Return number of unique paths from grid start to grid end.

        Grid start and end are top left and bottom right respectively.
        Can only move down or right.

        Uses combination math to return

        Args:
            num_row (int): Number of rows on the grid
            num_col (int): Number of columns on the grid

        Returns:
            int: Number of unique paths
        """
        return comb(num_row + num_col - 2, num_row - 1)

    def uniquePathsDP(self, num_row: int, num_col: int) -> int:
        """Return number of unique paths for grid.

        Same result as above but uses Dynamic Programming tabulation.

        Args:
            num_row (int): Number of rows on the grid
            num_col (int): Number of columns on the grid

        Returns:
            int: Number of unique paths
        """
        data_tab = [1] * num_col
        # Only way to stay in first row is to move only right
        # Only way to stay in first column is to move only down
        for _ in range(1, num_row):
            # skip first row
            for col in range(1, num_col):
                # skip first column
                data_tab[col] += data_tab[col - 1]
        return data_tab[-1]


def main():
    """Unique Paths on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.uniquePaths(3, 2)
        3

    Example 2:
        >>> sol.uniquePaths(3, 7)
        28

    Dynamic Programming Tests
    Example 1:
        >>> sol.uniquePathsDP(3, 2)
        3

    Example 2:
        >>> sol.uniquePathsDP(3, 7)
        28
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
