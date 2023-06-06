# Standard Library
import doctest


class Solution:  # noqa: D101
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """Return length of smallest subarray that's sum that reaches target.

        Args:
            target (int): target sum for subarray to reach
            nums (List[int]): List of numbers to create subarray from

        Returns:
            int: Minimum length of summed subarray, 0 if no subarray exists.
        """
        small_len = float("inf")
        left = prefix_sum = 0
        for right, num_val in enumerate(nums):
            prefix_sum += num_val
            while prefix_sum >= target:
                small_len = min(small_len, right - left + 1)
                prefix_sum -= nums[left]
                left += 1
        return small_len if not isinstance(small_len, float) else 0


def main() -> None:
    """Minimum Size Subarray Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.minSubArrayLen(7, [2,3,1,2,4,3])
        2

    Example 2:
        >>> sol.minSubArrayLen(4, [1, 4, 4])
        1

    Example 3:
        >>> sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1])
        0

    Binary Search
    Example 1:
        >>> sol.minSubArrayLenBin(7, [2,3,1,2,4,3])
        2

    Example 2:
        >>> sol.minSubArrayLenBin(4, [1, 4, 4])
        1

    Example 3:
        >>> sol.minSubArrayLenBin(11, [1,1,1,1,1,1,1,1])
        0

    Test 1:
        >>> sol.minSubArrayLenBin(15, [1, 2, 3, 4, 5])
        5
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
