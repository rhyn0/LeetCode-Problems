"""Daily Challenge for April 13, 2025.

1922. Count Good Numbers on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 1
    >>> example_case_2 = 4

Example 1:
    >>> sol.countGoodNumbers(example_case_1)
    5
    >>> sol.countGoodNumbersMath(example_case_1)
    5
    >>> sol.countGoodNumbersBit(example_case_1)
    5

Example 2:
    >>> sol.countGoodNumbers(example_case_2)
    400
    >>> sol.countGoodNumbersMath(example_case_2)
    400
    >>> sol.countGoodNumbersBit(example_case_2)
    400
"""

# Standard Library
from functools import cache


class Solution:  # noqa: D101
    MOD = 10**9 + 7

    def countGoodNumbers(self, n: int) -> int:
        """Return the number of good number strings that are of length `n`.

        A good number is one that has even digits at its (0-indexed) even
        indices and prime digits at the odd indices.

        NOTE: this will cause RecursionError at high `n` so unlikely to
        pass the test cases.

        Args:
            n (int): Length of the digit string to test

        Returns:
            int: Total number of good numbers mod 10^9 + 7
        """

        @cache
        def recurse_helper(curr_index: int) -> int:
            if curr_index == 0:
                return 5

            # if even index we use even numbers (5)
            # if odd index we use prime numbers (4)
            options = 5 if curr_index % 2 == 0 else 4
            return (options * recurse_helper(curr_index - 1)) % self.MOD

        # length `n` starts at index `n- 1`
        return recurse_helper(n - 1) % self.MOD

    def countGoodNumbersMath(self, n: int) -> int:
        """Return same as above using math.

        NOTE: TLE can occur here due to the time taken
        to do ceil and floor math.

        Time: O(1) - kind of depends on hardware and also underlying Python.
        Space: O(1)
        """
        evens = (n + 1) // 2
        odds = n // 2
        return (5**evens * 4**odds) % self.MOD  # type: ignore[no-any-return]

    def countGoodNumbersBit(self, n: int) -> int:
        """Return same as above using math and bit checking.

        Use binary exponentiation to speed up power calculations.

        Time: O(log n) - due to our custom bin expon
        Space: O(1)
        """

        def bin_expon(base: int, power: int) -> int:
            result = 1
            while power > 0:
                if power & 1:
                    result = result * base % self.MOD
                # update base and power for next loop
                base = base * base % self.MOD
                power >>= 1
            return result

        evens = (n + 1) // 2
        odds = n // 2
        return (bin_expon(5, evens) * bin_expon(4, odds)) % self.MOD  # type: ignore[no-any-return]
