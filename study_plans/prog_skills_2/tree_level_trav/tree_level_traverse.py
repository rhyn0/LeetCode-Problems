from __future__ import annotations

# Standard Library
from collections import deque


class Node:  # noqa: D101
    __slots__ = "val", "children"

    def __init__(  # noqa: D107
        self, value: int | None = None, children: list[Node] | None = None
    ):
        self.val = value
        self.children = children


class Solution:  # noqa: D101
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        """Return n-ary tree as List of Lists in level order traversal.

        First entry in returned List is the list containing the root,
        then its children and so on.

        Args:
            root (Node | None): Root node, or None if no root.

        Returns:
            list[list[int]]: List of Lists showing level order traversal
        """
        if root is None:
            return []
        q, ret_list = deque(), []
        q.append((1, root))
        while len(q):
            level, curr = q.popleft()
            if level > len(ret_list):
                ret_list.append([])
            ret_list[level - 1].append(curr.val)
            if curr.children:
                q.extend([(level + 1, c) for c in curr.children])
        return ret_list


if __name__ == "__main__":
    sol = Solution()
    sol.levelOrder(
        Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    )  # [[1], [3, 2, 4], [5, 6]]
    sol.levelOrder(
        Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    )  # [[1], [3, 2, 4], [5, 6]]
