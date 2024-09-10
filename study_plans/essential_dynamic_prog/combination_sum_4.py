"""Essentials of Dynamic Programming Knapsack Problem on LeetCode.

Combination Sum IV on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [1,2,3], 4
    >>> example_case_2 = [9], 3

Example 1:
    >>> sol.combinationSum4(*example_case_1)
    7
    >>> sol.combinationSum4Tab(*example_case_1)
    7

Example 2:
    >>> sol.combinationSum4(*example_case_2)
    0
    >>> sol.combinationSum4Tab(*example_case_2)
    0
"""

# Standard Library
from functools import cache


class Solution:  # noqa: D101
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """Return the total number of combinations that sum up to target from nums.

        Note that each number in `nums` has unlimited uses. Order of nums
        to create the summing sequence matters.
        target = 3, solutions: [1,2] [2,1] are different.

        Args:
            nums (list[int]): List of numbers available to use
            target (int): target sum

        Returns:
            int: Total number of combinations
        """
        n = len(nums)
        # if nums is empty, this causes a runtime error on `sum()` call
        if n == 0:
            return 0

        @cache
        def dfs(subtarget: int) -> int:
            if subtarget == 0:
                # succesfully created target
                return 1
            if subtarget < 0:
                return 0

            return sum(dfs(subtarget - num) for num in nums)

        return dfs(target)

    def combinationSum4Tab(self, nums: list[int], target: int) -> int:
        """Return same as above using bottom up approach."""
        dp = [0] * (target + 1)
        # if we can create reduce to 0, then we have a solution
        dp[0] = 1

        for subtarget in range(1, target + 1):
            for num in nums:
                if subtarget >= num:
                    dp[subtarget] += dp[subtarget - num]
        return dp[target]
