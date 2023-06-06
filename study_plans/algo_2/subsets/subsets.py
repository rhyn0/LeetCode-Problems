# Standard Library
import doctest


class Solution:  # noqa: D101
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """Return power set given a sequence of numbers.

        Order of elements in power set is not important.

        Args:
            nums (List[int]): sequence of numbers

        Returns:
            List[List[int]]: power set in list of lists form
        """
        size_n = len(nums)

        def subset_recursion(start: int) -> list[list[int]]:
            if start == size_n:
                return [[]]

            curr_num = nums[start]
            results = subset_recursion(start + 1)
            results.extend([[curr_num, *res] for res in results[:]])
            return results

        return subset_recursion(0)

    def subsets_backtracking(self, nums: list[int]) -> list[list[int]]:
        """Return power set of sequence."""
        size_n = len(nums)
        ret_lists = []

        def backtrack(start: int = 0, tail: list[int] = []) -> None:  # noqa: B006
            if len(tail) == _k:
                ret_lists.append(tail[:])
                return
            for i in range(start, size_n):
                tail.append(nums[i])
                backtrack(i + 1, tail)
                # remove last entry which is only useful for building set below
                tail.pop()

        for _k in range(size_n + 1):
            backtrack()

        return ret_lists


def main() -> None:
    """Subsets on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.subsets([1, 2, 3])
        [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

    Example 2:
        >>> sol.subsets([0])
        [[], [0]]

    Example 1:
        >>> sol.subsets_backtracking([1, 2, 3])
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    Example 2:
        >>> sol.subsets_backtracking([0])
        [[], [0]]

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
