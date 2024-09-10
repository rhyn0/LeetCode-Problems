"""Problem 98. Validate Binary Search Tree on LeetCode."""

# Standard Library
import doctest
import math
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


def build_tree(node_list: list[int | None]) -> TreeNode:
    """Return binary tree made of TreeNode from inorder array."""
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
    # these numbers are outside the range of the problem
    MIN_NODE_VAL = -(2**32)
    MAX_NODE_VAL = 2**32 - 1

    def isValidBST(self, root: TreeNode | None) -> bool:  # noqa: D102
        if root is None:
            return True
        stack: list[tuple[TreeNode | None, int, int]] = [
            (root, self.MIN_NODE_VAL, self.MAX_NODE_VAL),
        ]
        while stack:
            # dfs approach
            node, lower_bound, upper_bound = stack.pop()
            # handle that we added a None
            if node is None:
                continue
            if node.val <= lower_bound or node.val >= upper_bound:
                # child value is greater surpasses the parent/grandparent value
                # in the opposite direction of grandparent child
                # so if we are in left subtree of a grandparent, lower_bound is infinite
                # but we can't go greater than grandparent node val
                return False
            stack.append((node.right, node.val, upper_bound))
            stack.append((node.left, lower_bound, node.val))

        return True

    def isValidBSTTraverse(self, root: TreeNode | None) -> bool:
        """Return same as above without using range bounds as extra space."""
        # store a stack of the nodes we passed but didn't check
        stack: list[TreeNode] = []
        prev = -math.inf
        while stack or root:
            # traverse left subtree
            while root:
                stack.append(root)
                root = root.left
            # check current node
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            # traverse right subtree
            root = root.right
        return True


def main() -> None:
    """98. Validate Binary Search Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = build_tree([2,1,3])
        >>> example_case_2 = build_tree([5,1,4,None,None,3,6])

    Example 1:
        >>> sol.isValidBST(example_case_1)
        True
        >>> sol.isValidBSTTraverse(example_case_1)
        True

    Example 2:
        >>> sol.isValidBST(example_case_2)
        False
        >>> sol.isValidBSTTraverse(example_case_2)
        False
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
