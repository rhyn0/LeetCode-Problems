"""Daily Challenge for June 14, 2025.

2566. Maximum Difference by Remapping a Digit

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 11891
    >>> example_case_2 = 90

Example 1:
    >>> sol.minMaxDifference(example_case_1)
    99009

Example 2:
    >>> sol.minMaxDifference(example_case_2)
    99
"""


class Solution:  # noqa: D101
    def minMaxDifference(self, num: int) -> int:
        """Return the maximum difference possible after remapping digits for a number.

        Remapping means that one digit will turn into one of the 10 digits possible.
        Can turn into itself. All occurrences of that digit are changed.

        Args:
            num (int): Number to remap

        Returns:
            int: Result of greatest value possible minus the smallest value possible
        """
        str_num = str(num)
        first_non_nine_digit = next((ch for ch in str_num if ch != "9"), "")
        # valid numbers cant start with 0, so first non-zero is first number
        # exception is 0, but then we can't make the value smaller anyway
        first_non_zero_digit = str_num[0]
        max_value = (
            int(str_num.replace(first_non_nine_digit, "9"))
            if first_non_nine_digit
            else num
        )
        min_value = int(str_num.replace(first_non_zero_digit, "0"))
        return max_value - min_value
