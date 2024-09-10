"""Essentials of Dynamic Programming Knapsack Problem on LeetCode.

Coin Change II on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 5, [1,2,5]
    >>> example_case_2 = 3, [2]
    >>> example_case_3 = 10, [10]

Example 1:
    >>> sol.change(*example_case_1)
    4
    >>> sol.changeManualMemo(*example_case_1)
    4
    >>> sol.changeDP(*example_case_1)
    4
    >>> sol.changeDpSpace(*example_case_1)
    4

Example 2:
    >>> sol.change(*example_case_2)
    0
    >>> sol.changeManualMemo(*example_case_2)
    0
    >>> sol.changeDP(*example_case_2)
    0
    >>> sol.changeDpSpace(*example_case_2)
    0

Example 3:
    >>> sol.change(*example_case_3)
    1
    >>> sol.changeManualMemo(*example_case_3)
    1
    >>> sol.changeDP(*example_case_3)
    1
    >>> sol.changeDpSpace(*example_case_3)
    1
"""

# Standard Library
from collections import defaultdict
from functools import cache


class Solution:  # noqa: D101
    def change(self, amount: int, coins: list[int]) -> int:
        """Return the number of ways to make the `amount` using the `coins`.

        Args:
            amount (int): Amount of change to make up
            coins (list[int]): Denomination of coins to use, unlimited quantity

        Returns:
            int: Number of ways
        """
        n = len(coins)

        @cache
        def dfs(coin_idx: int, subamount: int) -> int:
            if subamount == 0:
                return 1
            if subamount < 0:
                return 0
            if coin_idx == n:
                return 0

            # recursive step
            return dfs(coin_idx, subamount - coins[coin_idx]) + dfs(
                coin_idx + 1,
                subamount,
            )

        return dfs(0, amount)

    def changeManualMemo(self, amount: int, coins: list[int]) -> int:
        """Return same as above but using an explicit controlled cache.

        ! NOTE: this has Time Limit Exceeded (TLE)
        """
        n = len(coins)

        cache: defaultdict[tuple[int, int], int] = defaultdict(int)

        def dfs(coin_idx: int, subamount: int) -> int:
            if subamount == 0:
                return 1
            if subamount < 0:
                return 0
            if coin_idx == n:
                return 0

            index = (coin_idx, subamount)
            # use walrus to skip the double lookup
            if cached_val := cache[index]:
                return cached_val
            # recursive step
            rv = dfs(coin_idx, subamount - coins[coin_idx]) + dfs(
                coin_idx + 1,
                subamount,
            )
            cache[index] = rv
            return rv

        return dfs(0, amount)

    def changeDP(self, amount: int, coins: list[int]) -> int:
        """Return same as above using a full 2D tabulation approach."""
        # create buffer to avoid out of bound index access
        n = len(coins) + 1
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        # set goal factor for DP. if we can reach zero from our current amount
        # then we have made a valid combination
        for i in range(n):
            dp[i][0] = 1

        for i, coin_amount in enumerate(coins, start=1):
            for curr_amount in range(1, amount + 1):
                # available solutions at this point is always additive to prior
                # doesn't matter amount
                dp[i][curr_amount] = dp[i - 1][curr_amount]
                if curr_amount - coin_amount >= 0:
                    same_coin_prior_amount = dp[i][curr_amount - coin_amount]
                    dp[i][curr_amount] += same_coin_prior_amount

        return dp[-1][-1]

    def changeDpSpace(self, amount: int, coins: list[int]) -> int:
        """Return same as above using space-optimized dynamic programming."""
        prev_row = [0 for _ in range(amount + 1)]
        prev_row[0] = 1

        for coin_amount in coins:
            new_row = [1]
            for curr_amount in range(1, amount + 1):
                val = prev_row[curr_amount]
                if curr_amount >= coin_amount:
                    val += new_row[curr_amount - coin_amount]
                new_row.append(val)
            prev_row = new_row
        return prev_row[-1]
