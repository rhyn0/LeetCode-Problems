from __future__ import annotations

# Standard Library
from collections import deque
import doctest


class Node:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        next_: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_

    def __repr__(self) -> str:  # noqa: D105
        return f"Node({self.val}, {self.left}, {self.right})"


class Solution:  # noqa: D101
    def connect(self, root: Node | None) -> Node | None:
        """Modify given tree to point each node to next node in level.

        Use Node.next and it must point to the node to the left of
        the current one in its level.

        Args:
            root (Node | None): Root of tree to modify

        Returns:
            Node | None: Root node if supplied a tree with nodes, None otherwise
        """
        if not root:
            return None

        level_q = deque([root])
        while level_q:
            size = len(level_q)
            for i in range(size):
                curr_node = level_q.popleft()

                if i < size - 1:
                    # since we add nodes from left to right
                    # #only update until the second last element in each level
                    # and q[0] since they are in order and pop off the left most one
                    curr_node.next = level_q[0]

                if curr_node.left:
                    level_q.append(curr_node.left)
                if curr_node.right:
                    level_q.append(curr_node.right)

        return root


def main():
    """Populating Next Right Pointers in Each Node II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.connect(Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(7))))
        Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, None, \
            Node(7, None, None)))

    Example 2:
        >>> sol.connect(None)
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
