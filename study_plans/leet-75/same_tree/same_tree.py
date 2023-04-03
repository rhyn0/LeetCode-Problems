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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """Return if both given trees are structurally the same.

        Args:
            p (TreeNode | None): first tree
            q (TreeNode | None): first tree

        Returns:
            bool: True if same, False otherwise
        """
        return (
            p is q
            if p is None or q is None
            else (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        )


def main():
    """Same Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
        True

    Example 2:
        >>> sol.isSameTree(TreeNode(1, TreeNode(2), None), TreeNode(1, None, TreeNode(2)))
        False

    Example 3:
        >>> sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2)))
        False
    """  # noqa: E501


if __name__ == "__main__":
    doctest.testmod(verbose=True)
