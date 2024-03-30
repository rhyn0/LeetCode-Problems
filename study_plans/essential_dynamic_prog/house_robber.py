"""Study Plan problem for Essentials of Dynamic Programming.

This problem was previously solved by me and placed elsewhere.
See LeetCode-Problems/study_plans/leet-75/house_robber/house_rob.py.
"""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def rob(self, nums: list[int]) -> int:
        """Return maximum value available without choosing adjacent numbers.

        A robber is trying to take valuables from a set of houses on a street.
        Adjacent houses have an alarm system tied together that immediately
        alerts police if two neighboring houses are robbed on same night.
        What is maximum value available to the robber tonight?

        Args:
            nums (list[int]): Value of each house on street, adjacency kept

        Returns:
            int: Maximum total value
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])
        for step, curr_house_val in enumerate(nums[2:], start=2):
            dp[step] = max(curr_house_val + dp[step - 2], dp[step - 1])

        return dp[n - 1]

    def rob_const_space(self, nums: list[int]) -> int:
        """Return same as above using constant space, modifies input."""
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[:2])
        for step, val in enumerate(nums[2:], start=2):
            nums[step] = max(nums[step - 2] + val, nums[step - 1])

        return nums[-1]

    def rob_variables(self, nums: list[int]) -> int:
        """Return same as above, using variable iteration."""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        first = nums[0]
        second = max(nums[:2])
        for val in nums[2:]:
            second, first = max(val + first, second), second
        return second


def main() -> None:
    """198. House Robber on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,2,3,1]
        >>> example_case_2 = [2,7,9,3,1]

    Example 1:
        >>> sol.rob(example_case_1)
        4
        >>> sol.rob_variables(example_case_1)
        4
        >>> sol.rob_const_space(example_case_1)
        4

    Example 2:
        >>> sol.rob(example_case_2)
        12
        >>> sol.rob_variables(example_case_2)
        12
        >>> sol.rob_const_space(example_case_2)
        12
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
