"""Meta Interview Question Practice List on LeetCode.

Previously solved - see `study_plans/leet_75/k_smallest_bst/kth_small_element_bst.py`

230. Kth Smallest Element in a BST on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = build_tree([3,1,4,None,2]), 1
    >>> example_case_2 = build_tree([5,3,6,2,4,None,None,1]), 3

Example 1:
    >>> sol.kthSmallest(*example_case_1)
    1
    >>> sol.kthSmallestBFS(*example_case_1)
    1
    >>> sol.kthSmallestDFS(*example_case_1)
    1

Example 2:
    >>> sol.kthSmallest(*example_case_2)
    3
    >>> sol.kthSmallestBFS(*example_case_2)
    3
    >>> sol.kthSmallestDFS(*example_case_2)
    3
"""

# Standard Library
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
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """Given the root of a BST, return the kth (1 index) smallest element.

        Args:
            root (TreeNode | None): Root of BST if any
            k (int): kth smallest element to return

        Returns:
            int: kth Smallest element value if exists, else -1
        """
        current = root
        # try to preserve input tree, so we save our results here
        smallest_val = -1
        # number of elements from smallest
        count = 0
        while current:
            # keep track of our the next state before we jump
            if current.left is None:
                # we reached the farthest left node possible at this time
                count += 1
                if count == k:
                    smallest_val = current.val
                current = current.right
            else:
                # from the left subtree
                child = current.left
                # run as far right as possible
                while child.right and child.right is not current:
                    child = child.right
                if child.right is None:
                    # link this far right child to its grand* parent
                    # which allows our to jump levels to its ancestors
                    child.right = current
                    current = current.left
                else:
                    # child has a link to its grandparent
                    # which means we have found a minimum element again
                    # but in the right subtree of a subtree
                    count += 1
                    if count == k:
                        smallest_val = current.val
                    # undo ancestor links
                    child.right = None
                    current = current.right

        return smallest_val

    def kthSmallestBFS(self, root: TreeNode | None, k: int) -> int:
        """Return same as above using BFS methodology."""
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallestDFS(self, root: TreeNode | None, k: int) -> int:
        """Return same as above using DFS methodology."""

        # use DFS to build the inorder array of the tree
        def dfs_array(node: TreeNode | None) -> list[int]:
            return (
                ([*dfs_array(node.left), node.val, *dfs_array(node.right)])
                if node
                else []
            )

        # convert 1 indexed number to 0 index
        return dfs_array(root)[k - 1]
