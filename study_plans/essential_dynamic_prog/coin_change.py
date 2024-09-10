"""Essentials of Dynamic Programming General 1D Problem on LeetCode.

322. Coin Change on LeetCode.

This has been previously solved as part of the Leet 75 - `../leet_75/coin_change`.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [1,2,5], 11
    >>> example_case_2 = [2], 3
    >>> example_case_3 = [1], 0

Example 1:
    >>> sol.coinChange(*example_case_1)
    3
    >>> sol.coinChangeBfs(*example_case_1)
    3

Example 2:
    >>> sol.coinChange(*example_case_2)
    -1
    >>> sol.coinChangeBfs(*example_case_2)
    -1

Example 3:
    >>> sol.coinChange(*example_case_3)
    0
    >>> sol.coinChangeBfs(*example_case_3)
    0
"""

# Standard Library
from collections import deque


class Solution:  # noqa: D101
    def coinChange(self, coins: list[int], amount: int) -> int:
        """Return the minimum number of coins necessary to make amount.

        Args:
            coins (list[int]): Denomination of coins available
            amount (int): Amount to sum up to

        Returns:
            int: -1 if no solution, otherwise number of coins
        """
        default_amount = amount + 1
        dp = [default_amount] * (amount + 1)
        # base case is that it takes no coins to make 0
        dp[0] = 0
        for subamount in range(1, amount + 1):
            for coin in coins:
                if coin > subamount:
                    continue
                dp[subamount] = min(
                    dp[subamount - coin] + 1,
                    dp[subamount],
                )

        return dp[amount] if dp[amount] != default_amount else -1

    def coinChangeBfs(self, coins: list[int], amount: int) -> int:
        """Return same as above using breadth first search.

        NOTE: this can cause Memory Limit Exceeded.
        """
        que = deque([(0, 0)])
        while que:
            curr_amount, num_coins = que.popleft()

            if curr_amount == amount:
                return num_coins
            for coin in coins:
                if coin + curr_amount > amount:
                    continue
                que.append((coin + curr_amount, num_coins + 1))
        return -1
