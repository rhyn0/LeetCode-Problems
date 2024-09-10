"""Weekly Challenge on LeetCode: Problem #1660 [Medium]."""

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
        return (
            f"TreeNode({self.val}, "
            f"{self.left.val if self.left else None}, "
            f"{self.right.val if self.right else None})"
        )


class InvalidBinaryTreeError(Exception):
    """Exception for an improperly defined binary tree."""

    def __init__(self, nodes: list, *args: object) -> None:
        """Default message and pass though args."""
        super().__init__(f"Invalid definition: ({','.join(nodes)})", *args)


def build_tree(node_list: list[int | None], from_node: int, to_node: int) -> TreeNode:
    """Return binary tree made of TreeNode from inorder array."""
    if not node_list or node_list[0] is None:
        raise InvalidBinaryTreeError(node_list)
    tree_node_que = []
    input_queue = node_list[1:]
    root_node = TreeNode(node_list[0])
    tree_node_map = {node_list[0]: root_node}
    tree_node_que.append(root_node)
    while input_queue:
        left_input = input_queue.pop(0) if input_queue else None
        right_input = input_queue.pop(0) if input_queue else None
        current = tree_node_que.pop(0)
        if left_input is not None:
            left = TreeNode(left_input)
            tree_node_map[left_input] = left
            current.left = left
            tree_node_que.append(left)
        if right_input is not None:
            right = TreeNode(right_input)
            tree_node_map[right_input] = right
            current.right = right
            tree_node_que.append(right)

    # custom to this problem, mangle one connection
    tree_node_map[from_node].right = tree_node_map[to_node]

    return root_node


def deconstruct_tree(root: TreeNode | None) -> list[int | None]:
    """Return inorder array from binary tree made of TreeNode."""
    if root is None:
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
        tree_node_que.append(current.left)
        tree_node_que.append(current.right)
    # trim trailing None
    while output_queue and output_queue[-1] is None:
        output_queue.pop()
    return output_queue


class Solution:  # noqa: D101
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        """Given a binary tree root, fix it so that there is no invalid link."""
        # store node, parent
        que: deque[tuple[TreeNode, TreeNode | None]] = deque([(root, None)])
        # store child node value -> (parent_node, isLeft)
        seen_nodes = {}
        linked_node = None
        while que:
            node, parent = que.popleft()
            if node.val in seen_nodes:
                linked_node = node.val
                seen_nodes[node.val] = (
                    parent,
                    parent.left == node if parent else False,
                )
                break
            seen_nodes[node.val] = (parent, parent.left == node if parent else False)
            if node.left:
                que.append((node.left, node))
            if node.right:
                que.append((node.right, node))
        if linked_node is None:
            msg = "No offending node found."
            raise ValueError(msg)

        offending_node, _ = seen_nodes[linked_node]
        parent_node, is_left = seen_nodes[offending_node.val]  # type: ignore[union-attr]
        if is_left:
            parent_node.left = None  # type: ignore[union-attr]
        else:
            parent_node.right = None  # type: ignore[union-attr]
        return root

    def correctBinaryTreeLevelImprov(self, root: TreeNode) -> TreeNode:
        """Same as above but use a smaller visited object."""
        queue: deque[tuple[TreeNode, TreeNode | None]] = deque([(root, None)])
        while queue:
            level_len = len(queue)
            visited = set()
            for _ in range(level_len):
                node, parent = queue.popleft()
                if node.right in visited:
                    if parent is None:
                        raise InvalidBinaryTreeError(list(visited))
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root
                visited.add(node)
                if node.right:
                    queue.append((node.right, node))
                if node.left:
                    queue.append((node.left, node))

        # this is an error state
        msg = "No offending node found."
        raise ValueError(msg)

    def correctBinaryTreeDFS(self, root: TreeNode) -> TreeNode:
        """Return same as above using DFS."""
        visited = set()

        def build_correct_tree(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return None

            if node.right and node.right in visited:
                # found the bad node, remove it and its children
                return None

            visited.add(node)
            node.right = build_correct_tree(node.right)
            node.left = build_correct_tree(node.left)
            return node

        new_root = build_correct_tree(root)
        if new_root is None:
            msg = "No offending node found."
            raise ValueError(msg)

        return new_root


def main() -> None:
    """1660. Correct a Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([1,2,3],2,3)
        >>> example_case_2 = ([8,3,1,7,None,9,4,2,None,None,None,5,6],7,4)

    Example 1:
        >>> deconstruct_tree(sol.correctBinaryTree(build_tree(*example_case_1)))
        [1, None, 3]
        >>> deconstruct_tree(\
            sol.correctBinaryTreeLevelImprov(build_tree(*example_case_1)))
        [1, None, 3]

    Example 2:
        >>> deconstruct_tree(sol.correctBinaryTree(build_tree(*example_case_2)))
        [8, 3, 1, None, None, 9, 4, None, None, 5, 6]
        >>> deconstruct_tree(\
            sol.correctBinaryTreeLevelImprov(build_tree(*example_case_2)))
        [8, 3, 1, None, None, 9, 4, None, None, 5, 6]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
