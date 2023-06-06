# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:  # spec
        """Return all permutations of the input list.

        Input list may contain duplicate elements,
        will not return duplicate permutations.

        Args:
            nums (List[int]): input sequence

        Returns:
            List[List[int]]: All permutations of input list
        """
        size_n = len(nums)
        ret_lists = []

        def backtrack(
            avail_nums: list[int],
            tail: list[int] = [],  # noqa: B006
        ) -> None:
            if len(tail) == size_n:
                if tail not in ret_lists:
                    ret_lists.append(tail[:])
                return
            for num in avail_nums:
                tail.append(num)
                num_copy = avail_nums[:]
                num_copy.remove(num)
                backtrack(num_copy, tail)
                tail.pop()

        backtrack(nums)
        return ret_lists

    def permuteUniqueCounter(self, nums: list[int]) -> list[list[int]]:
        """Return all permutations of the input list."""
        size_n = len(nums)
        ret_lists = []

        def backtrack(
            avail_nums: Counter[int],
            tail: list[int] = [],  # noqa: B006
        ) -> None:
            if len(tail) == size_n:
                ret_lists.append(list(tail))  # make a deep copy
                return

            for num in avail_nums:
                if avail_nums[num] <= 0:
                    continue
                tail.append(num)
                avail_nums[num] -= 1
                backtrack(avail_nums, tail)
                avail_nums[num] += 1
                tail.pop()

        backtrack(Counter(nums))
        return ret_lists


def main() -> None:
    """Permutations II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> test_case_1 = [1, 1, 2]
        >>> test_case_2 = [1, 2, 3]

    Example 1:
        >>> sol.permuteUnique(test_case_1)
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    Example 2:
        >>> sol.permuteUnique(test_case_2)
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    Example 1:
        >>> sol.permuteUniqueCounter(test_case_1)
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    Example 2:
        >>> sol.permuteUniqueCounter(test_case_2)
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
