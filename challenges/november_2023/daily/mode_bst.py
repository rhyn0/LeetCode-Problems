"""Daily Challenge for November 1 on LeetCode: Problem #501 [Easy]."""
# Standard Library
from collections import Counter
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
    def findMode(self, root: TreeNode | None) -> list[int]:
        """Return the mode of a binary search tree.

        Values are allowed to be duplicated in this BST.
        So values to left are less than or equal to parent
        and values to right are greater than or equal to parent.

        Each subtree is a valid BST.
        """
        # BFS approach
        if root is None:
            return []
        que = deque([root])
        seen_values = Counter()
        while que:
            node = que.popleft()
            seen_values[node.val] += 1
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        mode = max(seen_values.values())
        return [k for k, v in seen_values.items() if v == mode]

    def findModeDFS(self, root: TreeNode | None) -> list[int]:
        """Return same as above using DFS recursive approach."""
        if root is None:
            return []
        seen_values = Counter()

        def dfs(node: TreeNode) -> None:
            seen_values[node.val] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        mode = max(seen_values.values())
        return [k for k, v in seen_values.items() if v == mode]

    def findModeDFSSpace(self, root: TreeNode | None) -> list[int]:
        """Return same as above using DFS recursively with constant space.

        This is constant space given the context of the problem, which says to
        ignore the space required by the recursive call stack.
        """
        curr_streak = max_streak = 0
        curr_num = 0
        modes = []

        def dfs(node: TreeNode | None) -> None:
            nonlocal curr_streak, max_streak, curr_num, modes
            if node is None:
                return

            # inorder traversal
            dfs(node.left)

            # check if current node extends sreak
            if curr_num == node.val:
                curr_streak += 1
            # new number, reset streak
            else:
                curr_streak = 1
                curr_num = node.val

            if curr_streak > max_streak:
                # new max streak
                max_streak = curr_streak
                modes = []
            # does current streak match max streak
            if curr_streak == max_streak:
                modes.append(curr_num)

            # visit right subtree
            dfs(node.right)

        if root is None:
            return []
        dfs(root)
        return modes

    def findModeMorris(self, root: TreeNode | None) -> list[int]:
        """Return same as above using Morris Traversal.

        This is true constant space as there is no recursion.
        This algorithm will not modify the tree after call completion.
        """
        if root is None:
            return []

        curr_streak = max_streak = 0
        curr_num = 0
        modes = []

        def update_counts(val: int) -> None:
            """Helper function to do the streak updates."""
            nonlocal curr_streak, max_streak, curr_num, modes
            # check if current node extends sreak
            if curr_num == val:
                curr_streak += 1
            # new number, reset streak
            else:
                curr_streak = 1
                curr_num = val

            if curr_streak > max_streak:
                # new max streak
                max_streak = curr_streak
                modes = []
            # does current streak match max streak
            if curr_streak == max_streak:
                modes.append(curr_num)

        current = root
        while current:
            if current.left is None:
                # examine current data
                update_counts(current.val)
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right
                if pre.right is None:
                    # link this right-most leaf to grandparent
                    pre.right = current
                    current = current.left
                else:
                    # this right most node of left subtree already
                    # linked to grandparent, so we can examine current.val
                    # and undo the link
                    update_counts(current.val)
                    pre.right = None
                    current = current.right
        return modes


def main() -> None:
    """501. Find Mode in Binary Search Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,None,2,2]
        >>> example_case_2 = [0]

    Example 1:
        >>> sol.findMode(build_tree(example_case_1))
        [2]
        >>> sol.findModeDFS(build_tree(example_case_1))
        [2]
        >>> sol.findModeDFSSpace(build_tree(example_case_1))
        [2]
        >>> sol.findModeMorris(build_tree(example_case_1))
        [2]

    Example 2:
        >>> sol.findMode(build_tree(example_case_2))
        [0]
        >>> sol.findModeDFS(build_tree(example_case_2))
        [0]
        >>> sol.findModeDFSSpace(build_tree(example_case_2))
        [0]
        >>> sol.findModeMorris(build_tree(example_case_2))
        [0]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
