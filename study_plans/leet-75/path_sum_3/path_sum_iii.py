from __future__ import annotations

# Standard Library
from collections import defaultdict
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
    def pathSum(self, root: TreeNode | None, target: int) -> int:  # noqa: D102
        def preorder_trav(node: TreeNode | None, /, curr_sum: int = 0) -> None:
            nonlocal count_paths
            if node is None:
                return

            curr_sum += node.val
            if curr_sum == target:
                count_paths += 1
            count_paths += hmap[curr_sum - target]
            hmap[curr_sum] += 1
            preorder_trav(node.left, curr_sum)
            preorder_trav(node.right, curr_sum)
            hmap[curr_sum] -= 1

        count_paths, hmap = 0, defaultdict(int)
        preorder_trav(root)
        return count_paths


def main():
    """Path Sum III on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8)  # noqa: E501
        3

    Test 1:
        >>> sol.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22)
        3

    Test 2:
        >>> sol.pathSum(TreeNode(1), 1)
        1

    Test 3:
        >>> sol.pathSum(TreeNode(1, TreeNode(2)), 3)
        1
    """  # noqa: E501


if __name__ == "__main__":
    doctest.testmod(verbose=True)
