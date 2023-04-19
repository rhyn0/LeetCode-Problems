"""Daily Challenge from April 18, 2023."""
# Standard Library
import doctest
from functools import cache


class TreeNode:  # noqa: D101
    def __init__(self, val=0, left=None, right=None):  # noqa: D107
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Debugging method."""
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class InvalidBinaryTreeError(Exception):
    """Exception for an improperly defined binary tree."""

    def __init__(self, *args: object) -> None:
        """Default message and pass through args."""
        super().__init__("Invalid definition", *args)


def build_tree(node_list: list[int | None]) -> TreeNode:
    """Return binary tree made of TreeNode from inorder array."""
    if not node_list or node_list[0] is None:
        raise InvalidBinaryTreeError()

    tree_node_que = []
    input_queue = node_list[1:]

    # for i in range(1, len(node_list)):
    #     integerQueue.append(node_list[i])

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
    def longestZigZag(self, root: TreeNode | None) -> int:
        """Return length of longest zig zag path in given binary tree.

        A zigzag path is built of alternating left-right paths
        from parent node to child node.

        Args:
            root (TreeNode | None): Valid binary tree

        Returns:
            int: Length of longest zigzag path
        """
        longest_path = 0

        def dfs(node: TreeNode | None, go_left: bool, curr_path: int) -> None:
            if node is None:
                return
            nonlocal longest_path
            longest_path = max(longest_path, curr_path)
            dfs(node.left, False, (curr_path + 1) if go_left else 1)
            dfs(node.right, True, (curr_path + 1) if not go_left else 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return longest_path

    def longestZigZagDP(self, root: TreeNode | None) -> int:
        """Return same as above using memoization."""
        longest_path = 0
        memo = {}

        def recurse_tree(node: TreeNode | None) -> None:
            nonlocal longest_path, memo
            if node is None:
                return
            if node.left is None and node.right is None:
                memo[node] = [0, 0]
                return
            recurse_tree(node.left)
            recurse_tree(node.right)

            left = memo.get(node.left, [-1, -1])[1] + 1
            right = memo.get(node.right, [-1, -1])[0] + 1
            memo[node] = [left, right]
            longest_path = max(longest_path, left, right)

        recurse_tree(root)
        return longest_path

    def longestZigZagDPBuilt(self, root: TreeNode | None) -> int:
        """Return same as above using builtin caching methods."""
        longest_path = 0

        @cache
        def recurse_tree(node: TreeNode | None) -> list[int]:
            nonlocal longest_path
            if node is None:
                return [-1, -1]
            if node.left is None and node.right is None:
                return [0, 0]
            left = recurse_tree(node.left)[1] + 1
            right = recurse_tree(node.right)[0] + 1

            longest_path = max(longest_path, left, right)
            return [left, right]

        recurse_tree(root)
        return longest_path


def main():
    """Longest ZigZag Path in a Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = build_tree([1,None,2,3,4,None,None,5,6,None,7,\
            None,None,None,8,None,9])
        >>> example_case_2 = build_tree([1,1,1,None,1,None,None,1,1,None,1])
        >>> example_case_3 = build_tree([1])
        >>> test_case_1 = build_tree([1, None, 1, None, 1])

    Example 1:
        >>> sol.longestZigZag(example_case_1)
        3
        >>> sol.longestZigZagDP(example_case_1)
        3
        >>> sol.longestZigZagDPBuilt(example_case_1)
        3

    Example 2:
        >>> sol.longestZigZag(example_case_2)
        4
        >>> sol.longestZigZagDP(example_case_2)
        4
        >>> sol.longestZigZagDPBuilt(example_case_2)
        4

    Example 3:
        >>> sol.longestZigZag(example_case_3)
        0
        >>> sol.longestZigZagDP(example_case_3)
        0
        >>> sol.longestZigZagDPBuilt(example_case_3)
        0

    Test 1:
        >>> sol.longestZigZag(test_case_1)
        1
        >>> sol.longestZigZagDP(test_case_1)
        1
        >>> sol.longestZigZagDPBuilt(test_case_1)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        # ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
