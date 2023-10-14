"""Daily Change for June 15, 2023 on LeetCode."""
from __future__ import annotations

# Standard Library
from collections import defaultdict
from collections import deque
import doctest
from operator import itemgetter


class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
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
    def maxLevelSum(self, root: TreeNode | None) -> int:
        """Return max sum of any level in a given tree.

        Prefer to return earlier levels.
        Root node is the first level.

        Args:
            root (TreeNode | None): Root of tree to traverse

        Returns:
            int: Level that contains the maximal sum
        """
        layers = defaultdict(int)
        que = deque()
        que.append((root, 1))
        while que:
            curr_node, level = que.popleft()
            layers[level] += curr_node.val
            if curr_node.right:
                que.append((curr_node.right, level + 1))
            if curr_node.left:
                que.append((curr_node.left, level + 1))
        # sort by layer asc, then by value desc
        # guarantees that earlier levels come first when scores match
        return sorted(layers.items(), key=itemgetter(1), reverse=True)[0][0]


def main() -> None:
    """1161. Maximum Level Sum of a Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,7,0,7,-8,None,None]
        >>> example_case_1 = [989,None,10250,98693,-89388,None,None,None,-32127]

    Example 1:
        >>> sol.maxLevelSum(build_tree(example_case_1))
        2

    Example 2:
        >>> sol.maxLevelSum(build_tree(example_case_2))
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
