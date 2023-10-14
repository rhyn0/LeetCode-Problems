"""Daily Challenge for June 26, 2023 on LeetCode."""
# Standard Library
import doctest
import heapq


class Solution:  # noqa: D101
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        """Return minimum cost to hire `k` workers.

        Hiring is broken into rounds - in each round up to 2 * candidates
        can be considered. Only the lowest core employee can be hired.
        If there is a tie in hiring cost, then lower index employee will be hired.
        In each round, only the first and last `candidates` of
        the array are considered.

        Args:
            costs (list[int]): Array of costs to hire the i-th employee
            k (int): Number of employees to hire
            candidates (int): Number of candidates from tails of array to consider

        Returns:
            int: Minimum cost to hire k workers
        """
        hiring_cost = 0
        n = len(costs)
        curr_candidates = [
            (item, idx)
            for idx, item in enumerate(costs)
            if idx < candidates or idx >= n - candidates
        ]
        heapq.heapify(curr_candidates)
        left_idx, right_idx = candidates, n - candidates - 1

        for _ in range(k):
            # tuples compare by item, so ties will be broken by idx if value is equal
            hired = heapq.heappop(curr_candidates)
            hiring_cost += hired[0]
            if left_idx <= right_idx:
                if hired[1] < left_idx:
                    heapq.heappush(curr_candidates, (costs[left_idx], left_idx))
                    left_idx += 1
                else:
                    heapq.heappush(curr_candidates, (costs[right_idx], right_idx))
                    right_idx -= 1

        return hiring_cost


def main() -> None:
    """2462. Total Cost to Hire K Workers on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [17,12,10,2,7,2,11,20,8], 3, 4
        >>> example_case_2 = [1,2,4,1], 3, 3
        >>> self_test_1 = [4,2,1,4], 3, 1

    Example 1:
        >>> sol.totalCost(*example_case_1)
        11

    Example 2:
        >>> sol.totalCost(*example_case_2)
        4

    Self Test 1:
        >>> sol.totalCost(*self_test_1)
        7
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
