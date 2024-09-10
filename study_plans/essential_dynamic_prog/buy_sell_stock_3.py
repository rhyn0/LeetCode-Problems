# Standard Library
import doctest
from operator import add


class Solution:  # noqa: D101
    def maxProfit(self, prices: list[int]) -> int:
        """Return max profit achievable with at most two transactions.

        Transaction is one buy and sell pairing. Must buy before sell.

        Args:
            prices (list[int]): Price of the stock on day i

        Returns:
            int: Maximum amount of profit achievable
        """
        n = len(prices)
        if n <= 1:
            # no sale possible
            return 0

        left_buy, right_sell = prices[0], prices[-1]
        split1_profits, split2_profits = [0] * n, [0] * (n + 1)
        for left, right in zip(range(1, n), range(n - 2, -1, -1), strict=False):
            split1_profits[left] = max(
                split1_profits[left - 1],
                prices[left] - left_buy,
            )
            split2_profits[right] = max(
                split2_profits[right + 1],
                right_sell - prices[right],
            )

            left_buy = min(left_buy, prices[left])
            right_sell = max(right_sell, prices[right])

        return max(
            add(*item) for item in zip(split1_profits, split2_profits[1:], strict=False)
        )

    def maxProfitFSM(self, prices: list[int]) -> int:
        """Return same as above using FSM logic with no extra space."""
        # instead of making multiple passes through the array to figure it out
        # we know we can make at most 2 transactions, the split point
        # between sell_1 and buy_2 is important to note as it
        # means that profits from transaction 1 end up offsetting our costs
        # when we start transaction 2
        cost_t1 = cost_t2 = 10**6  # MAX_INT for given constraints
        profit_t1 = profit_t2 = 0
        for price in prices:
            cost_t1 = min(cost_t1, price)
            profit_t1 = max(profit_t1, price - cost_t1)
            # now effects of transaction one ripple into two
            # essentially price is lowered by however we made previous
            cost_t2 = min(cost_t2, price - profit_t1)
            profit_t2 = max(profit_t2, price - cost_t2)

        return profit_t2


def main() -> None:
    """Best Time to Buy and Sell Stock III on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [3,3,5,0,0,3,1,4]
        >>> example_case_2 = [1,2,3,4,5]
        >>> example_case_3 = [7,6,4,3,1]
        >>> test_case_1 = [14,9,10,12,4,8,1,16]

    Example 1:
        >>> sol.maxProfit(example_case_1)
        6
        >>> sol.maxProfitFSM(example_case_1)
        6

    Example 2:
        >>> sol.maxProfit(example_case_2)
        4
        >>> sol.maxProfitFSM(example_case_2)
        4

    Example 3:
        >>> sol.maxProfit(example_case_3)
        0
        >>> sol.maxProfitFSM(example_case_3)
        0

    Test 1:
        >>> sol.maxProfit(test_case_1)
        19
        >>> sol.maxProfitFSM(test_case_1)
        19
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
