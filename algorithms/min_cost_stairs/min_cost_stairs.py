# Standard Library
import doctest


class Solution:  # noqa: D101
    def minCostClimbingStairs(self, cost: list[int]) -> int:  # spec
        """Return minimum cost for getting from bottom floor to top floor.

        Array must be of integer cost. A climber can either go up
        1 step or up 2 steps at each point.

        Args:
            cost (List[int]): `cost[i]` for i represents the cost at that time.
                List will be modified

        Returns:
            int: Minimum cost to reach top of stairs
        """
        cost.append(0)
        # community suggests removing this, and change return statement to a min
        # it is slightly faster considering list is slow to append
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return cost[-1]


def main() -> None:
    """746. Min Cost Climbing Stairs on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [10, 15, 20]
        >>> example_case_2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    Example 1:
        >>> sol.minCostClimbingStairs(example_case_1)
        15

    Example 2:
        >>> sol.minCostClimbingStairs(example_case_2)
        6
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
