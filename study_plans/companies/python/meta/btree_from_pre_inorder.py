"""Meta Interview Question Practice List on LeetCode.

105. Construct Binary Tree from Preorder and Inorder Traversal on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [3,9,20,15,7], [9,3,15,20,7]
    >>> example_case_2 = [-1], [-1]

Example 1:
    >>> sol.buildTree(*example_case_1)
    TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

Example 2:
    >>> sol.buildTree(*example_case_2)
    TreeNode(-1, None, None)
"""  # noqa: E501

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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """Return teh assembled binary tree from the given orderings.

        Args:
            preorder (list[int]): Preorder traversal of tree
            inorder (list[int]): inorder traversal of tree

        Returns:
            TreeNode | None: Tree
        """
        preorder_idx = 0
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}

        def handle_subtree(left: int, right: int) -> TreeNode | None:
            nonlocal preorder_idx
            if left > right:
                return None
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)

            preorder_idx += 1

            root_inorder_idx = inorder_idx_map[root_val]
            root.left = handle_subtree(left, root_inorder_idx - 1)
            root.right = handle_subtree(root_inorder_idx + 1, right)

            return root

        return handle_subtree(0, len(preorder) - 1)
