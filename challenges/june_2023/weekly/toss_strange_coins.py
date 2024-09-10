"""First Weekly Challenge of June on LeetCode."""

# Standard Library
from decimal import localcontext
import doctest
from functools import cache


class Solution:  # noqa: D101
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        """Return probability of getting `target` heads from odd coins.

        These coins are odd in that they have unique probabilities
        of landing on heads - given by `prob`.

        Args:
            prob (list[float]): List of coins unique probabilities
            target (int): Number of heads to get

        Returns:
            float: Probability of getting this number of heads from the coins
        """
        # num coin rows, target columns
        n = len(prob)
        dp = [[0.0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1.0

        for row in range(1, n + 1):
            # target = 0, means only tails
            dp[row][0] = dp[row - 1][0] * (1 - prob[row - 1])
            for col in range(1, min(row, target) + 1):
                dp[row][col] = dp[row - 1][col - 1] * prob[row - 1] + dp[row - 1][
                    col
                ] * (1 - prob[row - 1])

        return dp[n][target]

    def probabilityOfHeads1D(self, prob: list[float], target: int) -> float:
        """Return same as above using a 1D array."""
        n = len(prob)
        prev_dp = [0.0] * (target + 1)
        prev_dp[0] = 1.0
        for row in range(1, n + 1):
            dp = [(prev_dp[0] * (1 - prob[row - 1]))] + prev_dp[1:]
            for col in range(1, min(row, target) + 1):
                dp[col] = prev_dp[col - 1] * prob[row - 1] + prev_dp[col] * (
                    1 - prob[row - 1]
                )
            prev_dp = dp[:]

        return prev_dp[target]

    def probabilityOfHeadsRec(self, prob: list[float], target: int) -> float:
        """Return same as above using recursion/memoization."""
        n = len(prob)

        @cache
        def recurse_coin(curr_coin: int, remain_heads: int) -> float:
            if remain_heads < 0:
                return 0
            if curr_coin == n:
                return 1 if remain_heads == 0 else 0

            heads_prob = prob[curr_coin] * recurse_coin(curr_coin + 1, remain_heads - 1)
            tails_prob = (1 - prob[curr_coin]) * recurse_coin(
                curr_coin + 1,
                remain_heads,
            )
            return heads_prob + tails_prob

        return recurse_coin(0, target)


def float_compare(x: float, y: float) -> bool:
    """Compare the given floats given constraints of problem."""
    with localcontext() as ctx:
        # Problem says, correct if they are within 10^-5 of the correct answer
        ctx.prec = 5
        return (
            ctx.compare(
                ctx.create_decimal_from_float(x),
                ctx.create_decimal_from_float(y),
            )
            == 0
        )


def main() -> None:
    """1230. Toss Strange Coins on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [0.4], 1
        >>> example_case_2 = [0.5,0.5,0.5,0.5,0.5], 0
        >>> self_test_1 = [0.7, 0.1, 0.3], 3
        >>> self_test_2 = [0.7, 0.1, 0.3], 1
        >>> test_case_1 = [0.2,0.8,0,0.3,0.5], 3

    Example 1:
        >>> float_compare(sol.probabilityOfHeads(*example_case_1), 0.4)
        True
        >>> float_compare(sol.probabilityOfHeads1D(*example_case_1), 0.4)
        True
        >>> float_compare(sol.probabilityOfHeadsRec(*example_case_1), 0.4)
        True

    Example 2:
        >>> float_compare(sol.probabilityOfHeads(*example_case_2), 0.03125)
        True
        >>> float_compare(sol.probabilityOfHeads1D(*example_case_2), 0.03125)
        True
        >>> float_compare(sol.probabilityOfHeadsRec(*example_case_2), 0.03125)
        True

    Self Test 1:
        >>> float_compare(sol.probabilityOfHeads(*self_test_1), 0.021)
        True
        >>> float_compare(sol.probabilityOfHeads1D(*self_test_1), 0.021)
        True
        >>> float_compare(sol.probabilityOfHeadsRec(*self_test_1), 0.021)
        True

    Self Test 2:
        >>> float_compare(sol.probabilityOfHeads(*self_test_2), 0.54300)
        True
        >>> float_compare(sol.probabilityOfHeads1D(*self_test_2), 0.54300)
        True
        >>> float_compare(sol.probabilityOfHeadsRec(*self_test_2), 0.54300)
        True


    Test 1:
        >>> float_compare(sol.probabilityOfHeads(*test_case_1), 0.18200)
        True
        >>> float_compare(sol.probabilityOfHeads1D(*test_case_1), 0.18200)
        True
        >>> float_compare(sol.probabilityOfHeadsRec(*test_case_1), 0.18200)
        True
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
