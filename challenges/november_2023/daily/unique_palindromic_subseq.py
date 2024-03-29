"""Daily Challenge for November 14 on LeetCode: Problem #1930 [Medium]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def countPalindromicSubsequence(self, s: str) -> int:
        """Return number of unique palindromic subsequences of length 3.

        String is made up of only lowercase English letters.

        Args:
            s (str): source string

        Returns:
            int: Number of unique subsequences
        """
        return sum(
            len(set(s[s.index(letter) + 1 : s.rindex(letter)])) for letter in set(s)
        )

    def countPalindromicSubsequenceBucket(self, s: str) -> int:
        """Return same as above using a bucket to store indices."""
        first = [-1] * 26
        last = [-1] * 26
        for idx, letter in enumerate(s):
            index = ord(letter) - ord("a")
            if first[index] == -1:
                first[index] = s.index(letter)
            last[index] = max(last[index], idx)

        return sum(
            len(set(s[first_idx + 1 : last_idx]))
            for first_idx, last_idx in zip(first, last, strict=True)
            if first_idx != -1
        )


def main() -> None:
    """1930. Unique Length-3 Palindromic Subsequences on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "aabca"
        >>> example_case_2 = "adc"
        >>> example_case_3 = "bbcbaba"

    Example 1:
        >>> sol.countPalindromicSubsequence(example_case_1)
        3
        >>> sol.countPalindromicSubsequenceBucket(example_case_1)
        3

    Example 2:
        >>> sol.countPalindromicSubsequence(example_case_2)
        0
        >>> sol.countPalindromicSubsequenceBucket(example_case_2)
        0

    Example 3:
        >>> sol.countPalindromicSubsequence(example_case_3)
        4
        >>> sol.countPalindromicSubsequenceBucket(example_case_3)
        4
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
