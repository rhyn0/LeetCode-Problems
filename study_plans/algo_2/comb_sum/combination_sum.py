# Standard Library
import doctest


class Solution:  # noqa: D101
    def combinationSum(  # spec
        self,
        candidates: list[int],
        target: int,
    ) -> list[list[int]]:
        """Return all combinations using numbers from candidates to sum to target.

        Each element is candidates is distinct and has unlimited uses available.

        Args:
            candidates (List[int]): sequence of elements to sum with
            target (int): target sum to reach

        Returns:
            List[List[int]]: all possible combinations
        """
        size_n = len(candidates)
        ret_lists = []
        candidates.sort()

        def backtrack(
            remainder: int,
            start: int,
            tail: list[int] = [],  # noqa: B006
        ) -> None:
            if remainder == 0:
                ret_lists.append(list(tail))
                return
            if remainder < 0:
                return

            for i in range(start, size_n):
                tail.append(candidates[i])
                backtrack(remainder - candidates[i], i, tail)
                tail.pop()

        backtrack(target, 0)
        return ret_lists


def main() -> None:
    """Combination Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.combinationSum([2,3,6,7], 7)
        [[2, 2, 3], [7]]

    Example 2:
        >>> sol.combinationSum([2,3,5], 8)
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    Example 3:
        >>> sol.combinationSum([2], 1)
        []
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
