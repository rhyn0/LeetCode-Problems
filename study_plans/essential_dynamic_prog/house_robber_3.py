"""Essentials of Dynamic Programming Trees Problem on LeetCode.

House Robber 3 on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = build_tree([3,2,3,None,3,None,1])
    >>> example_case_2 = build_tree([3,4,5,1,3,None,1])

Example 1:
    >>> sol.rob(example_case_1)
    7

Example 2:
    >>> sol.rob(example_case_2)
    9
"""

from __future__ import annotations

# Standard Library
from collections import defaultdict
from collections import deque


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
    def rob(self, root: TreeNode | None) -> int:
        """Rob a set of houses that form a binary tree.

        Parent children houses can not be robbed without an alarm sounding.
        Sibling houses do not have this restriction.

        Args:
            root (TreeNode | None): Root of the houses

        Returns:
            int: Maximum amount of value to be robbed from houses
        """
        index_to_children = defaultdict(list)
        tree = []  # recording of our index to that node's value
        num_nodes = -1

        if root is None:
            return 0
        q = deque([(root, -1)])
        while q:
            curr_node, curr_index = q.popleft()
            if curr_node is not None:
                num_nodes += 1
                tree.append(curr_node.val)
                index_to_children[curr_index].append(num_nodes)
                q.append((curr_node.left, num_nodes))
                q.append((curr_node.right, num_nodes))

        dp_to_rob = [0] * (num_nodes + 1)
        dp_did_not_rob = [0] * (num_nodes + 1)

        # from the bottom of the tree to root, either rob this node or dont
        # both paths are worth iterating and tracking
        for i in reversed(range(num_nodes + 1)):
            if not index_to_children[i]:  # leaf
                dp_to_rob[i] = tree[i]
                dp_did_not_rob[i] = 0
            else:
                dp_to_rob[i] = tree[i] + sum(
                    dp_did_not_rob[child] for child in index_to_children[i]
                )
                dp_did_not_rob[i] = sum(
                    max(dp_to_rob[child], dp_did_not_rob[child])
                    for child in index_to_children[i]
                )

        return max(dp_did_not_rob[0], dp_to_rob[0])
