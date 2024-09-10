"""Essentials of Dynamic Programming State Machine Problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def maxProfit(self, prices: list[int]) -> int:
        """Return maximum profit available by selling a trading a stock with prices.

        Only one action can be held per day. When selling the stock, it incurs a
        cooldown period of one day. So if stock is sold on day 2, on day 3 no actions
        can be taken.

        Args:
            prices (list[int]): List of prices per day

        Returns:
            int: maximum profit achievable
        """
        n = len(prices)
        have_stock, no_stock = [0] * n, [0] * (n + 1)
        # have stock case is that we must buy on day 1
        have_stock[0] = -prices[0]
        for i in range(1, n):
            have_stock[i] = max(have_stock[i - 1], no_stock[i - 1] - prices[i])
            no_stock[i + 1] = max(
                no_stock[i - 1],
                no_stock[i],
                have_stock[i - 1] + prices[i],
            )
        return max(have_stock[-1], no_stock[-1])

    def maxProfitFSM(self, prices: list[int]) -> int:
        """Return same as above using a clear finite state machine."""
        # define 3 states: bought, sold, reset
        # which denote: having stock, just sold stock, no stock and able to trade
        # MIN_INT is -1500 as this is greater than negative of greatest price
        min_int = -1500
        bought, sold, reset = min_int, min_int, 0

        for price in prices:
            # can inline without temp variables
            # bought, sold, reset = (
            #   max(bought, reset - price), bought + price, max(reset, sold)
            # )
            # sold is the only state with no 'stay' action
            prev_sold = sold
            sold = bought + price
            # bought state is reachable from reset or bought
            #    reset -> bought involves a buy transaction
            bought = max(bought, reset - price)
            # reset state can occur via 'stay' or a cooldown from sold
            #    neither action involves money, so just maximum of prev states
            reset = max(reset, prev_sold)

        # max value can only be achieved when we don't end on having stock
        return max(reset, sold)


def main() -> None:
    """309. Best Time to Buy and Sell Stock with Cooldown on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,2,3,0,2]
        >>> example_case_2 = [1]
        >>> test_case_1 = [1,4,2]

    Example 1:
        >>> sol.maxProfit(example_case_1)
        3
        >>> sol.maxProfitFSM(example_case_1)
        3

    Example 2:
        >>> sol.maxProfit(example_case_2)
        0
        >>> sol.maxProfitFSM(example_case_2)
        0

    Test 1:
        >>> sol.maxProfit(test_case_1)
        3
        >>> sol.maxProfitFSM(test_case_1)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
