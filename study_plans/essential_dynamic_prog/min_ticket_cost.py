"""Essentials of Dynamic Programming General 1D Problem on LeetCode.

983. Minimum Cost For Tickets on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [1,4,6,7,8,20], [2,7,15]
    >>> example_case_2 = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]

Example 1:
    >>> sol.mincostTickets(*example_case_1)
    11
    >>> sol.mincostTicketsTab(*example_case_1)
    11

Example 2:
    >>> sol.mincostTickets(*example_case_2)
    17
    >>> sol.mincostTicketsTab(*example_case_2)
    17
"""


class Solution:  # noqa: D101
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """Return the minimum cost of purchasing tickets for your travel days.

        Travel days are given in the days list - numbering each day of the year [1,365].
        Tickets are sold in 1,7,30 day passes
        costing costs[0], costs[1], and costs[2] respectively.

        Args:
            days (list[int]): Travel days
            costs (list[int]): Cost per type of ticket

        Returns:
            int: Minimum cost for tickets to travel all days.
        """
        travel_days = set(days)
        memo = {}

        def dfs(curr_day: int) -> int:
            if curr_day <= 0:
                return 0
            if curr_day not in travel_days:
                return dfs(curr_day - 1)
            if curr_day in memo:
                return memo[curr_day]
            rv = min(
                costs[0] + dfs(curr_day - 1),
                costs[1] + dfs(curr_day - 7),
                costs[2] + dfs(curr_day - 30),
            )
            memo[curr_day] = rv
            return rv

        return dfs(days[-1])

    def mincostTicketsTab(self, days: list[int], costs: list[int]) -> int:
        """Return same as above using tabulation."""
        max_day = days[-1]
        dp = [0] * (max_day + 1)
        latest_day_idx = 0
        for day in range(1, max_day + 1):
            if day < days[latest_day_idx]:
                dp[day] = dp[day - 1]
            else:
                latest_day_idx += 1
                dp[day] = min(
                    cost + dp[max(0, day - idx_off)]
                    for idx_off, cost in zip((1, 7, 30), costs, strict=True)
                )
        return dp[-1]
