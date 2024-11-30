"""Essentials of Dynamic Programming General Multidimensional on LeetCode.

256. Paint House on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[17,2,17],[16,16,5],[14,3,19]]
    >>> example_case_2 = [[7,6,2]]

Example 1:
    >>> sol.minCost(example_case_1)
    10
    >>> sol.minCostSpace(example_case_1)
    10
    >>> sol.minCostRecursive(example_case_1)
    10
    >>> sol.minCostRowWriter(example_case_1)
    10

Example 2:
    >>> sol.minCost(example_case_2)
    2
    >>> sol.minCostSpace(example_case_2)
    2
    >>> sol.minCostRecursive(example_case_2)
    2
    >>> sol.minCostRowWriter(example_case_2)
    2
"""

# Standard Library
import copy


class Solution:  # noqa: D101
    def minCost(self, costs: list[list[int]]) -> int:
        """Return minimum cost to paint the given houses a color.

        Adjacent houses can not be painted the same color, 3 possbile colors.
        Cost of color 0 is index 0 in the given item representing the cost
        to paint the house that color

        Args:
            costs (list[list[int]]): unique costs to paint each house the given color

        Returns:
            int: Minimum cost to paint all houses
        """
        # store the cost of painting the last house red,green,blue
        dp = [0, 0, 0]
        if len(costs) == 1:
            return min(costs[0])

        for house in costs:
            # to pain this house a color, cost of this house plus min of other color
            # make sure to calculate this all at once, otherwise comparisons are wrong.
            dp = [
                house[0] + min(dp[1], dp[2]),
                house[1] + min(dp[0], dp[2]),
                house[2] + min(dp[0], dp[1]),
            ]

        # return minimum cost at end
        return min(dp)

    def minCostSpace(self, costs: list[list[int]]) -> int:
        """Return same as above but optimized for space."""
        last_red = last_blue = last_green = 0
        if len(costs) == 1:
            return min(costs[0])

        for house in costs:
            last_red, last_green, last_blue = (
                house[0] + min(last_green, last_blue),
                house[1] + min(last_red, last_blue),
                house[2] + min(last_red, last_green),
            )

        return min(last_red, last_green, last_blue)

    def minCostRowWriter(self, costs: list[list[int]]) -> int:
        """Return same as above but optimized for space."""
        n = len(costs)
        if n == 0:
            return 0
        previous_row = costs[0]
        for i in range(1, n):
            current_row = copy.deepcopy(costs[i])
            current_row[0] += min(previous_row[1], previous_row[2])
            current_row[1] += min(previous_row[0], previous_row[2])
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row
        return min(previous_row)

    def minCostRecursive(self, costs: list[list[int]]) -> int:
        """Return same as above but using recursion."""

        # if only 1 house, minimum of possible colors
        def helper(index: int, last_color_idx: int) -> int:
            if index < 0:
                return 0
            return min(
                costs[index][j] + helper(index - 1, j)
                for j in range(3)
                if j != last_color_idx
            )

        return min(helper(len(costs) - 1, i) for i in range(3))
