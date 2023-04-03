# Standard Library
import doctest


class Solution:  # noqa: D101
    def coinChange(self, coins: list[int], amount: int) -> int:  # spec
        """Return least number of coins needed to create ``amount``.

        If the amount is unable to be made using given coins, return -1.

        Args:
            coins (List[int]): Set of coin values available to use
            amount (int): Total amount to make

        Returns:
            int: Number of coins used to make or -1 if impossible to make
        """
        num_coins = [0] * amount
        if amount == 0:
            return 0
        for coin in coins:
            if coin > amount:
                continue
            num_coins[coin - 1] = 1
        for i, val in enumerate(num_coins):
            if val != 0:
                continue
            if possible_coins := [
                num_coins[i - coin] + 1
                for coin in coins
                if i >= coin and num_coins[i - coin] > 0
            ]:
                num_coins[i] = min(possible_coins)

        return num_coins[-1] if num_coins[-1] != 0 else -1


def main():
    """Coin Change on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.coinChange([1, 2, 5], 11)
        3

    Example 2:
        >>> sol.coinChange([2], 3)
        -1

    Example 3:
        >>> sol.coinChange([1], 0)
        0

    Test 1:
        >>> sol.coinChange([474,83,404,3], 264)
        8
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
