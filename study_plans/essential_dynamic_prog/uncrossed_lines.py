"""Essentials of Dynamic Programming LCS Problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        """Return maximum number of uncrossed lines feasible for input nums arrays.

        The nums arrays are printed on their own horizontal line.
        A line can be drawn between the two lines (number to number) if:
          - the numbers are equal
          - the line drawn doesn't cross any previously existing line
          - Lines cannot intersect at endpoints, each number at most once

        Which just becomes a problem on the length of the common subsequence.
        Arrays order can not be changed.

        Args:
            nums1 (list[int]): First input number array
            nums2 (list[int]): second input number array

        Returns:
            int: Length of longest common subsequence
        """
        # m + 1 rows, n + 1 columns
        n = len(nums2)
        prev_dp = [0] * (n + 1)
        for num1 in nums1:
            dp = prev_dp.copy()
            for j, num2 in enumerate(nums2, start=1):
                if num1 == num2:
                    dp[j] = prev_dp[j - 1] + 1
                else:
                    dp[j] = max(prev_dp[j], dp[j - 1])
            prev_dp = dp
        return prev_dp[-1]


def main() -> None:
    """1035. Uncrossed Lines on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,4,2], [1,2,4]
        >>> example_case_2 = [2,5,1,2,5], [10,5,2,1,5,2]
        >>> example_case_3 = [1,3,7,1,7,5], [1,9,2,5,1]

    Example 1:
        >>> sol.maxUncrossedLines(*example_case_1)
        2

    Example 2:
        >>> sol.maxUncrossedLines(*example_case_2)
        3

    Example 3:
        >>> sol.maxUncrossedLines(*example_case_3)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
