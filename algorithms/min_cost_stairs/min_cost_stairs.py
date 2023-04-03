# Standard Library


class Solution:  # noqa: D101
    def minCostClimbingStairs(self, cost: list[int]) -> int:  # spec
        """Return minimum cost for getting from bottom floor to top floor.

        Array must be of integer cost. A climber can either go up
        1 step or up 2 steps at each point.

        Args:
            cost (List[int]): `cost[i]` for i represents the cost at that time.
                List will be modified

        Returns:
            int: Minimum cost to reach top of stairs
        """
        cost.append(0)
        # community suggests removing this, and change return statement to a min
        # it is slightly faster considering list is slow to append
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return cost[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10, 15, 20]))  # 15
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
