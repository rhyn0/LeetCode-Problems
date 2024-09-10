"""Essentials of Dynamic Programming Knapsack Problem on LeetCode.

279. Perfect Squares on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 12
    >>> example_case_2 = 13

Example 1:
    >>> sol.numSquares(example_case_1)
    3
    >>> sol.numSquaresMemo(example_case_1)
    3
    >>> sol.numSquaresBfs(example_case_1)
    3

Example 2:
    >>> sol.numSquares(example_case_2)
    2
    >>> sol.numSquaresMemo(example_case_2)
    2
    >>> sol.numSquaresBfs(example_case_2)
    2
"""

# Standard Library
from collections import deque
from functools import cache
import math


class Solution:  # noqa: D101
    def numSquares(self, n: int) -> int:
        """Return the minimum number of perfect squares needed to sum up to `n`.

        Perfect square is defined as an integer whose square root is an integer
        that when multiplied against itself equals the original integer.

        Args:
            n (int): target sum

        Returns:
            int: Minimum number of perfect squares
        """
        # bottom up approach
        tab = [0 for _ in range(n + 1)]
        for num in range(1, int(math.sqrt(n)) + 1):
            square = num * num
            if square > n:
                # greater than target sum, can't contribute
                # all numbers after this will also be greater so early exit
                break
            for idx in range(1, n + 1):
                # if we can get away with only using `square` to build this number
                if idx % square == 0:
                    # need `idx // square` copies of `square` to create the sum `idx`
                    tab[idx] = idx // square
                else:
                    # if its not clean, use leftovers from smaller numbers
                    tab[idx] = min(idx // square + tab[idx % square], tab[idx])
        # last value is `n` by 0 indexing, so return the best result for it
        return tab[-1]

    def numSquaresMemo(self, n: int) -> int:
        """Return same as above using top down approach.

        This code is hard to run for Python without TLE issues.
        Lots of micro optimizations have made it pass a few times.
        """

        @cache
        def dp(num: int) -> int:
            if num < 0:
                return 10_000
            if num == 0:
                return 0

            minimum = 100_000
            for val in range(1, 101):
                square = val * val
                if square > num:
                    break
                minimum = min(minimum, dp(num - square) + 1)
            return minimum

        return dp(n)

    def numSquaresBfs(self, n: int) -> int:
        """Return same as above using BFS approach."""
        if n < 0:
            return 0
        que = deque([n])
        visited = {n}

        # keep track of how many nums we have used to reach our current sum
        total_nums = 0
        while que:
            size = len(que)
            total_nums += 1
            for _ in range(size):
                curr_val = que.popleft()
                for i in range(1, int(math.sqrt(curr_val)) + 1):
                    # our newest target to sum up to
                    remainder = curr_val - i * i
                    # we reached the sum, any other combination after this is either
                    # the same or greater amoutn of numbers
                    if remainder == 0:
                        return total_nums
                    # dont do additional work for numbers visited
                    if remainder not in visited:
                        visited.add(remainder)
                        que.append(remainder)

        return total_nums
