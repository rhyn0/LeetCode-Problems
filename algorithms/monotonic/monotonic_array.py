# Standard Library
from itertools import pairwise
from operator import ge
from operator import le


class Solution:  # noqa: D101
    def isMonotonic(self, nums: list[int]) -> bool:  # spec
        """Return whether array of numbers is monotonic or not.

        Monotonic means that array is strictly increasing or strictly decreasing

        Args:
            nums (List[int]): array to consider for being monotonic

        Returns:
            bool: True if monotonic, else False
        """
        comparator = le if nums[0] <= nums[-1] else ge
        # for i, j in pairwise(nums):  # pairwise immediately stops if length one array
        #     if not comparator(i, j):
        #         return False
        # return True
        # make it pythonic
        return all(comparator(i, j) for i, j in pairwise(nums))


class SolutionLeet:  # noqa: D101
    def isMonotonic(self, nums: list[int]) -> bool:  # spec
        """Comparison for speed."""
        incr = decr = True
        for i, j in pairwise(nums):
            if i > j:
                incr = False
            elif i < j:
                decr = False
        return incr or decr


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMonotonic([1, 2, 2, 3]))  # true
    print(sol.isMonotonic([6, 5, 4, 4]))  # true
    print(sol.isMonotonic([1, 3, 2]))  # false
    print(sol.isMonotonic([1]))  # true
