# Standard Library
import doctest


class Solution:  # noqa: D101
    def partitionString(self, s: str) -> int:  # spec
        """Return number of substrings needed to make strings with unique characters.

        Easiest and simplest answer to come to.
        Time: O(n)
        Space: O(l) - number of unique characters in a substring
        """
        if len(set(s)) == 1:
            return len(s)

        substrings = 1
        seen_in_substring = set()
        for char in s:
            if char not in seen_in_substring:
                seen_in_substring.add(char)
            else:
                seen_in_substring.clear()
                seen_in_substring.add(char)
                substrings += 1
        return substrings

    def partitionString1Space(self, s: str) -> int:  # noqa: D102
        char_start = ord("a")
        # possible characters
        last_seen_idx = [-1] * 26
        substrings, substring_start = 1, 0
        for i, char in enumerate(s):
            if last_seen_idx[ord(char) - char_start] >= substring_start:
                substring_start = i
                substrings += 1
            last_seen_idx[ord(char) - char_start] = i

        return substrings


def main():
    """Optimal Partition of String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> test_case_1 = "abacaba"
        >>> test_case_2 = "ssssss"

    Example 1:
        >>> sol.partitionString(test_case_1)
        4
        >>> sol.partitionString1Space(test_case_1)
        4

    Example 2:
        >>> sol.partitionString(test_case_2)
        6
        >>> sol.partitionString1Space(test_case_2)
        6
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
