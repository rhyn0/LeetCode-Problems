"""Study Problem from Essential Dynamic Programming Plan."""
# Standard Library
import doctest
from functools import cache
from operator import itemgetter


class Solution:  # noqa: D101
    def deleteAndEarn(self, nums: list[int]) -> int:
        """Return maximum points available after doing infinite operations.

        An operation involves deleting a value from a list,
        afterwards all values that are 1 greater or 1 less are removed from array.

        Args:
            nums (list[int]): Array of values

        Returns:
            int: Maximum points available
        """
        uniq_vals = {num: nums.count(num) * num for num in nums}

        if len(uniq_vals) == 0:
            return 0

        max_value = max(uniq_vals.keys())
        if len(uniq_vals) == 1:
            return uniq_vals[max_value]

        @cache
        def recurse_vals(curr_key: int) -> int:
            if curr_key > max_value:
                return 0
            total = uniq_vals.get(curr_key, 0)

            return max(
                recurse_vals(curr_key + 1),
                total + recurse_vals(curr_key + 2),
            )

        return recurse_vals(min(uniq_vals.keys()))

    def deleteAndEarnBottom(self, nums: list[int]) -> int:
        """Return same as above using bottom up approach."""
        uniq_vals = {num: nums.count(num) * num for num in nums}

        if len(uniq_vals) == 0:
            return 0

        max_value = max(uniq_vals.keys())
        if len(uniq_vals) == 1:
            return uniq_vals[max_value]

        dp = [0] * (max_value + 1)
        for step in range(max_value + 1):
            dp[step] = max(dp[step - 2] + uniq_vals.get(step, 0), dp[step - 1])

        return dp[max_value]

    def deleteAndEarnElements(self, nums: list[int]) -> int:
        """Return same as above using shorter runtime than O(max(nums))."""
        uniq_vals = {num: nums.count(num) * num for num in nums}

        if len(uniq_vals) == 0:
            return 0

        ordered_num_points = sorted(uniq_vals.items(), key=itemgetter(0))
        first, second = 0, ordered_num_points[0][1]
        # intentionally lag idx behind for easier lookup in list
        for idx, (curr_key, total_points) in enumerate(ordered_num_points[1:], start=0):
            if curr_key == ordered_num_points[idx][0] + 1:
                first, second = second, max(second, total_points + first)
            else:
                first, second = second, total_points + second

        return second


def main():
    """740. Delete and Earn on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [3,4,2]
        >>> example_case_2 = [2,2,3,3,3,4]
        >>> test_case_1 = [3, 3, 3]
        >>> test_case_2 = [3, 4, 3]
        >>> test_case_3 = [3, 1]

    Example 1:
        >>> sol.deleteAndEarn(example_case_1)
        6
        >>> sol.deleteAndEarnBottom(example_case_1)
        6
        >>> sol.deleteAndEarnElements(example_case_1)
        6

    Example 2:
        >>> sol.deleteAndEarn(example_case_2)
        9
        >>> sol.deleteAndEarnBottom(example_case_2)
        9
        >>> sol.deleteAndEarnElements(example_case_2)
        9

    Test 1:
        >>> sol.deleteAndEarn(test_case_1)
        9
        >>> sol.deleteAndEarnBottom(test_case_1)
        9
        >>> sol.deleteAndEarnElements(test_case_1)
        9

    Test 2:
        >>> sol.deleteAndEarn(test_case_2)
        6
        >>> sol.deleteAndEarnBottom(test_case_2)
        6
        >>> sol.deleteAndEarnElements(test_case_2)
        6

    Test 3:
        >>> sol.deleteAndEarn(test_case_3)
        4
        >>> sol.deleteAndEarnBottom(test_case_3)
        4
        >>> sol.deleteAndEarnElements(test_case_3)
        4
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
