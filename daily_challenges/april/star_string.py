"""LeetCode Daily Challenge April 11, 2023."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def removeStars(self, s: str) -> str:
        """Return string after completing star removal operations.

        A star removal operation will remove a single star (*) character
        and the first non-star character to its left.

        Args:
            s (str): Valid string that will remove stars

        Returns:
            str: String after star removal.
        """
        result_str = []
        for char in s:
            if char == "*":
                result_str.pop()
            else:
                result_str.append(char)

        return "".join(result_str)

    def removeStarsTwoPointer(self, s: str) -> str:
        """Return same as above but using Two Pointer method."""
        result_str = [""] * len(s)
        j = 0
        for char in s:
            if char == "*":
                j -= 1
            else:
                result_str[j] = char
                j += 1

        return "".join(result_str[:j])


def main() -> None:
    """Removing Stars from a String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "leet**cod*e"
        >>> example_case_2 = "hello*****"

    Example 1:
        >>> sol.removeStars(example_case_1)
        'lecoe'
        >>> sol.removeStarsTwoPointer(example_case_1)
        'lecoe'

    Example 2:
        >>> sol.removeStars(example_case_2)
        ''
        >>> sol.removeStarsTwoPointer(example_case_2)
        ''
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
