"""Practice for Matrix Pattern of Dynamic Programming Essentials."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """Return the size of the largest square containing only '1's.

        Args:
            matrix (list[list[str]]): Given matrix to find square in

        Returns:
            int: maximum area of square
        """
        # initialize base case
        prev_row = [0] * (len(matrix[0]) + 1)

        max_area = 0
        for row in matrix:
            curr_row = [0]
            for idx, val in enumerate(row, start=1):
                curr_row.append(
                    (min(prev_row[idx], curr_row[-1], prev_row[idx - 1]) + 1)
                    if val == "1"
                    else 0,
                )
                max_area = max(max_area, curr_row[-1])
            prev_row = curr_row
        return max_area**2


def main() -> None:
    """221. Maximal Square on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [["1","0","1","0","0"],["1","0","1","1","1"],\
            ["1","1","1","1","1"],["1","0","0","1","0"]]
        >>> example_case_2 = [["0","1"],["1","0"]]
        >>> example_case_3 = [["0"]]
        >>> test_case_1 = [["1"]]
        >>> test_case_2 = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],\
            ["1","1","1","1"]]
        >>> test_case_3 = [["0","1"]]

    Example 1:
        >>> sol.maximalSquare(example_case_1)
        4

    Example 2:
        >>> sol.maximalSquare(example_case_2)
        1

    Example 3:
        >>> sol.maximalSquare(example_case_3)
        0

    Test 1:
        >>> sol.maximalSquare(test_case_1)
        1

    Test 2:
        >>> sol.maximalSquare(test_case_2)
        4

    Test 3:
        >>> sol.maximalSquare(test_case_3)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
