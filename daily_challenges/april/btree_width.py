"""Daily Challenge from April 19, 2023."""
from __future__ import annotations

# Standard Library
import doctest


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
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        """Return maximum width of a given binary tree.

        Width is number nodes wide at a given depth of a binary tree.

        Args:
            root (TreeNode | None): Root of tree, or None if empty tree

        Returns:
            int: max width
        """
        first_idx_layer = {}
        max_width = 0

        def dfs(node: TreeNode | None, depth: int, col_index: int) -> None:
            nonlocal max_width, first_idx_layer
            if not node:
                return

            # if new depth, we always visit left first
            # so number it
            if depth not in first_idx_layer:
                first_idx_layer[depth] = col_index

            max_width = max(max_width, col_index - first_idx_layer[depth] + 1)

            dfs(node.left, depth + 1, 2 * col_index)
            dfs(node.right, depth + 1, 2 * col_index + 1)

        dfs(root, 0, 0)
        return max_width

    def widthOfBinaryTreeBFS(self, root: TreeNode) -> int:
        """Return same as above using Breadth First Search."""
        queue: list[tuple[TreeNode, int]] = []
        max_width = 0
        # node, index of node in level
        queue.append((root, 0))
        while queue:
            level_width = len(queue)
            # peek the queue
            _, first_index = queue[0]
            last_idx = queue[-1][1]
            for _ in range(level_width):
                node, curr_idx = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * curr_idx))
                if node.right:
                    queue.append((node.right, 2 * curr_idx + 1))

            max_width = max(max_width, last_idx - first_index + 1)

        return max_width


def main() -> None:
    """Maximum Width of a Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = build_tree([1,3,2,5,3,None,9])
        >>> example_case_2 = build_tree([1,3,2,5,None,None,9,6,None,7])
        >>> example_case_3 = build_tree([1,3,2,5])

    Example 1:
        >>> sol.widthOfBinaryTree(example_case_1)
        4
        >>> sol.widthOfBinaryTreeBFS(example_case_1)
        4

    Example 2:
        >>> sol.widthOfBinaryTree(example_case_2)
        7
        >>> sol.widthOfBinaryTreeBFS(example_case_2)
        7

    Example 3:
        >>> sol.widthOfBinaryTree(example_case_3)
        2
        >>> sol.widthOfBinaryTreeBFS(example_case_3)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
