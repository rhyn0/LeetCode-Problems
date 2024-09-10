"""Daily Challenge for July 6, 2023 on LeetCode."""

# Standard Library
import doctest
from itertools import accumulate


class Solution:  # noqa: D101
    MAX_INT = 10**9

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """Return minimum subarray length needed from nums to reach or exceed target.

        Args:
            target (int): Goal of the sum of the subarray
            nums (list[int]): Array to make subarrays from

        Returns:
            int: Minimum length of subarray needed, 0 if no answer
        """
        prefix_sums = [*list(accumulate(nums)), 0]  # for the -1 case
        n = len(nums)

        def check_subarray_len(length: int) -> bool:
            return any(
                prefix_sums[i] - prefix_sums[i - length] >= target
                for i in range(length - 1, n)
            )

        # zero size subarray is not ever valid
        left, right = 1, n
        best_len = 0
        while left <= right:
            mid = (left + right) // 2
            if check_subarray_len(mid):
                # if this size works, try smaller
                right = mid - 1
                best_len = mid
            else:
                left = mid + 1
        return best_len

    def minSubArrayLenConstSpace(self, target: int, nums: list[int]) -> int:
        """Return same as above using constant space."""
        small_len = self.MAX_INT
        left = prefix_sum = 0
        for right, num_val in enumerate(nums):
            prefix_sum += num_val
            while prefix_sum >= target:
                small_len = min(small_len, right - left + 1)
                prefix_sum -= nums[left]
                left += 1
        return small_len if small_len < self.MAX_INT else 0


def main() -> None:
    """209. Minimum Size Subarray Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 7, [2,3,1,2,4,3]
        >>> example_case_2 = 4, [1,4,4]
        >>> example_case_3 = 11, [1,1,1,1,1,1,1,1]

    Example 1:
        >>> sol.minSubArrayLen(*example_case_1)
        2
        >>> sol.minSubArrayLenConstSpace(*example_case_1)
        2

    Example 2:
        >>> sol.minSubArrayLen(*example_case_2)
        1
        >>> sol.minSubArrayLenConstSpace(*example_case_2)
        1

    Example 3:
        >>> sol.minSubArrayLen(*example_case_3)
        0
        >>> sol.minSubArrayLenConstSpace(*example_case_3)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
