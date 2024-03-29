"""Daily Challenge for November 19 on LeetCode: Problem #1887[Medium]."""
# Standard Library
import doctest
from itertools import pairwise


class Solution:  # noqa: D101
    def reductionOperations(self, nums: list[int]) -> int:
        """Return number of operations to make all elements to min of array."""
        arranged = sorted(nums)
        levels_up = ans = 0
        for prev, curr in pairwise(arranged):
            if prev != curr:
                levels_up += 1
            ans += levels_up
        return ans


def main() -> None:
    """1887. Reduction Operations to Make the Array Elements Equal on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [5,1,3]
        >>> example_case_2 = [1,1,1]
        >>> example_case_3 = [1,1,2,2,3]

    Example 1:
        >>> sol.reductionOperations(example_case_1)
        3

    Example 2:
        >>> sol.reductionOperations(example_case_2)
        0

    Example 1:
        >>> sol.reductionOperations(example_case_3)
        4
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
