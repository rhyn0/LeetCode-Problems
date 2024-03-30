# Standard Library
import doctest


class Solution:  # noqa: D101
    def search(self, nums: list[int], target: int) -> int:
        """Binary search on a sorted rotated array.

        Array is sorted but then rotated left by a random k positions.
        Returns position in given array.

        Runs in O(log n)

        Args:
            nums (List[int]): Sorted array with possible rotations
            target (int): number to look for

        Returns:
            int: index of number in sorted array
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # left side is not rotated
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def main() -> None:
    """Search in Rotated Sorted Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.search([4, 5, 6, 7, 0, 1, 2], 0)
        4

    Example 2:
        >>> sol.search([4,5,6,7,0,1,2], 3)
        -1

    Example 3:
        >>> sol.search([1], 3)
        -1

    Test 1:
        >>> sol.search([4,5,6,7,8,1,2,3], 8)
        4
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
