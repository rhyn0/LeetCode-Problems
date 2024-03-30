"""Practice for Matrix Pattern for Essentials of Dynamic Programming Study Plan."""

# Standard Library
import doctest
from typing import Final


class Solution:  # noqa: D101
    # constraints say that this number will never be input
    INT_MAX: Final = 10**5

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """Return least cost path from top root to bottom row.

        Movement is restricted to be only down or diagonal down-right.
        This means when moving between rows the only possible endpoints from
        position i is either next row's i or i+1.

        One can think of the given argument as being
              1
             2 3
            4 5 6
            ....
        But for this problem it is easier to think of it as a matrix
            1 _ _
            2 3 _
            4 5 6
            ....

        Args:
            triangle (list[list[int]]): Triangle layout of the numbers
        """
        dp: list[int] = [self.INT_MAX] * len(triangle)
        dp[0] = triangle[0][0]
        for row_num, row in enumerate(triangle[1:], start=1):
            # have to go reverse, no dependencies on in row values
            for idx in range(row_num, -1, -1):
                value = row[idx]
                # be careful about negative index
                if idx == 0:
                    dp[idx] += value
                else:
                    dp[idx] = min(dp[idx], dp[idx - 1]) + value
        return min(dp)

    def minimumTotalUpside(self, triangle: list[list[int]]) -> int:
        """Return same as above but calculate in reverse order."""
        below_row = triangle[-1]
        n = len(triangle)
        # max index in a row is the row number (0 index)
        for curr_row in range(n - 2, -1, -1):
            below_row = [
                triangle[curr_row][idx] + min(below_row[idx], below_row[idx + 1])
                for idx in range(curr_row + 1)
            ]
        # at end this is the top row, with only one value
        return below_row[0]


def main() -> None:
    """120. Triangle on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
        >>> example_case_2 = [[-10]]
        >>> example_case_3 = [[-2],[-3,-4],[-6,-5,-7],[-4,-1,-8,-3]]


    Example 1:
        >>> sol.minimumTotal(example_case_1)
        11
        >>> sol.minimumTotalUpside(example_case_1)
        11

    Example 2:
        >>> sol.minimumTotal(example_case_2)
        -10
        >>> sol.minimumTotalUpside(example_case_2)
        -10

    Example 3:
        >>> sol.minimumTotal(example_case_3)
        -21
        >>> sol.minimumTotalUpside(example_case_3)
        -21
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
