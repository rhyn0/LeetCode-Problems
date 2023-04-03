# Standard Library
import doctest


class Solution:  # noqa: D101
    def findPeakElement(self, nums: list[int]) -> int:  # spec
        """Return a peak index of array.

        A peak is an element that is greater than its direct neighbors.
        Ends of the array are always greater than elements outside the array.

        Args:
            nums (List[int]): array of numbers, with no neighboring repeats

        Returns:
            int: 0-based index for location of a peak
        """
        size_n = len(nums)
        if size_n == 1:
            return 0

        low, high = 0, size_n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low


def main():
    """Find Peak Element on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.findPeakElement([1, 2, 3, 1])
        2

    Example 2:
        >>> sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])
        5

    Test 1:
        >>> sol.findPeakElement([1, 2])
        1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
