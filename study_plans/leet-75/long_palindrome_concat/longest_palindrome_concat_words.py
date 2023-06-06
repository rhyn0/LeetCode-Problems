# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def longestPalindrome(self, words: list[str]) -> int:  # spec
        """Find the longest palindrome by concatenating words in any order.

        All words are 2 letter strings of lowercase english alphabet. E.g. 'aa' 'ab' ...

        Args:
            words (List[str]): List of words

        Returns:
            int: Length of longest palindrome
        """
        counts = Counter(words)

        pal_used, length = False, 0
        for key, occurr in counts.most_common():
            min_occurr = min(occurr, counts[key[::-1]])
            if not pal_used and key[0] == key[1]:
                if min_occurr % 2 == 1:
                    pal_used = True
                length += min_occurr
            elif key[0] == key[1]:
                length += min_occurr - (min_occurr % 2)
            else:
                length += min_occurr * 2
            counts[key] = 0
        return length * 2


def main() -> None:
    """Longest Palindrome by Concatenating two Letter Words on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.longestPalindrome(["lc", "cl", "gg"])
        6

    Example 2:
        >>> sol.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"])
        8

    Example 3:
        >>> sol.longestPalindrome(["cc", "ll", "xx"])
        2

    Test 1:
        >>> sol.longestPalindrome(["cc", "cc", "cc"])
        6

    Test 2:
        >>> sol.longestPalindrome(["cc", "cc", "cc", "aa", "aa"])
        10

    Test 3:
        >>> sol.longestPalindrome(["io", "io"])
        0
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
