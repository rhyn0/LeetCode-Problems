# Standard Library
import doctest
import math


class Solution:  # noqa: D101
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """Return the minimized maximum value of the array after operations.

        Only valid operation is moving a '1' from an index to the previous index.
        Specifically:
            - Choose an integer `i` such that `1 <= i < n`and`nums[i] > 0`.
            - Decrease `nums[i]` by 1.
            - Increase `nums[i - 1]` by 1.
        Operations can be done an infinite number of times.

        Args:
            nums (list[int]): Input array to find the minimized maximum of

        Returns:
            int: The minimum maximum in the array after operations
        """
        operation_start = 1
        prefix = min_max = nums[operation_start - 1]
        for i, val in enumerate(nums[operation_start:], start=operation_start + 1):
            prefix += val
            min_max = max(min_max, math.ceil(prefix / i))

        return min_max

    def minimizeArrayValueBin(self, nums: list[int]) -> int:
        """Return result as above using binary search."""

        def valid_minima(target: int) -> bool:
            # can't decrease first num ever
            prev = nums[0]
            if target < prev:
                return False
            for val in nums[1:]:
                # operations needed to get prev value to target
                # remove that number from current val, emulating current val
                prev = val - (target - prev)
                if prev > target:
                    return False

            return True

        # boiler binary search
        left, right = 0, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if valid_minima(mid):
                right = mid
            else:
                left = mid + 1
        return right


def main() -> None:
    """Minimize Maximum of Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [3, 7, 1, 6]
        >>> example_case_2 = [10, 1]
        >>> test_case_1 = [6, 9, 3, 8, 14]
        >>> test_case_2 = [13,13,20,0,8,9,9]

    Example 1:
        >>> sol.minimizeArrayValue(example_case_1)
        5
        >>> sol.minimizeArrayValueBin(example_case_1)
        5

    Example 2:
        >>> sol.minimizeArrayValue(example_case_2)
        10
        >>> sol.minimizeArrayValueBin(example_case_2)
        10

    Test 1:
        >>> sol.minimizeArrayValue(test_case_1)
        8
        >>> sol.minimizeArrayValueBin(test_case_1)
        8

    Test 2:
        >>> sol.minimizeArrayValue(test_case_2)
        16
        >>> sol.minimizeArrayValueBin(test_case_2)
        16
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
