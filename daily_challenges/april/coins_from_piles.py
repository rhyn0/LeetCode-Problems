"""Daily Challenge for April 15, 2023."""

# Standard Library
import doctest
from functools import cache


class Solution:  # noqa: D101
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        """Return maximum value of coins possible from selecting from piles.

        All coins are stacked in pile, each pile is represented as a list in
        ``piles``. The top of a pile is the 0th index, and the bottom is the last.
        Coins can only be selected from the top of the pile, pick more coins from
        a pile to expose the lower ones.

        Args:
            piles (list[list[int]]): Array of piles to use
            k (int): Maximum number of coins to pickup

        Returns:
            int: Maximized value of coins that can be picked up
        """
        prev_dp = [0] * (k + 1)

        for pile in piles:
            # need to include 0 at beginning
            dp = [0] * (k + 1)
            # picking 0 coins is always 0, its pre initialized
            for total_coins in range(1, k + 1):
                previous_pile_prefix = 0
                for previously_used_coin in range(min(len(pile), total_coins) + 1):
                    if previously_used_coin > 0:
                        previous_pile_prefix += pile[previously_used_coin - 1]
                    dp[total_coins] = max(
                        dp[total_coins],
                        prev_dp[total_coins - previously_used_coin]
                        + previous_pile_prefix,
                    )
            prev_dp = dp

        return prev_dp[k]

    def maxValueOfCoinsMemo(self, piles: list[list[int]], k: int) -> int:
        """Return same as above using memoization."""

        @cache
        def search_subproblem(avail_coins: int, pile_available: int) -> int:
            # pile available is the greatest index of pile that we can use
            if avail_coins == 0 or pile_available < 0:
                return 0

            subproblem_max_val = search_subproblem(avail_coins, pile_available - 1)

            curr_pile = piles[pile_available]
            curr_pile_prefix = 0
            for curr_use_coin in range(min(avail_coins, len(curr_pile))):
                # coins here are 0 indexed, affects the total number of coin
                curr_pile_prefix += curr_pile[curr_use_coin]

                subproblem_max_val = max(
                    subproblem_max_val,
                    curr_pile_prefix
                    + search_subproblem(
                        avail_coins - curr_use_coin - 1,
                        pile_available - 1,
                    ),
                )
            return subproblem_max_val

        return search_subproblem(k, len(piles) - 1)


def main() -> None:
    """Maximum Value of K Coins From Piles on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([[1,100,3],[7,8,9]], 2)
        >>> example_case_2 = ([[100],[100],[100],[100],[100],[100],\
            [1,1,1,1,1,1,700]], 7)
        >>> test_case_1 = ([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]], 9)

    Example 1:
        >>> sol.maxValueOfCoins(*example_case_1)
        101
        >>> sol.maxValueOfCoinsMemo(*example_case_1)
        101

    Example 2:
        >>> sol.maxValueOfCoins(*example_case_2)
        706
        >>> sol.maxValueOfCoinsMemo(*example_case_2)
        706

    Test 1:
        >>> sol.maxValueOfCoins(*test_case_1)
        494
        >>> sol.maxValueOfCoinsMemo(*test_case_1)
        494
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        # ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
