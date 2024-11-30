"""Essentials of Dynamic Programming General Multidimensional on LeetCode.

Previously solved, find that solution
at `challenges/april_2023/daily/coins_from_piles.py`.

2218. Maximum Value of K Coins From Piles on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[1,100,3],[7,8,9]], 2
    >>> example_case_2 = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7

Example 1:
    >>> sol.maxValueOfCoins(*example_case_1)
    101

Example 2:
    >>> sol.maxValueOfCoins(*example_case_2)
    706
"""


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
        # initialize our 2D result table
        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
        # our result table is padded by one preceding row and one preceding column
        # so this ith pile is 1-indexed
        for i in range(1, len(piles) + 1):
            for total_coins_to_pick in range(1, k + 1):
                # while iterating keep a sum of the coins of current pile
                # since as we increase the number of new pile coins
                # that sum is based on the value of previous coins seen
                curr_pile_prefix_coins = 0
                # undo the one indexing of piles
                for num_new_coins in range(
                    min(len(piles[i - 1]), total_coins_to_pick) + 1,
                ):
                    # if number of new coins is 0, we don't use any new coins
                    # can't add to the prefix sum as we haven't seen it
                    if num_new_coins > 0:
                        curr_pile_prefix_coins += piles[i - 1][num_new_coins - 1]
                    dp[i][total_coins_to_pick] = max(
                        # stay the same
                        dp[i][total_coins_to_pick],
                        dp[i - 1][total_coins_to_pick - num_new_coins]
                        + curr_pile_prefix_coins,
                    )
        return dp[-1][-1]
