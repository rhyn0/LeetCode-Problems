# Standard Library
from collections import defaultdict
from collections import deque
import doctest


class Solution:  # noqa: D101
    def numBusesToDestination(  # spec
        self,
        routes: list[list[int]],
        source: int,
        target: int,
    ) -> int:
        """Return minimum number of buses to get from source stop to target stop.

        Given a set of bus routes, where ``bus_i`` runs ``routes[i]`` infinitely,
        find least number of bus swaps to get to target.
        Each bus route is unique, and they are cyclical.

        Args:
            routes (List[List[int]]): List of bus routes
            source (int): Starting bus stop
            target (int): Target bus stop

        Returns:
            int: Number of bus swaps to get to target
        """
        stop_to_bus = defaultdict(list)
        for i, bus in enumerate(routes):
            for stop in bus:
                stop_to_bus[stop].append(i)

        que, visited_set = deque(), {source}
        que.append((source, 0))
        while que:
            curr_stop, num_bus = que.popleft()
            if curr_stop == target:
                return num_bus

            for route in stop_to_bus[curr_stop]:
                for stop in routes[route]:
                    if stop not in visited_set:
                        que.append((stop, num_bus + 1))
                        visited_set.add(stop)
                routes[route].clear()
        return -1


def main() -> None:
    """Bus Routes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6)
        2

    Example 2:
        >>> sol.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12)
        -1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
