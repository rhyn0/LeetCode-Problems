# Standard Library
import doctest


class Solution:  # noqa: D101
    def canJump(self, nums: list[int]) -> bool:  # spec
        """Return if possible to jump from first index to last index of array.

        Number of jumps from position i is set by nums[i]

        Args:
            nums (List[int]): Array of jump counts

        Returns:
            bool: True if possible, False otherwise
        """
        if not nums:
            return True
        size_n = len(nums)
        max_ind = 0
        for i, jump_count in enumerate(nums):
            max_ind = max(max_ind, i + jump_count)
            if max_ind >= size_n - 1:
                return True
            if max_ind == i:
                return False

        return False

    def canJumpRev(self, nums: list[int]) -> bool:  # spec
        """Return if possible to jump from first index to last index of array."""
        size_n = len(nums)
        earliest_pos = size_n - 1
        for i in range(size_n - 1, -1, -1):
            if nums[i] + i >= earliest_pos:
                earliest_pos = i
        return earliest_pos == 0


def main():
    """Jump Game on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.canJump([2, 3, 1, 1, 4])
        True

    Example 2:
        >>> sol.canJump([3, 2, 1, 0, 4])
        False

    Test 1:
        >>> sol.canJump([0])
        True

    Test 2:
        >>> sol.canJump([2, 0, 0])
        True

    Greedy
    Example 1:
        >>> sol.canJumpRev([2, 3, 1, 1, 4])
        True

    Example 2:
        >>> sol.canJumpRev([3, 2, 1, 0, 4])
        False

    Test 1:
        >>> sol.canJumpRev([0])
        True

    Test 2:
        >>> sol.canJumpRev([2, 0, 0])
        True
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
