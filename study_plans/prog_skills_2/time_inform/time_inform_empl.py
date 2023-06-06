"""Daily Challenge of June 3, 2023 on LeetCode.

Previously did problem for a study plan.
"""
# Standard Library
from collections import defaultdict
from collections import deque
import doctest


class Solution:  # noqa: D101
    def numOfMinutes(
        self,
        _: int,
        head_id: int,
        manager: list[int],
        tti: list[int],
    ) -> int:
        """Find maximum inform time to alert all employees of company to urgent news.

        Alerts can only be sent from managers to their subordinates.

        Args:
            _ (int): Number of employees, unused in my solution
            head_id (int): Root of employee tree
            manager (List[int]): List showing manager for employee i
            tti (List[int]): time to inform subordinate for manager i

        Returns:
            int: Time needed to inform all employees
        """

        def dfs(curr_node: int) -> int:
            return (
                max(dfs(sub) for sub in empl_dict[curr_node])
                if curr_node in empl_dict
                else 0
            ) + tti[curr_node]

        empl_dict = defaultdict(list)
        for i, val in enumerate(manager):
            empl_dict[val].append(i)
        empl_dict = dict(empl_dict)
        return dfs(head_id)

    def numOfMinutesBFS(
        self,
        _: int,
        head_id: int,
        manager: list[int],
        tti: list[int],
    ) -> int:
        """Return same as above using BFS approach."""
        empl_dict = defaultdict(list)
        for i, val in enumerate(manager):
            empl_dict[val].append(i)
        # employee_num, current_time
        que = deque()
        tti_max = 0
        que.append((head_id, 0))
        while que:
            curr_empl, curr_time = que.popleft()
            tti_max = max(tti_max, curr_time)
            new_time = curr_time + tti[curr_empl]
            for empl in empl_dict[curr_empl]:
                if manager[empl] == curr_empl:
                    que.append((empl, new_time))

        return tti_max


def main() -> None:
    """1376. Time to Inform Employees on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 1, 0, [-1], [0]
        >>> example_case_2 = 6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]
        >>> test_case_1 = 7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]

    Example 1:
        >>> sol.numOfMinutes(*example_case_1)
        0
        >>> sol.numOfMinutesBFS(*example_case_1)
        0

    Example 2:
        >>> sol.numOfMinutes(*example_case_2)
        1
        >>> sol.numOfMinutesBFS(*example_case_2)
        1

    Test 1:
        >>> sol.numOfMinutes(*test_case_1)
        21
        >>> sol.numOfMinutesBFS(*test_case_1)
        21
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
