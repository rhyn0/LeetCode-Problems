"""Essentials of Dynamic Programming General 1D Problem on LeetCode.

2140. Solving Questions with Brainpower on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[3,2],[4,3],[4,4],[2,5]]
    >>> example_case_2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]

Example 1:
    >>> sol.mostPoints(example_case_1)
    5
    >>> sol.mostPointsTab(example_case_1)
    5

Example 2:
    >>> sol.mostPoints(example_case_2)
    7
    >>> sol.mostPointsTab(example_case_2)
    7
"""

# Standard Library
from functools import cache


class Solution:  # noqa: D101
    def mostPoints(self, questions: list[list[int]]) -> int:
        """Given questions that yield points and cost brainpower, return max points.

        Questions must be approached sequentially.
        Solving a question uses brainpower_i which means must skip the next brainpower_i
        questions.

        Each question is posed as [points_i, brainpower_i].

        Args:
            questions (list[list[int]]): Array of questions

        Returns:
            int: Maximum amount of points earnable
        """
        n = len(questions)

        @cache
        def dfs(index: int) -> int:
            if index >= n:
                return 0

            this_points, this_power = questions[index]
            return max(
                # solve this question
                this_points + dfs(index + this_power + 1),
                # skip this question
                dfs(index + 1),
            )

        return dfs(0)

    def mostPointsTab(self, questions: list[list[int]]) -> int:
        """Return same as above using bottom-up approach."""
        n = len(questions)
        dp = [0] * n
        # base case, last question max is by solving it
        dp[-1] = questions[-1][0]
        for idx in range(n - 2, -1, -1):
            points, power = questions[idx]
            dp[idx] = max(
                # solve this question
                points + (dp[idx + power + 1] if idx + power + 1 < n else 0),
                # skip it
                dp[idx + 1],
            )

        return dp[0]
