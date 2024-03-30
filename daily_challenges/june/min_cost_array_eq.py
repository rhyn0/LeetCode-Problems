"""Daily Challenge for June 21, 2023 on LeetCode."""

# Standard Library
import doctest
from itertools import accumulate
from operator import itemgetter


class Solution:  # noqa: D101
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        """Return minimum cost to turn array into all the same element.

        Operation is to increase/decrease any index in `nums` by 1. The cost of
        the operation on index `i` is `cost[i]`.

        Args:
            nums (list[int]): array of nums to make equal
            cost (list[int]): associated cost for doing operation on each index

        Returns:
            int: Minimum cost to make array equal
        """
        if len(set(nums)) == 1:
            return 0

        # sort by num, that way delta_x is always positive
        sort_nums, sort_cost = list(
            zip(*sorted(zip(nums, cost, strict=True), key=itemgetter(0)), strict=True),
        )
        prefix_costs = list(accumulate(sort_cost))
        total_cost = sum(
            abs(sort_nums[0] - x) * sort_cost[i] for i, x in enumerate(sort_nums)
        )
        min_cost = total_cost
        for i, num in enumerate(sort_nums[1:], start=0):
            # i lags behind to get delta x easier
            delta_num = num - sort_nums[i]
            total_cost += delta_num * (2 * prefix_costs[i] - prefix_costs[-1])
            min_cost = min(min_cost, total_cost)

        return min_cost

    def minCostBinSearch(self, nums: list[int], cost: list[int]) -> int:
        """Return same as above using binary search."""
        if len(set(nums)) == 1:
            return 0

        def total_cost(base: int) -> int:
            return sum(abs(base - x) * c for x, c in zip(nums, cost, strict=True))

        left, right = min(nums), max(nums)
        answer = 0
        while left < right:
            mid = (left + right) // 2
            cost_1, cost_2 = total_cost(mid), total_cost(mid + 1)
            answer = min(cost_1, cost_2)
            if cost_1 < cost_2:
                right = mid
            else:
                left = mid + 1

        return answer


def main() -> None:
    """2448. Minimum Cost to Make Array Equal on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,3,5,2], [2,3,1,14]
        >>> example_case_2 = [2,2,2,2,2], [4,2,8,1,3]
        >>> self_test_1 = [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]
        >>> self_test_2 = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]

    Example 1:
        >>> sol.minCost(*example_case_1)
        8
        >>> sol.minCostBinSearch(*example_case_1)
        8

    Example 2:
        >>> sol.minCost(*example_case_2)
        0
        >>> sol.minCostBinSearch(*example_case_2)
        0

    Self Test 1:
        >>> sol.minCost(*self_test_1)
        15
        >>> sol.minCostBinSearch(*self_test_1)
        15

    Self Test 2:
        >>> sol.minCost(*self_test_2)
        15
        >>> sol.minCostBinSearch(*self_test_2)
        15
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
