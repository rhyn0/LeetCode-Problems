# Standard Library
import doctest


class Solution:  # noqa: D101
    def rotate(self, matrix: list[list[int]]) -> None:
        """Rotate a given matrix 90 degrees clockwise.

        Can not make another 2D matrix and rotate it there.
        Update must be done to original object.

        Args:
            matrix (List[List[int]]): In-out parameter, representing matrix to rotate.
        """
        n_size = len(matrix)
        for row in range(n_size):
            for col in range(row + 1, n_size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            matrix[row].reverse()


def main() -> None:
    """Rotate Image on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> example_case_2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7],\
            [15, 14, 12, 16]]

    Example 1:
        >>> sol.rotate(example_case_1)
        >>> example_case_1
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    Example 2:
        >>> sol.rotate(example_case_2)
        >>> example_case_2
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
