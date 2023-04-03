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
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:  # spec
        """Find kth smallest element in a BST.

        Uses morris traversal to find the element and cleans up tree before exit.

        Args:
            root (TreeNode | None): Root of Tree, None if no nodes
            k (int): 1-indexed smallest element to find

        Returns:
            int: value of kth smallest element
        """
        count, curr = 0, root
        smallest = -1
        while curr is not None:
            if curr.left is None:
                count += 1
                if count == k:
                    smallest = curr.val
                curr = curr.right
            else:
                pre = curr.left
                while pre.right is not None and pre.right is not curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    count += 1
                    if count == k:
                        smallest = curr.val
                    pre.right = None
                    curr = curr.right
        return smallest


def main():
    """Kth Smallest Element in a BST on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1)
        1

    Example 2:
        >>> sol.kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)),\
            TreeNode(4)), TreeNode(6)), 3)
        3
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
