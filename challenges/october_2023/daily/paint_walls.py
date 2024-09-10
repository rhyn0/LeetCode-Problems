"""Daily Challenge on LeetCode for October 14: Problem #2742 [Hard]."""

# Standard Library
import doctest
import functools


class Solution:  # noqa: D101
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        """Return the minimum cost for a pair of painters to paint the given walls.

        Each wall has a cost and time for the first painter to paint it. The second
        painter is able to paint all walls in 1 unit of time at no cost but only
        when the first painter is occupied.

        Args:
            cost (list[int]): Cost of painting the ith wall.
            time (list[int]): Amount of time needed for paid painter to paint ith wall.

        Returns:
            int: Minimum cost to paint all the walls.
        """
        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[n] = [0] + [float("inf") for _ in range(n)]  # type: ignore[misc]
        for i in range(n - 1, -1, -1):
            # frame this as a 0-1 knapsack problem
            for j in range(1, n + 1):
                # cost of paid painting this wall
                # plus the cost of painting the rest of the walls
                # using the set of walls not including this one
                paint = cost[i] + dp[i + 1][max(0, j - 1 - time[i])]
                # do nothing to this wall
                dont_paint = dp[i + 1][j]
                dp[i][j] = min(paint, dont_paint)

        # return the cost of painting all the walls
        # using the set of all walls
        return dp[0][n]

    def paintWallsRecursive(self, cost: list[int], time: list[int]) -> int:
        """Do same as above but using recursion."""
        n = len(cost)

        @functools.cache
        def recursive(ith_wall: int, remaining_walls_todo: int) -> int | float:
            if remaining_walls_todo <= 0:
                # all done
                return 0
            if ith_wall == n:
                # no more walls to assign paid painter to
                return float("inf")
            # cost of paid painting this wall
            # plus the cost of painting the rest of the walls
            paint = cost[ith_wall] + recursive(
                ith_wall + 1,
                max(0, remaining_walls_todo - 1 - time[ith_wall]),
            )
            # do nothing
            dont_paint = recursive(ith_wall + 1, remaining_walls_todo)
            return min(paint, dont_paint)

        # consider all walls, with all walls left to do
        # constraint that all tasks are possible so the return
        # inf is never reached at top level
        return recursive(0, n)  # type: ignore[return-value]


def main() -> None:
    """2742. Painting the Walls on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([1,2,3,2], [1,2,3,2])
        >>> example_case_2 = ([2,3,4,2], [1,1,1,1])

    Example 1:
        >>> sol.paintWalls(*example_case_1)
        3
        >>> sol.paintWallsRecursive(*example_case_1)
        3

    Example 2:
        >>> sol.paintWalls(*example_case_2)
        4
        >>> sol.paintWallsRecursive(*example_case_2)
        4
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
