# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestPalindrome(self, in_str: str) -> str:
        """Return longest palindromic substring in given string.

        Args:
            in_str (str): given string

        Returns:
            str: longest palindromic substring inside of given string
        """
        long_len, long_start, long_end = 0, 0, 0
        size_n = len(in_str)

        def find_palindrome(left: int, right: int) -> None:
            nonlocal long_len, long_start, long_end
            while 0 <= left <= right < size_n and in_str[left] == in_str[right]:
                if right - left + 1 > long_len:
                    long_len, long_start, long_end = right - left + 1, left, right
                left -= 1
                right += 1

        for center in range(size_n):
            find_palindrome(center, center)
            # even len
            find_palindrome(center, center + 1)

        return in_str[long_start : long_end + 1]


def main() -> None:
    """Longest Palindromic Substring on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "babad"
        >>> example_case_2 = "cbbd"

    Example 1:
        >>> sol.longestPalindrome(example_case_1)
        'bab'

    Example 2:
        >>> sol.longestPalindrome(example_case_2)
        'bb'
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
