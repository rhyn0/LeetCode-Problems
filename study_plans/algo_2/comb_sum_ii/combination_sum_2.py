# Standard Library
import doctest


class Solution:  # noqa: D101
    def combinationSum2(  # spec
        self,
        candidates: list[int],
        target: int,
    ) -> list[list[int]]:
        """Return all combinations using numbers from candidates to sum to target.

        Args:
            candidates (List[int]): sequence of elements to sum with
            target (int): target sum to reach

        Returns:
            List[List[int]]: all possible combinations
        """
        ret_lists = []
        candidates.sort()

        def backtrack(
            remainder: int,
            start_ind: int,
            tail: list[int] = [],  # noqa: B006
        ) -> None:
            if remainder == 0:
                ret_lists.append(list(tail))
                return

            for i, cand_num in enumerate(candidates[start_ind:], start=start_ind):
                if i > start_ind and cand_num == candidates[i - 1]:
                    continue
                if remainder < cand_num:
                    break
                tail.append(cand_num)
                backtrack(remainder - cand_num, i + 1, tail)
                tail.pop()

        backtrack(target, 0)
        return ret_lists


def main() -> None:
    """Combination Sum II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.combinationSum2([10,1,2,7,6,1,5], 8)
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    Example 1:
        >>> sol.combinationSum2([2,5,2,1,2], 5)
        [[1, 2, 2], [5]]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
