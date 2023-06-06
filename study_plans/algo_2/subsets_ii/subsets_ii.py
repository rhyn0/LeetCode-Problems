# Standard Library
import doctest


class Solution:  # noqa: D101
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:  # spec
        """Return power set of sequence that may contain duplicate numbers.

        Args:
            nums (List[int]): sequence

        Returns:
            List[List[int]]: Power set
        """
        size_n = len(nums)
        ret_lists = []

        def backtracking(first: int = 0, tail: list[int] = []) -> None:  # noqa: B006
            if len(tail) == _k:
                temp = sorted(tail)
                if temp not in ret_lists:
                    ret_lists.append(temp)
                return

            for i in range(first, size_n):
                tail.append(nums[i])
                backtracking(i + 1, tail)
                tail.pop()

        for _k in range(size_n + 1):
            backtracking()

        return ret_lists

    def subsetsWithDupCascade(self, nums: list[int]) -> list[list[int]]:
        """Return power set of sequence that may contain duplicate numbers."""
        ret_lists = [[]]
        prev_subset_size = 0
        nums.sort()

        for i, num in enumerate(nums):
            start_ind = prev_subset_size if i > 0 and num == nums[i - 1] else 0
            prev_subset_size = len(ret_lists)
            for j_el in range(start_ind, prev_subset_size):
                ret_lists.append(ret_lists[j_el] + [num])

        return ret_lists


def main() -> None:
    """Subsets II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.subsetsWithDup([1, 2, 2])
        [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

    Example 2:
        >>> sol.subsetsWithDup([0])
        [[], [0]]

    Test 1:
        >>> sol.subsetsWithDup([4,4,4,1,4])
        [[], [4], [1], [4, 4], [1, 4], [4, 4, 4], [1, 4, 4], [1, 4, 4, 4], \
            [4, 4, 4, 4], [1, 4, 4, 4, 4]]


    CASCADING approach
    Example 1:
        >>> sol.subsetsWithDupCascade([1, 2, 2])
        [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

    Example 2:
        >>> sol.subsetsWithDupCascade([0])
        [[], [0]]

    Test 1:
        >>> sol.subsetsWithDupCascade([4,4,4,1,4])
        [[], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4], \
            [4, 4, 4, 4], [1, 4, 4, 4, 4]]

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
