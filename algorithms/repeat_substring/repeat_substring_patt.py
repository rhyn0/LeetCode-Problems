# Standard Library
import doctest


class Solution:  # noqa: D101
    def repeatedSubstringPattern(self, in_str: str) -> bool:  # spec
        """Return if there if s is made up of a repeated substr.

        Contiguous substring, must be more than one repeat.

        Args:
            in_str (str): Original string possibly made up of a repeated pattern

        Returns:
            bool: True if made up of repeated pattern, False otherwise
        """
        s_len = len(in_str)
        for substr_len in reversed(range(1, s_len // 2 + 1)):
            if (s_len / substr_len).is_integer():
                substr = in_str[:substr_len]
                if substr * (s_len // substr_len) == in_str:
                    return True
        return False


def main() -> None:
    """459. Repeated Substring Pattern on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "abab"
        >>> example_case_2 = "aba"
        >>> test_case_1 = "abcabcabcabc"

    Example 1:
        >>> sol.repeatedSubstringPattern(example_case_1)
        True

    Example 2:
        >>> sol.repeatedSubstringPattern(example_case_2)
        False

    Test 1:
        >>> sol.repeatedSubstringPattern(test_case_1)
        True
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
