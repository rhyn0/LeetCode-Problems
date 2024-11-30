"""Essentials of Dynamic Programming Gneeral Multidimensional on LeetCode.

265. Paint House II on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[1,5,3],[2,9,4]]
    >>> example_case_2 = [[1,3],[2,4]]

Example 1:
    >>> sol.minCostII(example_case_1)
    5
    >>> sol.minCostIIRecursive(example_case_1)
    5
    >>> sol.minCostIISpace(example_case_1)
    5

Example 2:
    >>> sol.minCostII(example_case_2)
    5
    >>> sol.minCostIIRecursive(example_case_2)
    5
    >>> sol.minCostIISpace(example_case_2)
    5
"""

# Standard Library
from functools import cache


class Solution:  # noqa: D101
    def minCostII(self, costs: list[list[int]]) -> int:
        """Return the minimum cost to paint all houses one of k colors.

        Adjacent houses can not be painted the same color.

        Args:
            costs (list[list[int]]): List of costs to paint house i the color j

        Returns:
            int: Minimum cost to paint all houses
        """
        n = len(costs)
        if n == 0:
            # while breaking leetcode constraints, generally helpful assumption
            return 0
        # make copy of last house options given
        running_costs = costs[n - 1][:]
        k = len(running_costs)
        for idx in range(n - 2, -1, -1):
            current_house = costs[idx]
            running_costs = [
                current_house[i]
                + min(
                    paint_cost
                    for paint_idx, paint_cost in enumerate(running_costs)
                    if paint_idx != i
                )
                for i in range(k)
            ]
        return min(running_costs)

    def minCostIIRecursive(self, costs: list[list[int]]) -> int:
        """Return same as above but using recursion."""
        n = len(costs)

        @cache
        def helper(house_idx: int, prev_chosen_color: int) -> int:
            if house_idx >= n:
                return 0
            curr_house = costs[house_idx]
            return min(
                curr_house_color_cost + helper(house_idx + 1, i)
                for i, curr_house_color_cost in enumerate(curr_house)
                if i != prev_chosen_color
            )

        if n == 0:
            return 0
        return min(helper(0, i) for i in range(len(costs[0])))

    def minCostIISpace(self, costs: list[list[int]]) -> int:
        """Return same as above using constant space.

        Also a helpful mixin to simplify time complexity.
        Time - O(nk)
        Space - O(1)
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        # use these as summing variables too
        prev_min_cost = prev_second_min_cost = prev_min_color = None
        # find the minimums of the first house
        for color_idx, color_cost in enumerate(costs[0]):
            if prev_min_cost is None or color_cost < prev_min_cost:
                prev_min_cost, prev_second_min_cost = color_cost, prev_min_cost
                prev_min_color = color_idx
            elif prev_second_min_cost is None or color_cost < prev_second_min_cost:
                prev_second_min_cost = color_cost

        # now iterate the remaining houses, adding into the prev_min* variables
        for house in range(1, n):
            min_cost = min_second_cost = min_color_idx = None
            for color in range(k):
                # determine cost to paint up to this house
                cost = costs[house][color]
                cost += (
                    prev_second_min_cost if color == prev_min_color else prev_min_cost
                )

                # for this house the min costs are
                if min_cost is None or cost < min_cost:
                    min_cost, min_second_cost = cost, min_cost
                    min_color_idx = color
                elif min_second_cost is None or cost < min_second_cost:
                    min_second_cost = cost

            # now update the runnings
            prev_min_cost, prev_second_min_cost, prev_min_color = (
                min_cost,
                min_second_cost,
                min_color_idx,
            )
        return prev_min_cost
