"""Meta Interview Question Practice List on LeetCode.

29. Divide Two Integers on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 10, 3
    >>> example_case_2 = 7, -3
    >>> test_case_1 = -2147483648, -1

Example 1:
    >>> sol.divide(*example_case_1)
    3
    >>> sol.divideLong(*example_case_1)
    3

Example 2:
    >>> sol.divide(*example_case_2)
    -2
    >>> sol.divideLong(*example_case_2)
    -2

Test 1:
    >>> sol.divide(*test_case_1)
    2147483647
    >>> sol.divideLong(*test_case_1)
    2147483647
"""


class Solution:  # noqa: D101
    MIN = -(2**31)
    MAX = 2**31 - 1
    HALF_MIN_INT = -1073741824  # MIN // 2

    def divide(self, dividend: int, divisor: int) -> int:
        """Return the integer quotient of doing dividend / divisor.

        Cannot use multiplication, division or modulo.
        Assume this is 32 signed bit operation, return maximum or minimum
        values for those if the quotient exceeds it.

        Args:
            dividend (int): dividend
            divisor (int): divisor, cannot be 0

        Returns:
            int: quotient
        """
        quot_is_negative = 2
        # handle the special edge case of MIN and -1
        if dividend == self.MIN and divisor == -1:
            return self.MAX

        if dividend > 0:
            quot_is_negative -= 1
            dividend = -dividend
        if divisor > 0:
            quot_is_negative -= 1
            divisor = -divisor

        high_doubling = divisor
        highest_power = -1
        while (
            # once we exceed HALF_MIN, the next step would be to underflow negative
            high_doubling >= self.HALF_MIN_INT
            # and remember they are negative numbers here
            and dividend <= high_doubling + high_doubling
        ):
            highest_power += highest_power
            high_doubling += high_doubling
        quot = 0
        while dividend <= divisor:
            # current fits in
            if dividend <= high_doubling:
                quot += highest_power
                dividend -= high_doubling
            high_doubling >>= 1
            highest_power >>= 1
        return quot if quot_is_negative == 1 else -quot

    def divideLong(self, dividend: int, divisor: int) -> int:
        """Return same as above using binary division."""
        quot_is_negative = 2
        # handle the special edge case of MIN and -1
        if dividend == self.MIN and divisor == -1:
            return self.MAX

        if dividend > 0:
            quot_is_negative -= 1
            dividend = -dividend
        if divisor > 0:
            quot_is_negative -= 1
            divisor = -divisor

        highest_power_of_two = 0
        while divisor >= self.HALF_MIN_INT and divisor + divisor >= dividend:
            highest_power_of_two += 1
            divisor += divisor

        quot = 0
        for bit in range(highest_power_of_two, -1, -1):
            if divisor >= dividend:
                dividend -= divisor
                quot -= 1 << bit
            # depending on language, might need to optimize for leading bit fill
            # which adds a +1 here, but Python uses twos complement so
            # negative numbers get 1's and positives get 0's
            divisor = divisor >> 1

        return quot if quot_is_negative == 1 else -quot
