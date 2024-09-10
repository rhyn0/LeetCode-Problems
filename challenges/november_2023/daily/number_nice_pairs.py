"""Daily Challenge for November 21 on LeetCode: Problem #1814 in an Array [Medium]."""

# Standard Library
from collections import defaultdict
import doctest
import math


class Solution:  # noqa: D101
    def countNicePairs(self, nums: list[int]) -> int:
        """Return number of nice pairs in given array.

        Nice pair is a pair (i, j) where i < j and
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]).

        Args:
            nums (list[int]): array of integers

        Returns:
            int: Total number of pairs
        """
        modulo = 10**9 + 7

        def expr(n: int) -> int:
            # return the value of n - rev(n)
            return n - int(str(n)[::-1])

        expr_appearances = defaultdict(int)
        for num in nums:
            expr_appearances[expr(num)] += 1
        return sum(math.comb(v, 2) for v in expr_appearances.values() if v > 1) % modulo


def main() -> None:
    """1814. Count Nice Pairs in an Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [42,11,1,97]
        >>> example_case_2 = [13,10,35,24,76]

    Example 1:
        >>> sol.countNicePairs(example_case_1)
        2

    Example 2:
        >>> sol.countNicePairs(example_case_2)
        4
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
