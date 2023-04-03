# Standard Library
import doctest


class Solution:  # noqa: D101
    def rob(self, nums: list[int]) -> int:
        """Return max sum that can be robbed in a cul-de-sac of houses.

        Since 'alarms' go off if you rob two neighbors, have to alternate houses.
        Compare whether it is better to rob first house or last house.

        Args:
            nums (List[int]): Array containing the numerical value of robbing each house

        Returns:
            int: Maximum value that can be robbed from this set of houses.
        """
        size_n = len(nums)
        if size_n <= 1:
            return 0 if size_n == 0 else max(nums)

        def robbers(num_sub: list[int]) -> int:
            leader_t, follow_t = 0, 0
            for house in num_sub:
                follow_t, leader_t = leader_t, max(house + follow_t, leader_t)
            return leader_t

        # hit both possibilities and then choose the best route
        return max(robbers(nums[1:]), robbers(nums[:-1]))


def main():
    """House Robber II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.rob([2, 3, 2])
        3

    Example 1:
        >>> sol.rob([1, 2, 3, 1])
        4

    Example 1:
        >>> sol.rob([1, 2, 3])
        3
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
