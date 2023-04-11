"""LeetCode Daily Challenge April 10, 2023.

Previously answered this, but reformatting this file
to be more modern like other ones.
"""
import doctest


class Solution:  # noqa: D101
    def isValid(self, s: str) -> bool:
        """Return if string is a valid set of open/close parentheses.

        Valid only if each pair is open closed in order
        and with its proper pairing

        Args:
            s (str): string to validate

        Returns:
            bool: True if valid, False otherwise
        """
        stack = []
        open_close_pairs = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        for char in s:
            if char in open_close_pairs:
                stack.append(char)
            elif len(stack) and char == open_close_pairs[stack.pop()]:
                continue
            else:
                return False
        return len(stack) == 0


def main():
    """Valid Parentheses on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "()"
        >>> example_case_2 = "(){}[]"
        >>> example_case_3 = "(]"

    Example 1:
        >>> sol.isValid(example_case_1)
        True

    Example 2:
        >>> sol.isValid(example_case_2)
        True

    Example 3:
        >>> sol.isValid(example_case_3)
        False
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
