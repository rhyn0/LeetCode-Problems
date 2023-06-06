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
    def isSubtree(self, root: TreeNode | None, subroot: TreeNode | None) -> bool:
        """Return if ``subRoot`` is a subtree of ``root``.

        Args:
            root (TreeNode | None): main root tree
            subroot (TreeNode | None): sub root to check for

        Returns:
            bool: True if ``subRoot`` is a subtree of ``root`` otherwise False
        """

        def match_sub(m_root: TreeNode | None, sub_root: TreeNode | None) -> bool:
            if not m_root and not sub_root:
                return True
            if m_root and sub_root and m_root.val == sub_root.val:
                return match_sub(m_root.left, sub_root.left) and match_sub(
                    m_root.right,
                    sub_root.right,
                )
            return False

        def dfs(main_root: TreeNode | None, sub_root: TreeNode | None) -> bool:
            if not main_root:
                return False
            if match_sub(main_root, sub_root):
                return True
            return dfs(main_root.left, sub_root) or dfs(main_root.right, sub_root)

        return dfs(root, subroot)


def main() -> None:
    """Subtree of Another Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)),\
            TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2)))
        True

    Example 2:
        >>> sol.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1),\
            TreeNode(2, TreeNode(0))),TreeNode(5)), \
                TreeNode(4, TreeNode(1), TreeNode(2)))
        False

    Test 1:
        >>> sol.isSubtree(TreeNode(1, TreeNode(1)), TreeNode(1))
        True
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
