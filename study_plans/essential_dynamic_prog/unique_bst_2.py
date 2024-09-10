"""Essentials of Dynamic Programming Trees Problem on LeetCode.

Unique Binary Search Trees II on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 3
    >>> example_case_2 = 1

Example 1:
    >>> sol.generateTrees(example_case_1)
    [TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, None))), \
        TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None)), \
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), \
                TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)), None), \
                    TreeNode(3, TreeNode(2, TreeNode(1, None, None), None), None)]

Example 2:
    >>> sol.generateTrees(example_case_2)
    [TreeNode(1, None, None)]
"""

from __future__ import annotations

# Standard Library
from functools import cache


class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val=0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Debugging representation."""
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def prefix_traverse_bst(root: TreeNode) -> list:  # noqa: D103
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            if node.left or node.right:  # Only add children if it's a non-leaf node
                stack.append(node.right)
                stack.append(node.left)
        else:
            result.append(None)

    return result


class Solution:  # noqa: D101
    def generateTrees(self, n: int):
        """Return all unique possible BST, given the number of nodes in the tree.

        The array of BST must be each structurally unique from each other.
        """

        # cache based on start end keys
        @cache
        def backtracker(start_id: int, end_id: int) -> list[TreeNode | None]:
            # return the subtrees available. If no sub node, then None
            result = []
            if start_id > end_id:
                result.append(None)
                return result

            # for all other nodes, choose a root for this subtree
            for root_id in range(start_id, end_id + 1):  # end_id is inclusive
                left_sub_tree = backtracker(start_id, root_id - 1)
                right_sub_tree = backtracker(root_id + 1, end_id)
                for left in left_sub_tree:
                    for right in right_sub_tree:
                        result.append(  # noqa: PERF401
                            TreeNode(root_id, left=left, right=right),
                        )

            return result

        return backtracker(1, n)
