# Standard Library
import doctest


class Solution:  # noqa: D101
    def lengthOfLastWord(self, s: str) -> int:  # spec
        """Return length of last word in a string.

        Word is given by set of characters not interrupted by spaces

        Args:
            s (str): String to parse

        Returns:
            int: Length of last word in string
        """
        # return len(s.split()[-1])
        curr_len, last = 0, 0
        for char in s:
            if char.isspace():
                if curr_len != 0:
                    curr_len, last = 0, curr_len
            else:
                curr_len += 1
        return curr_len or last


def main() -> None:
    """58. Length of Last Word on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "hello world"
        >>> example_case_2 = "   fly me   to   the moon  "
        >>> self_test_1 = "luffy is still joyboy"

    Example 1:
        >>> sol.lengthOfLastWord(example_case_1)
        5

    Example 2:
        >>> sol.lengthOfLastWord(example_case_2)
        4

    Self Test 1:
        >>> sol.lengthOfLastWord(self_test_1)
        6
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
