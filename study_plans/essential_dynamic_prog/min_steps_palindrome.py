"""Essentials of Dynamic Programming LCS Problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def minInsertions(self, s: str) -> int:
        """Return minimum number of insertions to make `s` a palindrome.

        Args:
            s (str): String to turn into a palindrome

        Returns:
            int: minimum number of insertions necessary
        """
        # n + 1 rows, n + 1 columns
        n = len(s)
        prev_dp = [0] * (n + 1)
        for char1 in s:
            dp = prev_dp.copy()
            for j, char2 in enumerate(reversed(s), start=1):
                if char1 == char2:
                    dp[j] = prev_dp[j - 1] + 1
                else:
                    dp[j] = max(prev_dp[j], dp[j - 1])
            prev_dp = dp
        # return number of places that didn't match
        return n - prev_dp[-1]


def main() -> None:
    """1312. Minimum Insertion Steps to Make a String Palindrome on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "zzazz"
        >>> example_case_2 = "mbadm"
        >>> example_case_3 = "leetcode"

    Example 1:
        >>> sol.minInsertions(example_case_1)
        0

    Example 2:
        >>> sol.minInsertions(example_case_2)
        2

    Example 3:
        >>> sol.minInsertions(example_case_3)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
