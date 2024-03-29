"""Daily Challenge for November 9 on LeetCode: Problem #1759 [Medium]."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def countHomogenous(self, s: str) -> int:
        """Return the number of homogenous substrings in `s`.

        A homogenous substring is a substring made up of only one
        type of character.

        Args:
            s (str): Source string to extract substrings from

        Returns:
            int: Number of homogenous substrings
        """
        # initialized to 1, due to skip first cycle
        ans = 1
        streak = 1
        modulo = 10**9 + 7
        # index is behind by 1, to make backwards compare easier
        for idx, char in enumerate(s[1:], start=0):
            if char == s[idx]:
                streak += 1
            else:
                streak = 1
            ans = (ans + streak) % modulo
        return ans


def main() -> None:
    """1759. Count Number of Homogenous Substrings on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "abbcccaa"
        >>> example_case_2 = "xy"
        >>> example_case_3 = "zzzzz"
        >>> self_test_1 = "a"

    Example 1:
        >>> sol.countHomogenous(example_case_1)
        13

    Example 2:
        >>> sol.countHomogenous(example_case_2)
        2

    Example 3:
        >>> sol.countHomogenous(example_case_3)
        15

    Self Test 1:
        >>> sol.countHomogenous(self_test_1)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
