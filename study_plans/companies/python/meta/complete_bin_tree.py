"""Meta Interview Question Practice List on LeetCode.

958. Check Completeness of a Binary Tree on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = build_tree([1,2,3,4,5,6])
    >>> example_case_2 = build_tree([1,2,3,4,5,None,7])
    >>> test_case_1 = build_tree([1,2,3,5])

Example 1:
    >>> sol.isCompleteTree(example_case_1)
    True
    >>> sol.isCompleteTreeDFS(example_case_1)
    True

Example 2:
    >>> sol.isCompleteTree(example_case_2)
    False
    >>> sol.isCompleteTreeDFS(example_case_2)
    False

Test Case 1:
    >>> sol.isCompleteTree(test_case_1)
    True
    >>> sol.isCompleteTreeDFS(test_case_1)
    True
"""

# Standard Library
from collections import deque
from typing import Self


class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Debugging representation."""
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class InvalidBinaryTreeError(Exception):
    """Exception for an improperly defined binary tree."""

    def __init__(self, nodes: list, *args: object) -> None:
        """Default message and pass though args."""
        super().__init__(f"Invalid definition: ({','.join(nodes)})", *args)


def build_tree(node_list: list[int | None] | None) -> TreeNode | None:
    """Return binary tree made of TreeNode from inorder array."""
    if node_list is None:
        # intentinal None build
        return None
    if not node_list or node_list[0] is None:
        raise InvalidBinaryTreeError(node_list)
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


def deconstruct_tree(root: TreeNode) -> list[int | None]:
    """Return inorder array from binary tree made of TreeNode."""
    if not root:
        return []
    tree_node_que: list[TreeNode | None] = []
    output_queue: list[int | None] = []
    tree_node_que.append(root)
    while tree_node_que:
        current = tree_node_que.pop(0)
        if current is None:
            output_queue.append(None)
            continue
        output_queue.append(current.val)
        if current.left is None and current.right is None:
            continue
        tree_node_que.append(current.left)
        tree_node_que.append(current.right)
    return output_queue


class Solution:  # noqa: D101
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        """Return whether the given root node is of a complete binary tree.

        Args:
            root (TreeNode | None): Root node

        Returns:
            bool: True if it is a complete binary tree, False otherwise
        """
        que: deque[TreeNode | None] = deque()
        que.append(root)
        none_seen = False
        while que:
            curr_node = que.popleft()
            if curr_node is None:
                none_seen = True
                continue
            if none_seen:
                return False

            que.append(curr_node.left)
            que.append(curr_node.right)
        return True

    def isCompleteTreeDFS(self, root: TreeNode | None) -> bool:
        """Return same as above using DFS method."""

        def count_nodes(node: TreeNode | None) -> int:
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        num_nodes = count_nodes(root)

        def dfs(node: TreeNode | None, curr_index: int) -> bool:
            nonlocal num_nodes
            if not node:
                return True
            if curr_index >= num_nodes:
                return False
            return dfs(node.left, 2 * curr_index + 1) and dfs(
                node.right,
                2 * curr_index + 2,
            )

        return dfs(root, 0)
