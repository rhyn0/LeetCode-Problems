# Standard Library
import doctest


class Solution:  # noqa: D101
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """Return first occurrence and last occurrence of target in array.

        If target not in sorted array, return [-1, -1].

        Args:
            nums (List[int]): non-decreasing array
            target (int): target to find in nums

        Returns:
            List[int]: list of first index occur and last index occur
        """

        def bin_search(low_point: int, high_point: int, first: bool) -> int:
            while low_point <= high_point:
                mid = (low_point + high_point) // 2
                if nums[mid] == target:
                    if first:
                        if mid == low_point or nums[mid - 1] < target:
                            return mid
                        high_point = mid - 1
                    else:
                        if mid == high_point or nums[mid + 1] > target:
                            return mid
                        low_point = mid + 1
                elif nums[mid] > target:
                    high_point = mid - 1
                else:
                    low_point = mid + 1
            return -1

        size_n = len(nums)
        if size_n == 0:
            return [-1, -1]
        first_occur = bin_search(0, size_n - 1, True)
        if first_occur == -1:
            return [-1, -1]
        last_occur = bin_search(0, size_n - 1, False)
        return [first_occur, last_occur]


def main():
    """Find First Last Position of Element in Sorted Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.searchRange([5,7,7,8,8,10], 8)
        [3, 4]

    Example 2:
        >>> sol.searchRange([5,7,7,8,8,10], 6)
        [-1, -1]

    Example 3:
        >>> sol.searchRange([], 0)
        [-1, -1]

    Test 1:
        >>> sol.searchRange([1], 1)
        [0, 0]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
