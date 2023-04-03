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
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:  # spec
        """Invert a given binary tree.

        Inversion is that left and right swap for each root node in tree.

        Args:
            root (TreeNode | None): Given tree, if no nodes in tree this is None

        Returns:
            TreeNode | None: Return altered tree
        """
        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def main():
    """Invert Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),\
            TreeNode(7, TreeNode(6), TreeNode(9))))
        TreeNode(4, TreeNode(7, TreeNode(9, None, None), TreeNode(6, None, None)),\
 TreeNode(2, TreeNode(3, None, None), TreeNode(1, None, None)))
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
