# Standard Library
import doctest


class Solution:  # noqa: D101
    MIN_SIZE = 3

    def numberOfArithmeticSlices(self, nums: list[int]) -> int:  # spec
        """Return number of arithmetic slices in a given array.

        An arithmetic slice is a subarray containing an
        arithmetic series (progression) of at least size 3.

        Args:
            nums (List[int]): input array

        Returns:
            int: Number of arithmetic slices
        """
        size_n = len(nums)
        if size_n < self.MIN_SIZE:
            return 0
        prev_slices = total_slices = 0
        for i in range(2, size_n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                prev_slices += 1
                total_slices += prev_slices
            else:
                prev_slices = 0

        return total_slices


def main() -> None:
    """Arithmetic Slices on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.numberOfArithmeticSlices([1, 2, 3, 4])
        3

    Example 2:
        >>> sol.numberOfArithmeticSlices([1])
        0

    Test 1:
        >>> sol.numberOfArithmeticSlices([1, 2, 3])
        1

    Test 2:
        >>> sol.numberOfArithmeticSlices([1,2,3,4,5,6])
        10
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
