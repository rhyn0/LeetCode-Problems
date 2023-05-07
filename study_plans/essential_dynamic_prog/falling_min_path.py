"""Practice for Matrix Pattern of Dynamic Programming Study Plan."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    @staticmethod
    def min_of_window(array: list[int], curr_idx: int, *, window_size: int = 3) -> int:
        """Return minimum of a window in the given array centered on given index.

        Args:
            array (list[int]): given array to create window in
            curr_idx (int): Index to center window on
            window_size (int, optional): Number of elements in window to consider.
                Should be an odd number. Defaults to 3.

        Returns:
            int: Minimum of the window
        """
        if window_size % 2 == 0:
            window_size += 1
        # inclusive on end of range
        return min(
            array[
                max(curr_idx - window_size // 2, 0) : (curr_idx + window_size // 2) + 1
            ]
        )

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        """Return minimum path from top row to bottom row.

        From current cell index `i`, can move to one of the cells in the row below
        of indices: `i - 1`, `i`, `i + 1`

        Args:
            matrix (list[list[int]]): Layout of matrix to traverse

        Returns:
            int: Minimum path weight
        """
        prev_row = matrix[0]
        for row in matrix[1:]:
            curr_row = [
                self.min_of_window(prev_row, idx) + value
                for idx, value in enumerate(row)
            ]
            prev_row = curr_row
        return min(prev_row)


def main():
    """931. Minimum Falling Path Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[2,1,3],[6,5,4],[7,8,9]]
        >>> example_case_2 = [[-19,57],[-40,-5]]

    Example 1:
        >>> sol.minFallingPathSum(example_case_1)
        13

    Example 2:
        >>> sol.minFallingPathSum(example_case_2)
        -59
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
