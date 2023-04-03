# Standard Library


# Definition for a binary tree node.
class TreeNode:  # noqa: D101
    __slots__ = "val", "left", "right"

    def __init__(self, val=0, left=None, right=None):  # noqa: D107
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


if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(
        3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    root2 = TreeNode(
        1,
        left=TreeNode(
            2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)
        ),
        right=TreeNode(2),
    )
    root3 = None
    print(sol.isBalanced(root1))  # True
    print(sol.isBalanced(root2))  # False
    print(sol.isBalanced(root3))  # True
