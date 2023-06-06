# Standard Library
import doctest


class Solution:  # noqa: D101
    def strStr(self, haystack: str, needle: str) -> int:  # spec
        """Find the string needle in the given string haystack.

        Manual implementation of str.index it seems.

        Args:
            haystack (str): Long string to search in
            needle (str): string target to find

        Returns:
            int: Position of needle in haystack, -1 if it doesn't exist.
        """
        if len(needle) == 0:
            return 0
        endpoint = -len(needle) + 1 or None
        for i, char in enumerate(haystack[slice(endpoint)]):
            if char == needle[0] and haystack[i : i + len(needle)] == needle:
                return i
        return -1


def main() -> None:
    """28. Find the Index of the First Occurrence in a String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "hello", "ll"
        >>> example_case_2 = "aaaaa", "bba"
        >>> self_test_1 = "aaa", ""
        >>> self_test_2 = "a", "a"

    Example 1:
        >>> sol.strStr(*example_case_1)
        2

    Example 2:
        >>> sol.strStr(*example_case_2)
        -1

    Self Test 1:
        >>> sol.strStr(*self_test_1)
        0

    Self Test 2:
        >>> sol.strStr(*self_test_2)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
