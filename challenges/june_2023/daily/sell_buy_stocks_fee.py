"""Daily Challenge for June 22, 2023 on LeetCode."""

# Standard Library
import doctest
from functools import cache


class Solution:  # noqa: D101
    def maxProfit(self, prices: list[int], fee: int) -> int:
        """Return maximum profit possible from buying and selling stocks.

        Each selling transaction has a `fee` associated with it.
        Only one stock can be held at a time. A stock cannot be sold
        before it is bought.
        An implied restriction is that a stock cannot be bought and sold
        on the same day - mostly because the net from this is negative `fee`.

        Args:
            prices (list[int]): Prices for each day of a stock
            fee (int): amount lost after selling a stock

        Returns:
            int: Maximum profit to be made from these prices
        """
        n = len(prices)

        @cache
        def recurse_stocks(day: int, *, has_stock: bool) -> int:
            if day >= n:
                return 0

            # always have two end states, with stock or without
            if has_stock:
                profit = recurse_stocks(day + 1, has_stock=False) + prices[day] - fee
            else:
                profit = recurse_stocks(day + 1, has_stock=True) - prices[day]
            return max(profit, recurse_stocks(day + 1, has_stock=has_stock))

        return recurse_stocks(0, has_stock=False)

    def maxProfitBottomUp(self, prices: list[int], fee: int) -> int:
        """Return same as above using bottom up approach."""
        n = len(prices)
        have_stock, no_stock = [0] * n, [0] * n
        # to have stock on day 0, we must buy
        have_stock[0] = -prices[0]
        for i in range(1, n):
            have_stock[i] = max(have_stock[i - 1], no_stock[i - 1] - prices[i])
            no_stock[i] = max(no_stock[i - 1], have_stock[i - 1] + prices[i] - fee)

        return max(have_stock[-1], no_stock[-1])


def main() -> None:
    """714. Best Time to Buy and Sell Stock with Transaction Fee on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,3,2,8,4,9], 2
        >>> example_case_2 = [1,3,7,5,10,3], 3
        >>> self_test_1 = [1], 2

    Example 1:
        >>> sol.maxProfit(*example_case_1)
        8
        >>> sol.maxProfitBottomUp(*example_case_1)
        8

    Example 2:
        >>> sol.maxProfit(*example_case_2)
        6
        >>> sol.maxProfitBottomUp(*example_case_2)
        6

    Self Test 1:
        >>> sol.maxProfit(*self_test_1)
        0
        >>> sol.maxProfitBottomUp(*self_test_1)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
