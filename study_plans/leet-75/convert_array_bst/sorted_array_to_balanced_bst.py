from __future__ import annotations

# Standard Library
import doctest


class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:  # noqa: D105
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:  # noqa: D101
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:  # spec
        """Convert sorted array to balanced BST.

        Uses recursive algorithm to choose middle point of array
        and then construct left and right.

        Args:
            nums (List[int]): Sorted array to turn into BST

        Returns:
            TreeNode | None: balanced BST, None if no elements in list
        """

        def recursive_builder(left: int, right: int) -> TreeNode | None:
            if left >= right:
                return None
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left, root.right = (
                recursive_builder(left, middle),
                recursive_builder(middle + 1, right),
            )
            return root

        if not nums:
            return None
        return recursive_builder(0, len(nums))


def main():
    """Convert Sorted Array to Binary Search Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.sortedArrayToBST([-10, -3, 0, 5, 9])
        TreeNode(0, TreeNode(-3, TreeNode(-10, None, None), None), TreeNode(9,\
            TreeNode(5, None, None), None))

    Example 2:
        >>> sol.sortedArrayToBST([1, 3])
        TreeNode(3, TreeNode(1, None, None), None)
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
