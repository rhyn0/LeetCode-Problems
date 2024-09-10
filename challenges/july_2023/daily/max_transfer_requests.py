"""Daily Challenge for July 2, 2023 on LeetCode."""

# Standard Library
from collections import defaultdict
import doctest
from operator import itemgetter


class Solution:  # noqa: D101
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        """Return maximum number of acceptable building transfers.

        A building transfer of form (i, j) moves a person from
        building i to building j. All `n` buildings are full and for
        the transfers to work, the buildings must also end full.

        Args:
            n (int): Number of buildings available
            requests (list[list[int]]): Each request to be processed

        Returns:
            int: Maximum number of acceptable transfers
        """
        curr_transfers = [0] * n
        best_transfers = 0
        request_len = len(requests)
        requests.sort(key=itemgetter(0))

        def backtrack(request_idx: int, accepted_transfers: int) -> None:
            nonlocal best_transfers
            # if the state is neutral, this is a solution
            if all(val == 0 for val in curr_transfers):
                best_transfers = max(best_transfers, accepted_transfers)
            # if greatest net change on any one building
            # exceeds the remaining number of requests to process, not valid
            if (
                max(curr_transfers, key=abs) > request_len - request_idx
                or request_idx >= request_len
            ):
                return

            # choice is to accept or not
            # ignore
            backtrack(request_idx + 1, accepted_transfers)
            curr_from, curr_to = requests[request_idx]
            curr_transfers[curr_from] -= 1
            curr_transfers[curr_to] += 1
            # accept
            backtrack(request_idx + 1, accepted_transfers + 1)
            curr_transfers[curr_from] += 1
            curr_transfers[curr_to] -= 1

        backtrack(0, 0)
        return best_transfers

    def maximumRequestsAllOn(self, _: int, requests: list[list[int]]) -> int:
        """Return same as above with different backtrack state."""
        curr_transfers = defaultdict(int)
        request_len = len(requests)
        for from_build, to_build in requests:
            curr_transfers[from_build] -= 1
            curr_transfers[to_build] += 1

        best_transfers = 0

        def backtrack(request_idx: int, accepted_transfers: int) -> None:
            nonlocal best_transfers
            if all(val == 0 for val in curr_transfers.values()):
                best_transfers = max(best_transfers, accepted_transfers)
                return
            if request_idx >= request_len:
                return

            # do accept option first, which in this case is do nothing
            backtrack(request_idx + 1, accepted_transfers)

            from_build, to_build = requests[request_idx]
            curr_transfers[from_build] += 1
            curr_transfers[to_build] -= 1
            # ignore option
            backtrack(request_idx + 1, accepted_transfers - 1)
            # reset
            curr_transfers[from_build] -= 1
            curr_transfers[to_build] += 1

        backtrack(0, request_len)
        return best_transfers


def main() -> None:
    """1601. Maximum Number of Achievable Transfer Requests on LeetCode.

    ====================================================

    Setup:
        >>> from copy import deepcopy
        >>> sol = Solution()
        >>> example_case_1 = 5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
        >>> example_case_2 = 3, [[0,0],[1,2],[2,1]]
        >>> example_case_3 = 4, [[0,3],[3,1],[1,2],[2,0]]
        >>> test_case_1 = 4, [[0,3],[3,3],[3,1],[0,1],[3,2],[2,2],[2,0],\
            [1,0],[1,0],[1,2],[2,0],[1,3],[3,0]]

    Example 1:
        >>> sol.maximumRequests(*deepcopy(example_case_1))
        5
        >>> sol.maximumRequestsAllOn(*example_case_1)
        5

    Example 2:
        >>> sol.maximumRequests(*deepcopy(example_case_2))
        3
        >>> sol.maximumRequestsAllOn(*example_case_2)
        3

    Example 3:
        >>> sol.maximumRequests(*deepcopy(example_case_3))
        4
        >>> sol.maximumRequestsAllOn(*example_case_3)
        4

    Test 1:
        >>> sol.maximumRequests(*deepcopy(test_case_1))
        10
        >>> sol.maximumRequestsAllOn(*test_case_1)
        10
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
