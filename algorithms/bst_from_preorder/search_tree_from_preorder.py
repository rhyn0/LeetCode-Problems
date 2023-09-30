"""Construct a binary search tree from a preorder traversal of the same tree."""
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
    # trim None from the end
    while output_queue and output_queue[-1] is None:
        output_queue.pop()
    return output_queue


class Solution:  # noqa: D101
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:  # noqa: D102
        # handle empty list
        if not preorder:
            return None
        # monotonic stack, stores ndoes in decreasing value - going left
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            # peek and grab parent node
            poss_parent, child = stack[-1], TreeNode(val)
            # if child is greater than parent, we are going up the tree and need to pop
            while stack and stack[-1].val < val:
                # every node in list is already linked to a parent, so we can discard
                poss_parent = stack.pop()
            # reached the most likely parent of child, link them
            if poss_parent.val < val:
                poss_parent.right = child
            else:
                poss_parent.left = child
            # push child onto stack
            stack.append(child)
        return root

    def bstFromPreorderInorder(self, preorder: list[int]) -> TreeNode | None:
        """Convert preorder to inorder then do comparison to create BST."""
        inorder = sorted(preorder)
        current_pre_idx = 0
        val_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_len = len(preorder)

        def inorder_helper(
            left: int = 0,
            right: int = preorder_len,
        ) -> TreeNode | None:
            # given left and right idx, recurse to build the subtree of the current node
            nonlocal current_pre_idx, val_map
            if left == right:
                return None

            # root splits the bounds into left and right
            root = TreeNode(preorder[current_pre_idx])
            current_pre_idx += 1
            root_inorder_idx = val_map[root.val]

            root.left = inorder_helper(left, root_inorder_idx)
            root.right = inorder_helper(root_inorder_idx + 1, right)
            return root

        return inorder_helper()


def main() -> None:
    """1008. Construct Binary Search Tree from Preorder Traversal on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [8,5,1,7,10,12]
        >>> example_case_2 = [1,3]
        >>> example_case_3 = [4, 2]
        >>> test_case_1 = [1, 3, 2]
        >>> test_case_2 = [7,20,19,12]

    Example 1:
        >>> deconstruct_tree(sol.bstFromPreorder(example_case_1))
        [8, 5, 10, 1, 7, None, 12]
        >>> deconstruct_tree(sol.bstFromPreorderInorder(example_case_1))
        [8, 5, 10, 1, 7, None, 12]

    Example 2:
        >>> deconstruct_tree(sol.bstFromPreorder(example_case_2))
        [1, None, 3]
        >>> deconstruct_tree(sol.bstFromPreorderInorder(example_case_2))
        [1, None, 3]

    Example 3:
        >>> deconstruct_tree(sol.bstFromPreorder(example_case_3))
        [4, 2]
        >>> deconstruct_tree(sol.bstFromPreorderInorder(example_case_3))
        [4, 2]

    Test 1:
        >>> deconstruct_tree(sol.bstFromPreorder(test_case_1))
        [1, None, 3, 2]
        >>> deconstruct_tree(sol.bstFromPreorderInorder(test_case_1))
        [1, None, 3, 2]

    Test 2:
        >>> deconstruct_tree(sol.bstFromPreorder(test_case_2))
        [7, None, 20, 19, None, 12]
        >>> deconstruct_tree(sol.bstFromPreorderInorder(test_case_2))
        [7, None, 20, 19, None, 12]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
