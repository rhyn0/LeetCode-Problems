"""Daily Challenge for June 16, 2023 on LeetCode."""

# Standard Library
import doctest
from itertools import accumulate
from math import comb
from operator import mul


class Solution:  # noqa: D101
    FORCED_ORDER_TREE_LEN = 2

    def numOfWays(self, nums: list[int]) -> int:
        """Return number of ways to reorder insertion order for this BST.

        `nums` creates a BST, how many other permutations of `nums` exist
        such that the same BST will be produced?
        Example:
          [2, 1, 3] is the same as [2, 3, 1] in this case.

        The number of permutations must be modulo by (10^9 + 7).

        Args:
            nums (list[int]): Original order of BST

        Returns:
            int: Number of permutations, modulo (10^9 + 7)
        """
        leet_mod = 10**9 + 7

        def subtree_combinations(tree_arr: list[int]) -> int:
            if len(tree_arr) <= self.FORCED_ORDER_TREE_LEN:
                return 1

            root = tree_arr[0]
            left, right = [], []
            for val in tree_arr[1:]:
                if val < root:
                    left.append(val)
                else:
                    right.append(val)

            len_left, len_right = len(left), len(right)
            return (
                comb(len_left + len_right, len_left)
                * subtree_combinations(left)
                * subtree_combinations(right)
            )

        # the given `nums` is already one permutation, can't return a match
        return (subtree_combinations(nums) - 1) % leet_mod

    def numOfWaysSelf(self, nums: list[int]) -> int:
        """Return same as above using self calculations."""
        leet_mod = 10**9 + 7

        def combs(left_len: int, right_len: int) -> int:
            return (
                factorials[left_len + right_len]
                // factorials[left_len]
                // factorials[right_len]
            )

        def subtree_combinations(tree_arr: list[int]) -> int:
            if len(tree_arr) <= self.FORCED_ORDER_TREE_LEN:
                return 1

            root = tree_arr[0]
            left = [val for val in tree_arr if val < root]
            right = [val for val in tree_arr if val > root]

            len_left, len_right = len(left), len(right)
            return (
                combs(len_left, len_right)
                * subtree_combinations(left)
                * subtree_combinations(right)
            )

        factorials = [1, *list(accumulate(range(1, len(nums) + 1), mul))]
        # the given `nums` is already one permutation, can't return a match
        return (subtree_combinations(nums) - 1) % leet_mod


def main() -> None:
    """1569. Number of Ways to Reorder Array to Get Same BST on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [2,1,3]
        >>> example_case_2 = [3,4,5,1,2]
        >>> example_case_3 = [1,2,3]

    Example 1:
        >>> sol.numOfWays(example_case_1)
        1

    Example 2:
        >>> sol.numOfWays(example_case_2)
        5

    Example 3:
        >>> sol.numOfWays(example_case_3)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
