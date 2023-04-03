# Standard Library
import doctest


class Solution:  # noqa: D101
    def jump(self, nums: list[int]) -> int:
        """Return minimum number of jumps to go from first index to last.

        All input arrays must have a solution.

        Args:
            nums (List[int]): jump array

        Returns:
            int: minimum number of jumps to reach end.
        """
        size_n = len(nums)
        nums[-1] = 0  # 0 steps to get to last index from last
        for i in range(size_n - 2, -1, -1):
            nums[i] = (
                (1 + min(nums[i + 1 : i + 1 + nums[i]])) if nums[i] != 0 else size_n
            )
        return nums[0]


def main():
    """Jump Game II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.jump([2, 3, 1, 1, 4])
        2

    Example 2:
        >>> sol.jump([2, 3, 0, 1, 4])
        2

    Test 1:
        >>> sol.jump([1, 2, 3])
        2
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
