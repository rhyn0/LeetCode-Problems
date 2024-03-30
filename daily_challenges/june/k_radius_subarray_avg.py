"""Daily Challenge for June 20, 2023 on LeetCode."""

# Standard Library
import doctest
from itertools import accumulate


class Solution:  # noqa: D101
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        """Return average of the radius `k` subarray for each index.

        For i, 0 <= i < len(nums), return array of radius k subarray averages
        Where the return avgs[i] = sum(nums[i - k: i + k + 1]) // (2 * k + 1)
        If the subarray at index i is not of length (2 * k + 1) then instead
        the value is -1.

        Args:
            nums (list[int]): Array of numbers to find averages of subarrays in
            k (int): Radius of subarray

        Returns:
            list[int]: Averages of the subarrays.
        """
        n = len(nums)
        if 2 * k + 1 > n:
            return [-1] * n
        if k == 0:
            return nums
        prefixes = list(accumulate(nums))
        total_len = 2 * k + 1
        averages = [-1] * k
        for middle_idx in range(k, n - k):
            greater_prefix_sum = prefixes[middle_idx + k]
            remove_prefix = prefixes[middle_idx - k - 1] if middle_idx > k else 0
            averages.append((greater_prefix_sum - remove_prefix) // total_len)
        averages.extend([-1] * k)
        return averages

    def getAveragesWindow(self, nums: list[int], k: int) -> list[int]:
        """Return same as above using sliding window approach."""
        n = len(nums)
        window_len = 2 * k + 1
        if k == 0:
            return nums
        averages = [-1] * n
        if window_len > n:
            return averages
        window_sum = sum(nums[: 2 * k + 1])
        averages[k] = window_sum // window_len
        # i will be the leading edge of window, added value
        for i in range(window_len, n):
            # i - k is the center of subarray, which is index we update in averages
            window_sum += nums[i] - nums[i - window_len]
            averages[i - k] = window_sum // window_len
        return averages


def main() -> None:
    """2090. K Radius Subarray Averages on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [7,4,3,9,1,8,5,2,6], 3
        >>> example_case_2 = [100000], 0
        >>> self_test_1 = [100000], 1

    Example 1:
        >>> sol.getAverages(*example_case_1)
        [-1, -1, -1, 5, 4, 4, -1, -1, -1]
        >>> sol.getAveragesWindow(*example_case_1)
        [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    Example 2:
        >>> sol.getAverages(*example_case_2)
        [100000]
        >>> sol.getAveragesWindow(*example_case_2)
        [100000]

    Self Test 1:
        >>> sol.getAverages(*self_test_1)
        [-1]
        >>> sol.getAveragesWindow(*self_test_1)
        [-1]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
