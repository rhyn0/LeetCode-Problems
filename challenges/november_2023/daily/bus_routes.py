"""Daily Challenge for November 12 on LeetCode: Problem #815 [Hard].

This problem has been solved before in this repository.
Check out that prior solve at: ../../../study_plans/leet_75/bus_routes.py
"""
# Standard Library
from collections import defaultdict
from collections import deque
import doctest


class Solution:  # noqa: D101
    def numBusesToDestination(
        self,
        routes: list[list[int]],
        source: int,
        target: int,
    ) -> int:
        """Return the minimum number of buses necessary to get from source to target.

        Each bus runs their route cyclically, and each bus route is unique.
        The route for bus i is routes[i].

        Base case:
            If source == target, return 0
            If unable to reach target, return -1

        Args:
            routes (list[list[int]]): each bus route
            source (int): Starting bus stop
            target (int): Ending bus stop

        Returns:
            int: Number of buses to reach target
        """
        bus_stop_to_bus = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                bus_stop_to_bus[stop].add(bus)

        que = deque([(source, 0)])
        visited_buses = set()
        while que:
            curr_stop, num_bus = que.popleft()
            if curr_stop == target:
                # can early terminate since this is fastest path
                return num_bus
            for bus in bus_stop_to_bus[curr_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                que.extend((stop, num_bus + 1) for stop in routes[bus])
        return -1


def main() -> None:
    """815. Bus Routes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1,2,7],[3,6,7]], 1, 6
        >>> example_case_2 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12

    Example 1:
        >>> sol.numBusesToDestination(*example_case_1)
        2

    Example 2:
        >>> sol.numBusesToDestination(*example_case_2)
        -1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
