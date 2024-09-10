"""Essentials of Dynamic Programming LIS Problem on LeetCode."""

# Standard Library
from bisect import bisect_left
import doctest


class Solution:  # noqa: D101
    def lengthOfLIS(self, nums: list[int]) -> int:
        """Return length of longest increasing subsequence in `nums`.

        Must be a strictly increasing subsequence

        Args:
            nums (list[int]): List of nums to use

        Returns:
            int: Length
        """
        subseq = [nums[0]]

        for num in nums[1:]:
            if num > subseq[-1]:
                subseq.append(num)
            else:
                # need to replace this one to reset subseq to bigger range
                alter_idx = bisect_left(subseq, num)
                subseq[alter_idx] = num

        return len(subseq)


def main() -> None:
    """300. Longest Increasing Subsequence on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [10,9,2,5,3,7,101,18]
        >>> example_case_2 = [0,1,0,3,2,3]
        >>> example_case_3 = [7,7,7,7,7,7,7]

    Example 1:
        >>> sol.lengthOfLIS(example_case_1)
        4

    Example 2:
        >>> sol.lengthOfLIS(example_case_2)
        4

    Example 3:
        >>> sol.lengthOfLIS(example_case_3)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
