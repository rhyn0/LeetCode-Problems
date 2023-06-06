# Standard Library
import doctest


class Solution:  # noqa: D101
    def multiply(self, num1: str, num2: str) -> str:
        """Multiply two strings representing numbers, return result as string.

        Iterative approach.

        Args:
            num1 (str): String representing first positive number
            num2 (str): String representing second positive number

        Returns:
            str: String representing result of multiplying the two numbers together.
        """
        total = 0
        for i, c1 in enumerate(reversed(num1)):
            temp_total, power, carry = 0, 10**i, 0
            c1_val = ord(c1) - ord("0") if c1 is not None else 1
            for c2 in reversed(num2):
                c2_val = ord(c2) - ord("0") if c2 is not None else 1

                temp_val = (c1_val * c2_val) + carry
                carry = temp_val // 10
                temp_val = temp_val % 10

                temp_total += temp_val * power
                power *= 10

            temp_total += carry * power
            total += temp_total
        return str(total)


def main() -> None:
    """43. Multiply Strings on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "2", "3"
        >>> example_case_2 = "123", "456"

    Example 1:
        >>> sol.multiply(*example_case_1)
        '6'

    Example 2:
        >>> sol.multiply(*example_case_2)
        '56088'
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
