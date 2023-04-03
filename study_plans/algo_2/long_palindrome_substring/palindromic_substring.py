# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestPalindrome(self, in_str: str) -> str:  # spec
        """Return longest palindromic substring in given string.

        Args:
            in_str (str): given string

        Returns:
            str: longest palindromic substring inside of given string
        """
        long_len, long_start, long_end = 0, 0, 0
        size_n = len(in_str)
        for center in range(size_n):
            left = right = center
            while 0 <= left <= right < size_n and in_str[left] == in_str[right]:
                if right - left + 1 > long_len:
                    long_len, long_start, long_end = right - left + 1, left, right
                left -= 1
                right += 1

            # even len
            left, right = center, center + 1
            while 0 <= left <= right < size_n and in_str[left] == in_str[right]:
                if right - left + 1 > long_len:
                    long_len, long_start, long_end = right - left + 1, left, right
                left -= 1
                right += 1
        return in_str[long_start : long_end + 1]


def main():
    """Longest Palindromic Substring on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.longestPalindrome("babad")
        'bab'

    Example 2:
        >>> sol.longestPalindrome("cbbd")
        'bb'
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
