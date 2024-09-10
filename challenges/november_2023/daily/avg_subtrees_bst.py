"""Daily Challenge for November 2 on LeetCode: Problem #2265 [Medium]."""

# Standard Library
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
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        """Return the number of nodes in a tree whose values equal their average.

        A subtree is inclusive of the root node itself.

        Args:
            root (TreeNode | None): root node of tree to consider

        Returns:
            int: Number of nodes that are equal to the average of their subtree
        """
        avg_count = 0

        def dfs(node: TreeNode | None) -> tuple[int, int]:
            """Depth first search of tree."""
            if node is None:
                return (0, 0)
            nonlocal avg_count
            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)
            curr_count = left_count + right_count + 1
            curr_sum = left_sum + right_sum + node.val
            # floor division since node.val is an int
            if curr_sum // curr_count == node.val:
                avg_count += 1
            return (curr_count, curr_sum)

        dfs(root)
        return avg_count


def main() -> None:
    """2265. Count Nodes Equal to Average of Subtree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [4,8,5,0,1,None,6]

    Example 1:
        >>> sol.averageOfSubtree(build_tree(example_case_1))
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
