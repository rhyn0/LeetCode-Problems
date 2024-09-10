"""Daily Challenge on LeetCode for October 16: Problem #119 [Easy]."""

# Standard Library
import doctest
from functools import reduce
from operator import mul


class Solution:  # noqa: D101
    def getRow(self, row: int) -> list[int]:
        """Return coefficients from the row of Pascal's Triangle.

        Args:
            row (int): Which row to get

        Returns:
            int: Row in order from left to right
        """

        # each row of Pascal's Triangle is a binomial coefficient of that spot
        def factorial(n: int) -> int:
            return reduce(mul, range(1, n + 1), 1)

        return [
            factorial(row) // (factorial(i) * factorial(row - i))
            for i in range(row + 1)
        ]

    def getRowLinear(self, row: int) -> list[int]:
        """Return same as above but using faster algorithm."""
        # first entry is always 1
        answer = [1]
        # successive terms in a row have the following relationship
        #   nCr = nCr-1 * (n - r + 1) / r
        for i in range(1, row + 1):
            answer.append(answer[i - 1] * (row - i + 1) // i)
        return answer


def main() -> None:
    """119. Pascal's Triangle II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 3
        >>> example_case_2 = 0
        >>> example_case_3 = 1

    Example 1:
        >>> sol.getRow(example_case_1)
        [1, 3, 3, 1]
        >>> sol.getRowLinear(example_case_1)
        [1, 3, 3, 1]

    Example 2:
        >>> sol.getRow(example_case_2)
        [1]
        >>> sol.getRowLinear(example_case_2)
        [1]

    Example 3:
        >>> sol.getRow(example_case_3)
        [1, 1]
        >>> sol.getRowLinear(example_case_3)
        [1, 1]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
