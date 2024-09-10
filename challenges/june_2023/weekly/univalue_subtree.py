"""Weekly Challenge for Week 5 of June 2023 on LeetCode."""

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
    def countUnivalSubtree(self, root: TreeNode | None) -> int:
        """Return number of uni-value subtrees present in the given tree.

        A uni-value subtree is a binary tree that consists of the same
        node value for all nodes that exist in the tree

        Args:
            root (TreeNode | None): Tree to check, None means empty tree

        Returns:
            int: Number of uni-value subtrees
        """
        count = 0

        def dfs(node: TreeNode | None) -> bool:
            # Returns whether current node is a univalue subtree
            nonlocal count
            if node is None:
                # leaves are univalue
                return True

            left_is_univalue = dfs(node.left)
            right_is_univalue = dfs(node.right)

            if left_is_univalue and right_is_univalue:
                if node.left is not None and node.val != node.left.val:
                    return False
                if node.right is not None and node.val != node.right.val:
                    return False

                count += 1
                return True
            # children don't match so fail it
            return False

        dfs(root)
        return count


def main() -> None:
    """250. Count Univalue Subtrees on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = build_tree([5,1,5,5,5,None,5])
        >>> example_case_2 = None
        >>> example_case_3 = build_tree([5,5,5,5,5,None,5])
        >>> test_case_1 = build_tree([1,1,1,5,5,None,5])

    Example 1:
        >>> sol.countUnivalSubtree(example_case_1)
        4

    Example 2:
        >>> sol.countUnivalSubtree(example_case_2)
        0

    Example 3:
        >>> sol.countUnivalSubtree(example_case_3)
        6

    Test 1:
        >>> sol.countUnivalSubtree(test_case_1)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
