"""Daily Challenge for June 25, 2023 on LeetCode."""

# Standard Library
from collections.abc import Iterator
import doctest
from functools import cache


class Solution:  # noqa: D101
    LEET_MOD = 10**9 + 7

    @staticmethod
    def _reachable_locations_fuel(
        locations: list[int],
        curr_loc: int,
        fuel: int,
    ) -> Iterator[tuple[int, int]]:
        for loc, city_fuel in enumerate(locations):
            fuel_cost = abs(locations[curr_loc] - city_fuel)
            if loc != curr_loc and fuel_cost <= fuel:
                yield loc, fuel - fuel_cost

    def countRoutes(
        self,
        locations: list[int],
        start: int,
        finish: int,
        init_fuel: int,
    ) -> int:
        """Return number of routes available from `start` to `finish`.

        Moving along a route consumes fuel, the consumption between cities
        'i' and 'j' is |locations[i] - locations[j]| or the absolute value.
        A valid 'j' is where 'j' != 'i'. Fuel cannot go negative.

        Return value is modulo 10**9 + 7 due to size.

        Args:
            locations (list[int]): Cities and their relative fuel level
            start (int): starting city
            finish (int): end city
            init_fuel (int): Fuel to start with

        Returns:
            int: Number of routes that exist traverse start -> finish
        """

        @cache
        def recurse_routes(end: int, curr_fuel: int) -> int:
            if curr_fuel < 0:
                return 0
            total_routes = 0
            if end == start:
                total_routes += 1
            for loc_idx, new_fuel in self._reachable_locations_fuel(
                locations,
                end,
                curr_fuel,
            ):
                total_routes += recurse_routes(loc_idx, new_fuel)
            return total_routes

        return recurse_routes(finish, init_fuel) % self.LEET_MOD

    def countRoutesIterative(
        self,
        locations: list[int],
        start: int,
        finish: int,
        init_fuel: int,
    ) -> int:
        """Return same as above using iterative methods."""
        n = len(locations)
        dp = [[0] * (init_fuel + 1) for _ in range(n)]

        # if we start at finish, we have one route at least no matter the fuel level
        for j in range(init_fuel + 1):
            dp[finish][j] = 1

        # for each city and fuel level, try reaching other cities
        # can't use 2D array due to jumping
        # from (i, j) -> (k, j - abs(locations[i] - locations[k])
        for j in range(init_fuel + 1):
            for i in range(n):
                for loc_idx, new_fuel in self._reachable_locations_fuel(
                    locations,
                    i,
                    j,
                ):
                    dp[i][j] = (dp[i][j] + dp[loc_idx][new_fuel]) % self.LEET_MOD

        return dp[start][init_fuel]


def main() -> None:
    """1575. Count All Possible Routes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [2,3,6,8,4], 1, 3, 5
        >>> example_case_2 = [4,3,1], 1, 0, 6
        >>> example_case_3 = [5,2,1], 0, 2, 3

    Example 1:
        >>> sol.countRoutes(*example_case_1)
        4
        >>> sol.countRoutesIterative(*example_case_1)
        4

    Example 2:
        >>> sol.countRoutes(*example_case_2)
        5
        >>> sol.countRoutesIterative(*example_case_2)
        5

    Example 3:
        >>> sol.countRoutes(*example_case_3)
        0
        >>> sol.countRoutesIterative(*example_case_3)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
