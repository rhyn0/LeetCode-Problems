"""Essentials of Dynamic Programming String Problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def numDistinct(self, s: str, t: str) -> int:
        """Return number of distinct subsequences in `s` that equal `t`.

        Args:
            s (str): Source string to make subsequence from
            t (str): string that subsequences must match

        Returns:
            int: Number of distinct subsequences
        """
        m, n = len(t), len(s)
        prev_dp = [1] * (n + 1)
        for i in range(m - 1, -1, -1):
            dp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                dp[j] = dp[j + 1] + (prev_dp[j + 1] if t[i] == s[j] else 0)

            prev_dp = dp

        return prev_dp[0]


def main() -> None:
    """115. Distinct Subsequences on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "rabbbit", "rabbit"
        >>> example_case_2 = "babgbag", "bag"

    Example 1:
        >>> sol.numDistinct(*example_case_1)
        3

    Example 2:
        >>> sol.numDistinct(*example_case_2)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
