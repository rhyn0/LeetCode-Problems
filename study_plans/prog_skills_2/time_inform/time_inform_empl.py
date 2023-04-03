# Standard Library
from collections import defaultdict


class Solution:  # noqa: D101
    def numOfMinutes(
        self, _: int, head_id: int, manager: list[int], tti: list[int]
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfMinutes(1, 0, [-1], [0]))  # 0
    print(sol.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))  # 1
    print(sol.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))  # 21
