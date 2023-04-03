from __future__ import annotations

# Standard Library
import doctest


class Solution:  # noqa: D101
    def copyRandomList(self, head: Node | None) -> Node | None:  # spec
        """Make a deep copy of linked list where each node has a random pointer.

        Random pointer can point to None or any node in the list

        Args:
            head (Node | None): Original list, None if list is empty

        Returns:
            Node | None: New Deep copy, or None if no list
        """
        if head is None:
            return None
        curr, second = head, head.next
        while curr:
            curr.next = Node(curr.val, second)
            curr = second
            if second is not None:
                second = second.next

        old = head
        while old and old.next:
            new = old.next
            if old.random is not None:
                new.random = old.random.next
            old = new.next

        old, head, prev = head, head.next, None
        while old:
            if prev:
                prev.next = old.next
            prev = old.next
            old.next, old = None, old.next.next

        return head


def main():
    """Copy List with Random Pointer on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> l_nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
        >>> l_nodes[1].random = l_nodes[0]
        >>> l_nodes[2].random = l_nodes[4]
        >>> l_nodes[3].random = l_nodes[2]
        >>> l_nodes[4].random = l_nodes[0]
        >>> for i in range(len(l_nodes) - 1):
        ...     l_nodes[i].next = l_nodes[i + 1]
        >>> new = sol.copyRandomList(l_nodes[0])
        >>> new
        Node(7, random=None, next=Node(13, random=7, next=Node(11, random=1, next=Node(10, random=11, next=Node(1, random=7, next=None)))))
        >>> id(new) != id(l_nodes[0])
        True
    """  # noqa: E501


class Node:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        x: int,
        next_: Node | None = None,
        random: Node | None = None,
    ):
        self.val = int(x)
        self.next = next_
        self.random = random

    def __repr__(self) -> str:  # noqa: D105
        return f"Node({self.val}, random={self.random.val if self.random else None},\
            next={self.next})"


if __name__ == "__main__":
    doctest.testmod(verbose=True)
