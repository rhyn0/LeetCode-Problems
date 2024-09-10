# Standard Library
import doctest


class Solution:  # noqa: D101
    # use for final return, avoid int overflow
    MODULO = 10**9 + 7

    def numFactoredBinaryTrees(self, arr: list[int]) -> int:  # spec
        """Return number of binary trees that can be made from input list.

        Each value in input array can be used unlimited times, but each
        non-leaf node's value must be the product of its two children nodes.

        Args:
            arr (List[int]): Monotonically increasing integer array,
                all values greater than 1

        Returns:
            int: Number of binary trees possible to make modulo (10**9 + 7)
        """
        arr.sort()
        possible_trees = {num: 1 for num in arr}
        for i, root_num in enumerate(arr):
            possible_trees[root_num] += sum(
                possible_trees[left_num] * possible_trees[right_num]
                for left_num in arr[:i]
                if root_num % left_num == 0
                and (right_num := root_num / left_num) in possible_trees
            )
        # should have a modulo operation on the set part to avoid overflow
        return sum(possible_trees.values()) % self.MODULO


def main() -> None:
    """Binary Trees with Factors on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.numFactoredBinaryTrees([2, 4])
        3

    Example 2:
        >>> sol.numFactoredBinaryTrees([2,4,5,10])
        7

    Test 1:
        >>> sol.numFactoredBinaryTrees([45,42,2,18,23,1170,12,41,40,9,47,\
        24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,\
        22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48])
        777
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
