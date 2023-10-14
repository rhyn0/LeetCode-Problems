"""Daily Challenge for June 8, 2023 on LeetCode."""
# Standard Library
from bisect import bisect_right
import doctest


class Solution:  # noqa: D101
    def countNegatives(self, grid: list[list[int]]) -> int:
        """Return count of negative numbers in a non-increasing sorted matrix.

        Matrix is sorted non-increasingly in both the rows and columns.
        For any value in a row, all values right of it are less than or equal.
        For that same value in its column, all values below are the same.

        Args:
            grid (list[list[int]]): non-increasing sorted matrix

        Returns:
            int: Count of negative numbers
        """
        return sum(val < 0 for row in grid for val in row)

    def countNegativesBisect(self, grid: list[list[int]]) -> int:
        """Return same as above using binary search from bisect."""
        n = len(grid[0])
        return sum(n - bisect_right(row, 0, key=lambda x: -x) for row in grid)

    def countNegativesSelfBin(self, grid: list[list[int]]) -> int:
        """Return same as above using binary search from scratch."""
        n = len(grid[0])

        def _bin_search(arr: list[int]) -> int:
            left, right = 0, n - 1
            # arr is still sorted in decreasing order
            while left <= right:
                # create left as index of first neg element
                mid = (left + right) // 2
                if arr[mid] < 0:
                    right = mid - 1
                else:
                    # we don't want left to land on this non-neg value
                    left = mid + 1

            return n - left

        return sum(_bin_search(row) for row in grid)

    def countNegativesLinear(self, grid: list[list[int]]) -> int:
        """Return same as above using binary search from linear traversal."""
        n = len(grid[0])
        negative_idx, total_negatives = n - 1, 0
        for row in grid:
            while negative_idx >= 0 and row[negative_idx] < 0:
                negative_idx -= 1
            total_negatives += n - (negative_idx + 1)
        return total_negatives


def main() -> None:
    """1351. Count Negative Numbers in a Sorted Matrix on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        >>> example_case_2 = [[3,2],[1,0]]

    Example 1:
        >>> sol.countNegatives(example_case_1)
        8
        >>> sol.countNegativesBisect(example_case_1)
        8
        >>> sol.countNegativesSelfBin(example_case_1)
        8
        >>> sol.countNegativesLinear(example_case_1)
        8

    Example 2:
        >>> sol.countNegatives(example_case_2)
        0
        >>> sol.countNegativesBisect(example_case_2)
        0
        >>> sol.countNegativesSelfBin(example_case_2)
        0
        >>> sol.countNegativesLinear(example_case_2)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
