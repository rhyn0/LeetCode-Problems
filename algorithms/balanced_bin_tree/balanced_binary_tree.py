from __future__ import annotations

# Standard Library
import doctest


# Definition for a binary tree node.
class TreeNode:  # noqa: D101
    __slots__ = "left", "right", "val"

    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:  # noqa: D101
    def isBalanced(self, root: TreeNode | None) -> bool:  # spec
        """Return whether given binary tree is balanced.

        Binary tree is considered balanced if height of branches differs
        by no more than 1.

        Args:
            root (Optional[TreeNode]): Tree to check

        Returns:
            bool: True if balanced, otherwise False
        """

        def dfs(node_root: TreeNode | None) -> int:
            if node_root is None:
                return 0
            left_height = dfs(node_root.left)
            right_height = dfs(node_root.right)
            if -1 in (left_height, right_height):
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return dfs(root) >= 0


def main() -> None:
    """110. Balanced Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = TreeNode(\
            3,\
            left=TreeNode(9),\
            right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
        >>> example_case_2 = TreeNode(\
                1,\
                left=TreeNode(\
                    2,\
                    left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)),\
                    right=TreeNode(3)),\
                right=TreeNode(2))
        >>> example_case_3 = None

    Example 1:
        >>> sol.isBalanced(example_case_1)
        True

    Example 2:
        >>> sol.isBalanced(example_case_2)
        False

    Example 3:
        >>> sol.isBalanced(example_case_3)
        True
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
