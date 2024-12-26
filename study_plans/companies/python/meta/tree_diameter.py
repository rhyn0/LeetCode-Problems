"""Meta Interview Question Practice List on LeetCode.

Previously solved - see study_plans/leet_75/diameter_btree/diameter_binary_tree.py.

543. Diameter of Binary Tree on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = build_tree([1,2,3,4,5])
    >>> example_case_2 = build_tree([1,2])

Example 1:
    >>> sol.diameterOfBinaryTree(example_case_1)
    3

Example 2:
    >>> sol.diameterOfBinaryTree(example_case_2)
    1
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
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """Return the diameter of a binary tree.

        Diameter is defined as the length of the longest path between 2 nodes.
        May or may not pass through the root.

        Args:
            root (TreeNode | None): The root of the binary tree to analyze

        Returns:
            int: Diameter of tree
        """
        # have to visit all nodes and make best attempt to build longest path for each
        # store the maximum externally to the dfs code
        longest_path = 0

        def dfs(node: TreeNode | None) -> int:
            nonlocal longest_path
            if not node:
                return 0
            # DFS both subtrees to find the longest paths in them
            left_longest = dfs(node.left)
            right_longest = dfs(node.right)
            # two options exist here, either this node is a leg of the longest path and
            # only extends the answer. OR the path that goes through this root is the
            # longest path.
            this_root_longest = left_longest + right_longest
            longest_path = max(this_root_longest, longest_path)
            # when returning to parent, only use the children paths
            # path calculation can't be tainted
            return 1 + max(left_longest, right_longest)

        dfs(root)
        return longest_path
