"""Essentials of Dynamic Programming LCS Problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return length of longest common subsequence between input strings.

        Args:
            text1 (str): First string
            text2 (str): Second string

        Returns:
            int: length
        """
        n = len(text2)
        # grid of m rows, n columns
        prev_dp = [0] * (n + 1)
        for c1 in text1:
            dp = prev_dp.copy()
            # skip the empty string compare, always a 0
            for j, c2 in enumerate(text2, start=1):
                if c1 == c2:
                    dp[j] = prev_dp[j - 1] + 1
                else:
                    dp[j] = max(prev_dp[j], dp[j - 1])
            prev_dp = dp
        return prev_dp[-1]


def main() -> None:
    """1143. Longest Common Subsequence on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "abcde", "ace"
        >>> example_case_2 = "abc", "abc"
        >>> example_case_3 = "abc", "def"
        >>> test_case_1 = "ezupkr", "ubmrapg"

    Example 1:
        >>> sol.longestCommonSubsequence(*example_case_1)
        3

    Example 2:
        >>> sol.longestCommonSubsequence(*example_case_2)
        3

    Example 3:
        >>> sol.longestCommonSubsequence(*example_case_3)
        0

    Test 1:
        >>> sol.longestCommonSubsequence(*test_case_1)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
