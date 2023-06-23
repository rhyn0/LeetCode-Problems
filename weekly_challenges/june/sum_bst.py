"""Weekly Challenge for Week 4 of June, 2023 on LeetCode."""
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
    def twoSumBSTs(
        self,
        root1: TreeNode | None,
        root2: TreeNode | None,
        target: int,
    ) -> bool:
        """Return if a target value can be created from two nodes in different trees.

        The given roots are root nodes to a Binary Search Tree.

        Args:
            root1 (TreeNode | None): first BST to traverse
            root2 (TreeNode | None): second BST to traverse
            target (int): value to try and sum up to

        Returns:
            bool: True if such a pair exists, otherwise False
        """

        def search_tree(node: TreeNode | None, remainder: int) -> bool:
            if not node:
                return False
            if node.val == remainder:
                return True
            if node.val > remainder:
                return search_tree(node.left, remainder)
            return search_tree(node.right, remainder)

        def dfs(curr_node: TreeNode | None) -> bool:
            if not curr_node:
                return False
            if search_tree(root2, target - curr_node.val):
                return True
            return dfs(curr_node.left) or dfs(curr_node.right)

        return dfs(root1)

    def twoSumBSTsList(
        self,
        root1: TreeNode | None,
        root2: TreeNode | None,
        target: int,
    ) -> bool:
        """Return same as above using in-order traversal for lists."""

        def dfs(node: TreeNode | None, node_list: list[int]) -> None:
            if not node:
                return
            dfs(node.left, node_list)
            node_list.append(node.val)
            dfs(node.right, node_list)

        node1_list, node2_list = [], []
        dfs(root1, node1_list)
        dfs(root2, node2_list)
        n1_len, n2_len = len(node1_list), len(node2_list)
        idx_n1, idx_n2 = 0, n2_len - 1
        while idx_n1 < n1_len and idx_n2 >= 0:
            test_sum = node1_list[idx_n1] + node2_list[idx_n2]
            if test_sum == target:
                return True
            if test_sum < target:
                idx_n1 += 1
            else:
                idx_n2 -= 1
        return False

    def twoSumBSTsSet(
        self,
        root1: TreeNode | None,
        root2: TreeNode | None,
        target: int,
    ) -> bool:
        """Return same as above using a set of the possible values."""

        def dfs(node: TreeNode | None, node_set: set[int]) -> None:
            if not node:
                return
            dfs(node.left, node_set)
            node_set.add(node.val)
            dfs(node.right, node_set)

        node1_set, node2_set = set(), set()
        dfs(root1, node1_set)
        dfs(root2, node2_set)
        return any(target - val in node2_set for val in node1_set)


def main() -> None:
    """1214. Two Sum BSTs on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = build_tree([2,1,4]), build_tree([1,0,3]), 5
        >>> example_case_2 = build_tree([0,-10,10]), build_tree([5,1,7,0,2]), 18

    Example 1:
        >>> sol.twoSumBSTs(*example_case_1)
        True
        >>> sol.twoSumBSTsList(*example_case_1)
        True
        >>> sol.twoSumBSTsSet(*example_case_1)
        True

    Example 2:
        >>> sol.twoSumBSTs(*example_case_2)
        False
        >>> sol.twoSumBSTsList(*example_case_2)
        False
        >>> sol.twoSumBSTsSet(*example_case_2)
        False
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
