"""Daily Challenge for June 10, 2023 on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        """Return maximum value at `index` given other constraints.

        4 constraints of an acceptable array must be fulfilled:
         - Array length is equal to `n`
         - Sum of elements in array must not exceed `maxSum`
         - All elements in array must be greater than 0
         - Difference between adjacent elements can be at most 1

        Additionally, the value at `index` must be maximized

        Args:
            n (int): Size of array to fulfill
            index (int): Index to maximize the value of
            max_sum (int): Array sum to not exceed

        Returns:
            int: Maximal value that can work at `index`
        """

        def _test_array(val: int) -> int:
            # there are index values prior to val
            # there are n - index - 1 after val
            # index: 1, n: 6, val: 3
            # how many values prior to index are 1s: index - (val - 2)
            # how many values after index are 1s: (n - index - 1) - (val - 2)
            ramp_up_ones = max(index - max(val - 2, 0), 0)
            ramp_down_ones = max(n - index - 1 - max(val - 2, 0), 0)
            ramp_up_sum = int(
                ((index - ramp_up_ones) / 2)
                * (2 * max(val - index, 2) + index - ramp_up_ones - 1),
            )
            ramp_down_sum = int(
                ((n - index - 1 - ramp_down_ones) / 2)
                * (2 * max(val - (n - index - 1), 2) + n - index - ramp_down_ones - 2),
            )
            return ramp_up_ones + ramp_up_sum + val + ramp_down_sum + ramp_down_ones

        # 0 is not a valid value in the array
        left, right = 1, max_sum
        greatest_val = -1
        while left <= right:
            mid = (left + right) // 2
            array_sum = _test_array(mid)
            if array_sum <= max_sum:
                left = mid + 1
                greatest_val = max(mid, greatest_val)
            else:
                right = mid - 1
        return greatest_val


def main() -> None:
    """1802. Maximum Value at a Given Index in a Bounded Array on LeetCode.

    Constraints: n <= maxSum

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 4, 2, 6
        >>> example_case_2 = 6, 1, 10
        >>> self_test_1 = 4, 1, 4
        >>> self_test_2 = 3, 1, 12
        >>> self_test_3 = 3, 1, 16
        >>> test_case_1 = 8257285, 4828516, 850015631

    Example 1:
        >>> sol.maxValue(*example_case_1)
        2

    Example 2:
        >>> sol.maxValue(*example_case_2)
        3

    Self Test 1:
        >>> sol.maxValue(*self_test_1)
        1

    Self Test 2:
        >>> sol.maxValue(*self_test_2)
        4

    Self Test 3:
        >>> sol.maxValue(*self_test_3)
        6

    Test 1:
        >>> sol.maxValue(*test_case_1)
        29014
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
