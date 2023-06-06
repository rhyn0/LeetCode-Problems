# Standard Library
import doctest


class Solution:  # noqa: D101
    def rob(self, nums: list[int]) -> int:
        """Return maximum amount of money to rob from list of houses.

        Can not rob two houses that are next to each other.

        This approach uses O(1) space by modifying input array.
        But can be changed to O(n) by just creating another array.

        Args:
            nums (List[int]): Money at house[i] for each index

        Returns:
            int: Maximum amount of money to be robbed.
        """
        if len(nums) == 1:
            return nums[-1]
        nums[1] = max(nums[:2])
        for i, money in enumerate(nums[2:], start=2):
            nums[i] = max(money + nums[i - 2], nums[i - 1])

        return nums[-1]

    def rob_no_mod(self, nums: list[int]) -> int:
        """Return answer using O(1) space."""
        if len(nums) == 1:
            return nums[0]
        two_ago, one_ago = nums[0], max(nums[:2])
        for money in nums[2:]:
            two_ago, one_ago = one_ago, max(money + two_ago, one_ago)
        return one_ago


def main() -> None:
    """House Robber on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.rob([1,2,3,1])
        4
        >>> sol.rob_no_mod([1,2,3,1])
        4

    Example 2:
        >>> sol.rob([2,7,9,3,1])
        12
        >>> sol.rob_no_mod([2,7,9,3,1])
        12

    Example 3:
        >>> sol.rob([2, 1])
        2
        >>> sol.rob_no_mod([2, 1])
        2
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
