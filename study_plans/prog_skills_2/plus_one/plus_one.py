# Standard Library
import doctest


class Solution:  # noqa: D101
    def plusOne(self, digits: list[int]) -> list[int]:
        """Given a list of digits representing a number, add one.

        List of digits is in order of most significant digit to
        least significant, left to right.

        Args:
            digits (List[int]): List of digits

        Returns:
            List[int]: List of digits after adding one.
        """
        return [int(tok) for tok in str(int("".join(str(d) for d in digits)) + 1)]


def main() -> None:
    """66. Plus One on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1, 2, 3]
        >>> example_case_2 = [4, 3, 2, 1]
        >>> self_test_1 = [9]

    Example 1:
        >>> sol.plusOne(example_case_1)
        [1, 2, 4]

    Example 2:
        >>> sol.plusOne(example_case_2)
        [4, 3, 2, 2]

    Self Test 1:
        >>> sol.plusOne(self_test_1)
        [1, 0]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
