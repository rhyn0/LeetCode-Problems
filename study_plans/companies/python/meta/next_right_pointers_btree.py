"""Meta Interview Question Practice List on LeetCode.

116. Populating Next Right Pointers in Each Node on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = build_tree([1,2,3,4,5,6,7])
    >>> example_case_2 = None
    >>> test_case_1 = build_tree([-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13])

Example 1:
    >>> deconstruct_tree(sol.connect(example_case_1))
    [1, None, 2, 3, None, 4, 5, 6, 7, None]

Example 2:
    >>> deconstruct_tree(sol.connect(example_case_2))
    []

Test Case 1:
    >>> deconstruct_tree(sol.connect(test_case_1))
    [-1, None, 0, 1, None, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, 11, 12, 13, None]
"""

# Standard Library
from typing import Self


class Node:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
        next_: Self | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next_

    def __repr__(self) -> str:
        """Debugging representation."""
        return f"Node({self.val}, {self.left}, {self.right}, {self.next})"


class InvalidBinaryTreeError(Exception):
    """Exception for an improperly defined binary tree."""

    def __init__(self, nodes: list, *args: object) -> None:
        """Default message and pass though args."""
        super().__init__(f"Invalid definition: ({','.join(nodes)})", *args)


def build_tree(node_list: list[int | None] | None) -> Node | None:
    """Return binary tree made of TreeNode from inorder array."""
    if node_list is None:
        # intentinal None build
        return None
    if not node_list or node_list[0] is None:
        raise InvalidBinaryTreeError(node_list)
    tree_node_que = []
    input_queue = node_list[1:]
    root_node = Node(node_list[0])
    tree_node_que.append(root_node)
    while input_queue:
        left_input = input_queue.pop(0) if input_queue else None
        right_input = input_queue.pop(0) if input_queue else None
        current = tree_node_que.pop(0)
        if left_input is not None:
            left = Node(left_input)
            current.left = left
            tree_node_que.append(left)
        if right_input is not None:
            right = Node(right_input)
            current.right = right
            tree_node_que.append(right)
    return root_node


def deconstruct_tree(root: Node) -> list[int | None]:
    """Return inorder array from binary tree made of TreeNode."""
    if not root:
        return []
    tree_node_que: list[Node | None] = []
    output_queue: list[int | None] = []
    tree_node_que.append(root)
    while tree_node_que:
        current = tree_node_que.pop(0)
        if current is None:
            output_queue.append(None)
            continue
        output_queue.append(current.val)
        if current.next is None:
            output_queue.append(current.next)
        if current.left is None and current.right is None:
            continue
        tree_node_que.append(current.left)
        tree_node_que.append(current.right)
    return output_queue


class Solution:  # noqa: D101
    def connect(self, root: Node | None) -> Node | None:
        """Return a perfect binary tree after linking each node to its right neighbor.

        Args:
            root (Node | None): Root of tree if any

        Returns:
            Node | None: Right connected perfect binary tree.
        """
        if not root:
            return None

        leftmost = root
        while leftmost.left:
            head: Node | None = leftmost
            # do level traversal
            while head:
                # connect children together
                head.left.next = head.right  # type: ignore[union-attr]
                # connect right child to sibling left child if there is a right sibling.
                if head.next:
                    head.right.next = head.next.left  # type: ignore[union-attr]
                head = head.next

            # next level
            leftmost = leftmost.left
        return root
