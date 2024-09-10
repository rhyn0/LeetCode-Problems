"""Essentials of Dynamic Programming Trees Problem on LeetCode.

124. Binary Tree Maximum Path Sum on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [1,2,3]
    >>> example_case_2 = [-10,9,20,None,None,15,7]
    >>> my_test_case_1 = [1]
    >>> my_test_case_2 = [-10]
    >>> my_test_case_3 = [-10, -1, -2]
    >>> test_case_1 = [1,-2,-3,1,3,-2,None,-1]

Example 1:
    >>> sol.maxPathSum(build_tree(example_case_1))
    6

Example 2:
    >>> sol.maxPathSum(build_tree(example_case_2))
    42

My Test Case 1:
    >>> sol.maxPathSum(build_tree(my_test_case_1))
    1

My Test Case 2:
    >>> sol.maxPathSum(build_tree(my_test_case_2))
    -10

My Test Case 3:
    >>> sol.maxPathSum(build_tree(my_test_case_3))
    -1

Test Case 1:
    >>> sol.maxPathSum(build_tree(test_case_1))
    3
"""

from __future__ import annotations

# Standard Library
import sys


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


class InvalidBinaryTreeError(Exception):
    """Exception for an improperly defined binary tree."""

    def __init__(self, *args: object) -> None:
        """Default message and pass though args."""
        super().__init__("Invalid definition", *args)


def build_tree(node_list: list[int | None]) -> TreeNode:
    """Return binary tree made of TreeNode from inorder array."""
    if not node_list or node_list[0] is None:
        raise InvalidBinaryTreeError
    tree_node_que = []
    input_queue = node_list[1:]
    root_node = TreeNode(node_list[0])
    tree_node_que.append(root_node)
    while input_queue:
        left_input = input_queue.pop(0) if input_queue else None
        right_input = input_queue.pop(0) if input_queue else None
        current = tree_node_que.pop(0)
        if left_input is not None:
            left = TreeNode(left_input)
            current.left = left
            tree_node_que.append(left)
        if right_input is not None:
            right = TreeNode(right_input)
            current.right = right
            tree_node_que.append(right)
    return root_node


class Solution:  # noqa: D101

    def maxPathSum(self, root: TreeNode | None) -> int:
        """Given a non-empty tree, return the maximum sum a from a non-empty path.

        A path is available between any adjacent
        nodes - bidirectional edges.
        """
        best_path_overall = float("-inf")

        def helper(curr_node: TreeNode | None) -> int:
            nonlocal best_path_overall
            if not curr_node:
                return 0

            left_total = helper(curr_node=curr_node.left)
            right_total = helper(curr_node=curr_node.right)

            best_path_to_return = max(
                left_total + curr_node.val,
                curr_node.val + right_total,
                curr_node.val,
            )
            best_path_overall = max(
                best_path_overall,
                left_total + curr_node.val + right_total,
                best_path_to_return,
            )

            return best_path_to_return

        helper(curr_node=root)

        return best_path_overall


class Solution2:
    """This approach is more object oriented to split code concerns.

    We get some performance improvement by not using a float as initial val.

    >>> example_case_1 = [1,2,3]
    >>> example_case_2 = [-10,9,20,None,None,15,7]
    >>> my_test_case_1 = [1]
    >>> my_test_case_2 = [-10]
    >>> my_test_case_3 = [-10, -1, -2]
    >>> test_case_1 = [1,-2,-3,1,3,-2,None,-1]

    Example 1:
        >>> Solution2().maxPathSum(build_tree(example_case_1))
        6

    Example 2:
        >>> Solution2().maxPathSum(build_tree(example_case_2))
        42

    My Test Case 1:
        >>> Solution2().maxPathSum(build_tree(my_test_case_1))
        1

    My Test Case 2:
        >>> Solution2().maxPathSum(build_tree(my_test_case_2))
        -10

    My Test Case 3:
        >>> Solution2().maxPathSum(build_tree(my_test_case_3))
        -1

    Test Case 1:
        >>> Solution2().maxPathSum(build_tree(test_case_1))
        3
    """

    def __init__(self) -> None:
        """Initialize the nonlocal best path seen."""
        self.ans = -sys.maxsize - 1

    def helper(self, curr_node: TreeNode | None):  # noqa: D102
        if not curr_node:
            return 0

        left_total = self.helper(curr_node=curr_node.left)
        right_total = self.helper(curr_node=curr_node.right)

        best_path_to_return = max(
            left_total + curr_node.val,
            curr_node.val + right_total,
            curr_node.val,
        )
        self.ans = max(
            self.ans,
            left_total + curr_node.val + right_total,
            best_path_to_return,
        )

        return best_path_to_return

    def maxPathSum(self, root: TreeNode | None) -> int:  # noqa: D102
        self.helper(root)
        return self.ans
