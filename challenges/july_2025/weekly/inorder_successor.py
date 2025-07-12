"""Weekly Challenge 2 for July, 2025.

285. Inorder Successor in BST on LeetCode.

====================================================

Setup:
Shouldn't be any bugs due to not choosing a node from tree
as contraint is that values are unique.

    >>> sol = Solution()
    >>> example_case_1 = build_tree([2,1,3]), TreeNode(1)
    >>> example_case_2 = build_tree([5,3,6,2,4,None,None,1]), TreeNode(6)
    >>> test_case_1 = build_tree([5,3,6,1,4,None,None,None,2]), TreeNode(4)

Example 1:
    >>> sol.inorderSuccessor(*example_case_1)
    TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))

Example 2:
    >>> sol.inorderSuccessor(*example_case_2)

Test 1:
    >>> sol.inorderSuccessor(*test_case_1)
    TreeNode(5,...
"""

# Standard Library
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
    """Build a binary tree from a level-order list of values.

    Args:
        node_list (list[int | None] | None): A list of integers or None representing
            a binary tree in level-order traversal. A value of `None` indicates
            a missing node. If the entire list is `None`, returns None.

    Returns:
        The root TreeNode of the constructed binary tree, or None if input is None.

    Raises:
        InvalidBinaryTreeError: If the input list is empty or starts with None.
    """
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
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        """Return the inorder successor of the node specified.

        Successor is defined as the smallest key greater than node specified.

        Args:
            root (TreeNode): Root of the tree
            p (TreeNode): Node to find successor of

        Returns:
            TreeNode | None: Successor if exists
        """

        def dfs_helper(node: TreeNode) -> TreeNode:
            if node.left is None:
                return node
            return dfs_helper(node.left)

        last_left_parent = None
        curr: TreeNode | None = root
        # Find current node
        while curr and curr.val != p.val:
            if curr.val < p.val:
                curr = curr.right
            else:
                last_left_parent = curr
                curr = curr.left

        if curr is None:
            raise RuntimeError

        if curr.right:
            # if we have a right child, it contains the successor
            return dfs_helper(curr.right)
        if last_left_parent:
            return last_left_parent
        # if we aren't either of above cases, there is no greater node
        return None
