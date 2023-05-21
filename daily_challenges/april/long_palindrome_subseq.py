"""Daily Challenge from April 14, 2023."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestPalindromeSubseq(self, s: str) -> int:
        """Return length of longest palindrome subsequence of string.

        Subsequence is string with some or no characters removed.
        Palindrome is a sequence of characters that is same
        forward and backwards.

        Args:
            s (str): string to find palindromic subsequence in

        Returns:
            int: length of the longest subsequence
        """
        str_len = len(s)
        dp, prev_dp = [0] * str_len, [0] * str_len
        # start from end of string
        for i in range(str_len - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, str_len):
                if s[i] == s[j]:
                    dp[j] = 2 + prev_dp[j - 1]
                else:
                    # either include i char or include j char
                    dp[j] = max(prev_dp[j], dp[j - 1])
            prev_dp = dp[:]

        return prev_dp[str_len - 1]


def main():
    """Longest Palindromic Subsequence on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "bbbab"
        >>> example_case_2 = "cbbd"

    Example 1:
        >>> sol.longestPalindromeSubseq(example_case_1)
        4

    Example 2:
        >>> sol.longestPalindromeSubseq(example_case_2)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
