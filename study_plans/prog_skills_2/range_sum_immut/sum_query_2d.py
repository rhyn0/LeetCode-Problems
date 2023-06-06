# Standard Library
import doctest


class NumMatrix:  # noqa: D101
    def __init__(self, matrix: list[list[int]]) -> None:
        """Precompute the num matrix to prepare for queries.

        Each position i, j is the sum of cells from 0, 0 to i, j.

        Args:
            matrix (List[List[int]]): Input number matrix
        """
        self.prefix_sum: list[list[int]] = [[0 for _ in matrix[0]] for _ in matrix]
        # sum for rectangle with top-left at 0,0
        for i, row in enumerate(matrix):
            for cell, val in enumerate(row):
                if i == 0:
                    self.prefix_sum[i][cell] = self.prefix_sum[i][cell - 1] + val
                elif cell == 0:
                    self.prefix_sum[i][cell] = self.prefix_sum[i - 1][cell] + val
                else:
                    self.prefix_sum[i][cell] = (
                        self.prefix_sum[i - 1][cell]
                        + self.prefix_sum[i][cell - 1]
                        + val
                        - self.prefix_sum[i - 1][cell - 1]
                    )

    def sumRegion(self, top: int, left: int, bot: int, right: int) -> int:
        """Return sum of a region defined by the bounds.

        Runs in O(1) time since all calculated an init

        Args:
            top (int): top row inclusive
            left (int): left column inclusive
            bot (int): bottom row inclusive
            right (int): right column inclusive

        Returns:
            int: sum of cells in the box defined
        """
        above = self.prefix_sum[top - 1][right] if top else 0
        side = self.prefix_sum[bot][left - 1] if left else 0
        diag = self.prefix_sum[top - 1][left - 1] if top and left else 0
        return self.prefix_sum[bot][right] - above - side + diag


def main() -> None:
    """Sum Region on LeetCode.

    ====================================================

    Setup:
        >>> example_matrix_1 = NumMatrix(\
            [\
                [3, 0, 1, 4, 2],\
                [5, 6, 3, 2, 1],\
                [1, 2, 0, 1, 5],\
                [4, 1, 0, 1, 7],\
                [1, 0, 3, 0, 5],\
            ])
        >>> example_case_1 = [2, 1, 4, 3]

    Example 1:
        >>> example_matrix_1.sumRegion(*example_case_1)
        8
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
