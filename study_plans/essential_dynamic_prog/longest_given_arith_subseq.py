"""Essentials of Dynamic Programming LIS problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestSubsequence(self, arr: list[int], diff: int) -> int:
        """Return the longest arithmetic subsequence from arr with given difference.

        Args:
            arr (list[int]): Numbers to create subsequence
            diff (int): Difference between elements in the arithmetic subseq

        Returns:
            int: Length of Longest increasing subsequence
        """
        dp = {}
        answer = 1
        for num in arr:
            before_num_len = dp.get(num - diff, 0)
            dp[num] = before_num_len + 1
            answer = max(answer, before_num_len + 1)

        return answer


def main() -> None:
    """1218. Longest Arithmetic Subsequence of Given Difference on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,2,3,4], 1
        >>> example_case_2 = [1,3,5,7], 1
        >>> example_case_3 = [1,5,7,8,5,3,4,2,1], -2
        >>> test_case_1 = [3,0,-3,4,-4,7,6], 3

    Example 1:
        >>> sol.longestSubsequence(*example_case_1)
        4

    Example 2:
        >>> sol.longestSubsequence(*example_case_2)
        1

    Example 3:
        >>> sol.longestSubsequence(*example_case_3)
        4

    Test 1:
        >>> sol.longestSubsequence(*test_case_1)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
