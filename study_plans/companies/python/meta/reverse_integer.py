"""Meta Interview Question Practice List on LeetCode.

7. Reverse Integer on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 123
    >>> example_case_2 = -123
    >>> example_case_3 = 120

Example 1:
    >>> sol.reverse(example_case_1)
    321

Example 1:
    >>> sol.reverse(example_case_2)
    -321

Example 3:
    >>> sol.reverse(example_case_3)
    21
"""


class Solution:  # noqa: D101
    MAX = 2**31 - 1

    def reverse(self, num: int) -> int:
        """Return the number with its digits reversed.

        Number is assumed to be a signed 32 bit integer.
        Can not use 64 signed integers.

        Args:
            num (int): Integer to reverse

        Returns:
            int: Integer with its digits reversed
        """
        is_negative = num < 0
        output = 0
        # dodge funkiness with euclidean modulo versus remainder language differences
        curr_num = abs(num)
        while curr_num != 0:
            curr_num, mod = divmod(curr_num, 10)
            output *= 10
            output += mod
            if output > self.MAX:
                return 0
        return output * (-1 if is_negative else 1)
