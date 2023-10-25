"""Daily Challenge on LeetCode: Problem #515 [Medium]."""
# Standard Library
from collections import deque
import doctest
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
    def largestValues(self, root: TreeNode | None) -> list[int]:
        """Return the greatest value from each level of a binary tree."""
        if root is None:
            return []

        que: deque[TreeNode] = deque([root])
        output = []
        while que:
            layer_width = len(que)
            visited = []
            for _ in range(layer_width):
                node = que.popleft()
                visited.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            output.append(max(visited))

        return output

    def largestValuesDFS(self, root: TreeNode | None) -> list[int]:
        """Return same as above using DFS."""
        if root is None:
            return []

        output = []

        def dfs(node: TreeNode, level: int) -> None:
            if len(output) == level:
                output.append(node.val)
            else:
                output[level] = max(output[level], node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return output

    def largestValuesDFSIter(self, root: TreeNode | None) -> list[int]:
        """Return same as above using DFS iteratively."""
        if root is None:
            return []

        output = []
        stack: list[tuple[TreeNode, int]] = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if len(output) == level:
                output.append(node.val)
            else:
                output[level] = max(output[level], node.val)

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return output


def main() -> None:
    """515. Find Largest Value in Each Tree Row on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,3,2,5,3,None,9]
        >>> example_case_2 = [1,2,3]
        >>> self_test_1 = None

    Example 1:
        >>> sol.largestValues(build_tree(example_case_1))
        [1, 3, 9]
        >>> sol.largestValuesDFS(build_tree(example_case_1))
        [1, 3, 9]
        >>> sol.largestValuesDFSIter(build_tree(example_case_1))
        [1, 3, 9]

    Example 2:
        >>> sol.largestValues(build_tree(example_case_2))
        [1, 3]
        >>> sol.largestValuesDFS(build_tree(example_case_2))
        [1, 3]
        >>> sol.largestValuesDFSIter(build_tree(example_case_2))
        [1, 3]


    Self 1:
        >>> sol.largestValues(self_test_1)
        []
        >>> sol.largestValuesDFS(self_test_1)
        []
        >>> sol.largestValuesDFSIter(self_test_1)
        []
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
