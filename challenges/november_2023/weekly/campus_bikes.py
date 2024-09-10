"""Weekly Challenge on LeetCode: Problem #1057 [Medium]."""

# Standard Library
from collections import defaultdict
import doctest
import heapq
from itertools import product
from typing import TypeAlias

Point2D: TypeAlias = list[int]


class Solution:  # noqa: D101
    @staticmethod
    def _manhattan_dist(p1: Point2D, p2: Point2D) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def assignBikes(self, workers: list[Point2D], bikes: list[Point2D]) -> list[int]:
        """Return list of worker-bike pairs that are sorted according to criteria.

        Criteria is:
            - Minimum distance pairs first
            - Ties of distance are broken by worker index in the given `workers`
            - Ties are finally broken by bike index in the given `bikes`

        Args:
            workers (list[Point2D]): List of points where the ith worker currently is
            bikes (list[Point2D]): List of points where the ith bike currently is

        Returns:
            list[int]: ith element is the bike index that the ith worker takes
        """
        # store the values for sorting in a tuple in that order
        # dist, worker idx, bike idx
        triplets = [
            (self._manhattan_dist(worker, bike), worker_idx, bike_idx)
            for (worker_idx, worker), (bike_idx, bike) in product(
                enumerate(workers),
                enumerate(bikes),
            )
        ]
        triplets.sort()

        num_workers = len(workers)
        bike_used = [False] * len(bikes)
        worker_bikes = [-1] * num_workers
        total_used = 0
        for _, worker_idx, bike_idx in triplets:
            if bike_used[bike_idx] or worker_bikes[worker_idx] != -1:
                continue

            bike_used[bike_idx] = True
            worker_bikes[worker_idx] = bike_idx
            total_used += 1

            if total_used == num_workers:
                break

        return worker_bikes

    def assignBikesBucketSort(
        self,
        workers: list[Point2D],
        bikes: list[Point2D],
    ) -> list[int]:
        """Return same as above using a bucket sort methodology."""
        pairs_of_dist = defaultdict(list)
        min_dist = float("inf")
        num_workers = len(workers)
        for (worker_idx, worker), (bike_idx, bike) in product(
            enumerate(workers),
            enumerate(bikes),
        ):
            distance = self._manhattan_dist(worker, bike)
            pairs_of_dist[distance].append((worker_idx, bike_idx))
            min_dist = min(min_dist, distance)

        curr_dist = min_dist
        bike_used = [False] * len(bikes)
        worker_bikes = [-1] * num_workers
        total_used = 0
        while total_used < num_workers:
            for worker_idx, bike_idx in pairs_of_dist[curr_dist]:
                if bike_used[bike_idx] or worker_bikes[worker_idx] != -1:
                    continue
                bike_used[bike_idx] = True
                worker_bikes[worker_idx] = bike_idx
                total_used += 1
            curr_dist += 1

        return worker_bikes

    def assignBikesHeap(
        self,
        workers: list[Point2D],
        bikes: list[Point2D],
    ) -> list[int]:
        """Return same as above using a Heap."""
        # keep one option for a worker in the Heap at any time
        # must store alternate options for each worker outside heap.
        worker_backup_options = []
        pq = []

        for worker_idx, worker in enumerate(workers):
            curr_worker_options = [
                (self._manhattan_dist(worker, bike), worker_idx, bike_idx)
                for bike_idx, bike in enumerate(bikes)
            ]
            # reverse order for optimized removal
            curr_worker_options.sort(reverse=True)
            heapq.heappush(pq, curr_worker_options.pop())
            # this keeps the options tied to the exact worker_idx
            worker_backup_options.append(curr_worker_options)

        bike_used = [False] * len(bikes)
        worker_bikes = [-1] * len(workers)
        # heap will keep one option per worker, while that worker has no bike assigned
        while pq:
            _, worker_idx, bike_idx = heapq.heappop(pq)
            if not bike_used[bike_idx]:
                # worker is free (in pq) and this bike is too
                # its minimum option for this worker based on options sorting
                bike_used[bike_idx] = True
                worker_bikes[worker_idx] = bike_idx
            else:
                # this pair can't be made choose the next bike option for this worker
                next_option = worker_backup_options[worker_idx].pop()
                heapq.heappush(pq, next_option)

        return worker_bikes


def main() -> None:
    """1057. Campus Bikes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[0,0],[2,1]], [[1,2],[3,3]]
        >>> example_case_2 = [[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]

    Example 1:
        >>> sol.assignBikes(*example_case_1)
        [1, 0]
        >>> sol.assignBikesBucketSort(*example_case_1)
        [1, 0]
        >>> sol.assignBikesHeap(*example_case_1)
        [1, 0]

    Example 2:
        >>> sol.assignBikes(*example_case_2)
        [0, 2, 1]
        >>> sol.assignBikesBucketSort(*example_case_2)
        [0, 2, 1]
        >>> sol.assignBikesHeap(*example_case_2)
        [0, 2, 1]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
