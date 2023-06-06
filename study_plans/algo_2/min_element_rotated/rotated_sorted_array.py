# Standard Library
import doctest


class Solution:  # noqa: D101
    def findMin(self, nums: list[int]) -> int:
        """Return minimum element in a rotated sorted array.

        Array must contain only unique values.
        Array can be rotated (right) any number of times.

        Args:
            nums (List[int]): Sorted array that may be rotated

        Returns:
            int: value of minimum element
        """
        size_n = len(nums)
        if size_n == 1 or nums[0] < nums[-1]:
            return nums[0]
        low, high = 0, size_n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if mid != size_n - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[0] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def main() -> None:
    """Find Minimum in Rotated Sorted Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.findMin([3, 4, 5, 1, 2])
        1

    Example 2:
        >>> sol.findMin([4,5,6,7,0,1,2])
        0

    Example 3:
        >>> sol.findMin([11,13,15,17])
        11

    Test 1:
        >>> sol.findMin([1])
        1

    Test 2:
        >>> sol.findMin([2, 1])
        1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
