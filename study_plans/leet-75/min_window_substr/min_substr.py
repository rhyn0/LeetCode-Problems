# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def minWindow(self, s: str, t: str) -> str:  # spec
        """Return smallest substring of `s` such that an anagram of `t` is found.

        This is a leetcode hard problem.
        If there is no such substring of ``s``, returns empty string

        Args:
            s (str): master string to make a substring of
            t (str): characters and counts to find in ``s``

        Returns:
            str: Substring of s to encompass all of ``t``,
                else empty string if no such string
        """
        if not t:
            return ""

        curr_count, t_count = {}, Counter(t)
        start, have, need = 0, 0, len(t_count)
        length_min, result_slice = float("inf"), slice(None, None)
        for end, count in enumerate(s):
            curr_count[count] = curr_count.get(count, 0) + 1

            if count in t_count and curr_count[count] == t_count[count]:
                have += 1
            while have == need:
                if end - start + 1 < length_min:
                    length_min, result_slice = end - start + 1, slice(start, end + 1)
                curr_count[s[start]] -= 1
                if s[start] in t_count and curr_count[s[start]] < t_count[s[start]]:
                    have -= 1
                start += 1

        return s[result_slice] if length_min != float("inf") else ""


def main() -> None:
    """Minimum Window Substring on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.minWindow("ADOBECODEBANC", "ABC")
        'BANC'

    Example 2:
        >>> sol.minWindow("a", "a")
        'a'

    Example 3:
        >>> sol.minWindow("a", "aa")
        ''

    Test 1:
        >>> sol.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
        'abbbbbcdd'
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
