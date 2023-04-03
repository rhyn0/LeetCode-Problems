# Standard Library
import doctest


class Solution:  # noqa: D101
    def canPartition(self, nums: list[int]) -> bool:
        """Given an array of numbers, return if possible to make 2 equal sum subsets.

        Subset means that the partitions do not need to be contiguous numbers

        Args:
            nums (List[int]): Array of numbers to use

        Returns:
            bool: True if possible to partition in this way, False otherwise
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        subset_sum = total_sum // 2
        can_make = [True] + [False] * subset_sum  # can always make 0
        for num in nums:
            for value_sum in range(subset_sum, num - 1, -1):
                can_make[value_sum] |= can_make[value_sum - num]
        return can_make[subset_sum]


def main():
    """Partition Equal Subset Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.canPartition([1, 5, 11, 5])
        True

    Example 2:
        >>> sol.canPartition([1,2,3,5])
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
