"""Weekly Challenge for 2nd Week of July, 2023 on LeetCode."""

# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Return length of longest substring with at most k distinct characters.

        Args:
            s (str): String to search in
            k (int): Maximum number of distinct characters

        Returns:
            int: Longest length
        """
        if k == 0:
            return 0
        n = len(s)
        left = 0
        seen_chars = Counter(s[:k])
        longest_len = seen_chars.total()
        for right in range(k, n):
            seen_chars[s[right]] += 1
            while len(seen_chars) > k:
                if seen_chars[s[left]] == 1:
                    seen_chars.pop(s[left])
                else:
                    seen_chars[s[left]] -= 1
                left += 1
            longest_len = max(longest_len, seen_chars.total())

        return longest_len


def main() -> None:
    """340. Longest Substring with At Most K Distinct Characters on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "eceba", 2
        >>> example_case_2 = "aa", 1

    Example 1:
        >>> sol.lengthOfLongestSubstringKDistinct(*example_case_1)
        3

    Example 2:
        >>> sol.lengthOfLongestSubstringKDistinct(*example_case_2)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
