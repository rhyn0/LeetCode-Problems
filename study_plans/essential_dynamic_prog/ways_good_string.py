"""Essentials of Dynamic Programming General 1D Problem on LeetCode.

2466. Count Ways to Build Good Strings on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 3, 3, 1, 1
    >>> example_case_2 = 2, 3, 1, 2
    >>> test_case_1 = 1, 100000, 1, 1

Example 1:
    >>> sol.countGoodStrings(*example_case_1)
    8
    >>> sol.countGoodStringsMemo(*example_case_1)
    8

Example 2:
    >>> sol.countGoodStrings(*example_case_2)
    5
    >>> sol.countGoodStringsMemo(*example_case_2)
    5

Test 1:
    >>> sol.countGoodStrings(*test_case_1)
    215447031
    >>> sol.countGoodStringsMemo(*test_case_1)
    215447031
"""

# Standard Library
import sys

# need this because of the insane test_case_1 size
sys.setrecursionlimit(110_000)


class Solution:  # noqa: D101
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """Return the number of 'good strings' that can be made.

        A good string is a string starting from empty and then appending
        either `zero` 0's or `one` 1's to it. This appending can be repeated
        unlimited times, but its length must be [low, high]

        Args:
            low (int): Minimum (inclusive) length of a good string
            high (int): Maximum (inclusive) length of a good string
            zero (int): Number of 0's to append at a step
            one (int): Number of 1's to append at a step

        Returns:
            int: Number of good strings creatable, modulo  10**9 + 7.
        """
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        # add to answer as we iterate, avoids extra iteration at end
        rv = 0
        for curr_len in range(1, high + 1):
            can_add_zero = dp[curr_len - zero] if curr_len >= zero else 0
            can_add_one = dp[curr_len - one] if curr_len >= one else 0
            # important to do modulo math often to keep the numbers smaller
            # which makes the summation "faster"
            dp[curr_len] = can_add_one % mod + can_add_zero % mod
            if curr_len >= low:
                rv = (rv + dp[curr_len]) % mod

        return rv

    def countGoodStringsMemo(self, low: int, high: int, zero: int, one: int) -> int:
        """Return same as above using memoization."""
        # instead of using functools.cache, use manual memoization since indices are int
        mod = 10**9 + 7
        memo = [-1] * (high + 1)

        def helper(curr_length: int) -> int:
            if curr_length > high:
                return 0
            if (rv := memo[curr_length]) != -1:
                return rv

            # start counting results only greater equal low
            memo[curr_length] = int(curr_length >= low)

            memo[curr_length] += (
                helper(curr_length + zero) + helper(curr_length + one)
            ) % mod
            return memo[curr_length]

        return helper(0)
