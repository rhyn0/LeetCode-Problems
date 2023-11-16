from __future__ import annotations

# Standard Library
import doctest


class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:  # noqa: D105
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:  # noqa: D101
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:  # spec
        """Find the diameter of a given binary tree.

        Diameter is the longest path between two nodes on a binary tree.
        It can be counted only by the number of edges between the nodes.

        Args:
            root (TreeNode | None): binary tree

        Returns:
            int: Length of the diameter.
        """
        longest_path = 0

        def dfs(branch: TreeNode | None) -> int:
            nonlocal longest_path
            if branch is None:
                return 0
            vals = dfs(branch.left), dfs(branch.right)
            longest_path = max(longest_path, sum(vals))
            return 1 + max(vals)

        dfs(root)
        return longest_path


def main() -> None:
    """Diameter of Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),\
            TreeNode(3)))
        3

    Example 2:
        >>> sol.diameterOfBinaryTree(TreeNode(1, TreeNode(2)))
        1

    Test 1:
        >>> sol.diameterOfBinaryTree(None)
        0

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
