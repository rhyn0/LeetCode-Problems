"""Essentials of Dynamic Programming State Machine Problem on LeetCode.

188. Best Time to Buy and Sell Stock IV on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 2, [2, 4, 1]
    >>> example_case_2 = 2, [3, 2, 6, 5, 0, 3]

Example 1:
    >>> sol.maxProfit(*example_case_1)
    2

Example 2:
    >>> sol.maxProfit(*example_case_2)
    7
"""


class Solution:  # noqa: D101
    def maxProfit(self, k: int, prices: list[int]) -> int:
        """Return maximum profit from buying and selling stocks.

        Can only complete at most k transactions. A transaction is a buy and a sell.
        Can not buy and sell on the same day. Have to buy before selling.

        Args:
            k (int): Maximum number of transactions.
            prices (list[int]): Prices for a stock on each day.

        Returns:
            int: Maximum profit available.
        """
        # use a state machine approach
        # each transaction trickles into the next, such as profit of second trade
        # is affected by the first trade
        costs = [10**3] * k
        profits = [0] * k
        for price in prices:
            for i in range(k):
                costs[i] = min(costs[i], price - profits[i - 1] if i > 0 else price)
                profits[i] = max(profits[i], price - costs[i])

        return profits[-1]
