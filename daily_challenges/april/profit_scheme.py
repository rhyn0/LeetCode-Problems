"""Daily Challenge for April 20, 2023."""

# Standard Library
import doctest
from typing import Final


class Solution:  # noqa: D101
    CONSTR_MAX: Final = 105
    MODULO: Final = 10**9 + 7

    def profitableSchemes(
        self,
        n: int,
        min_profit: int,
        group: list[int],
        profit: list[int],
    ) -> int:
        """Return the number of profitable schemes that will produce at least minProfit.

        Each worker from `n` can only be used once per scenario, each job
        will use group[i] workers and give profit[i].

        Args:
            n (int): Total number of workers available
            min_profit (int): profit to meet or exceed to be a good scenario
            group (list[int]): workers needed per job
            profit (list[int]): amount of profit per job

        Returns:
            int: Number of profitable job combinations
        """
        dp = [
            [[0 for _ in range(self.CONSTR_MAX)] for _ in range(self.CONSTR_MAX)]
            for _ in range(self.CONSTR_MAX)
        ]
        num_jobs = len(group)
        # profitable schemes instantiate from all jobs, any workers, at least min profit
        for worker in range(n + 1):
            dp[num_jobs][worker][min_profit] = 1
        for left_most_job in range(num_jobs - 1, -1, -1):
            for in_use_workers in range(n + 1):
                for profit_point in range(min_profit + 1):
                    # start at point from considering previous jobs
                    take = dp[left_most_job + 1][in_use_workers][profit_point]
                    if in_use_workers + group[left_most_job] <= n:
                        take += dp[left_most_job + 1][
                            in_use_workers + group[left_most_job]
                        ][min(profit_point + profit[left_most_job], min_profit)]

                    dp[left_most_job][in_use_workers][profit_point] = take % self.MODULO

        return dp[0][0][0]


def main():
    """879. Profitable Schemes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = (5, 3, [2,2], [2,3])
        >>> example_case_2 = (10, 5, [2,3,5], [6,7,8])

    Example 1:
        >>> sol.profitableSchemes(*example_case_1)
        2

    Example 2:
        >>> sol.profitableSchemes(*example_case_2)
        7
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
