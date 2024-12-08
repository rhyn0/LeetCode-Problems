"""Meta Interview Question Practice List on LeetCode.

314. Binary Tree Vertical Order Traversal on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = build_tree([3,9,20,None,None,15,7])
    >>> example_case_2 = build_tree([3,9,8,4,0,1,7])
    >>> example_case_3 = build_tree([1,2,3,4,10,9,11,None,5,None,None,None,None,None,None,None,6])

Example 1:
    >>> sol.verticalOrder(example_case_1)
    [[9], [3, 15], [20], [7]]
    >>> sol.verticalOrderNoSort(example_case_1)
    [[9], [3, 15], [20], [7]]
    >>> sol.verticalOrderDfs(example_case_1)
    [[9], [3, 15], [20], [7]]

Example 2:
    >>> sol.verticalOrder(example_case_2)
    [[4], [9], [3, 0, 1], [8], [7]]
    >>> sol.verticalOrderNoSort(example_case_2)
    [[4], [9], [3, 0, 1], [8], [7]]
    >>> sol.verticalOrderDfs(example_case_2)
    [[4], [9], [3, 0, 1], [8], [7]]

Example 3:
    >>> sol.verticalOrder(example_case_3)
    [[4], [2, 5], [1, 10, 9, 6], [3], [11]]
    >>> sol.verticalOrderNoSort(example_case_3)
    [[4], [2, 5], [1, 10, 9, 6], [3], [11]]
    >>> sol.verticalOrderDfs(example_case_3)
    [[4], [2, 5], [1, 10, 9, 6], [3], [11]]
"""  # noqa: E501

# Standard Library
from collections import defaultdict
from collections import deque
import operator
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
    def verticalOrder(self, root: TreeNode | None) -> list[list[int]]:
        """Return the vertical column order traversal of a binary tree.

        If two nodes are in the same row and column,
        the order should be from left to right.

        Args:
            root (TreeNode | None): Root node of the tree, if any

        Returns:
            list[list[int]]: Left to right column order of each column
        """
        if not root:
            return []

        que: deque[tuple[TreeNode, int]] = deque()
        que.append((root, 0))
        # mark the column of root as 0, -1 for going left, +1 for going right
        # will have to sort by keys on the output.
        column_mapping: dict[int, list[int]] = defaultdict(list)
        while que:
            (curr_node, column_num) = que.popleft()
            column_mapping[column_num].append(curr_node.val)
            # make sure to enqueue next nodes from left to right
            # don't enqueue None
            if curr_node.left:
                que.append((curr_node.left, column_num - 1))
            if curr_node.right:
                que.append((curr_node.right, column_num + 1))
        # sort items by column number (which is unique), only output list
        return [v for _, v in sorted(column_mapping.items())]

    def verticalOrderNoSort(self, root: TreeNode | None) -> list[list[int]]:
        """Return same as above without sorting at end."""
        if not root:
            return []

        min_column_val = max_column_val = 0
        que: deque[tuple[TreeNode, int]] = deque()
        que.append((root, 0))
        # mark the column of root as 0, -1 for going left, +1 for going right
        # will have to sort by keys on the output.
        column_mapping: dict[int, list[int]] = defaultdict(list)
        while que:
            (curr_node, column_num) = que.popleft()
            min_column_val = min(min_column_val, column_num)
            max_column_val = max(max_column_val, column_num)
            column_mapping[column_num].append(curr_node.val)
            # make sure to enqueue next nodes from left to right
            # don't enqueue None
            if curr_node.left:
                que.append((curr_node.left, column_num - 1))
            if curr_node.right:
                que.append((curr_node.right, column_num + 1))
        # sort items by column number (which is unique), only output list
        return [column_mapping[k] for k in range(min_column_val, max_column_val + 1)]

    def verticalOrderDfs(self, root: TreeNode | None) -> list[list[int]]:
        """Return same as above using DFS."""
        if not root:
            return []

        min_column_val = max_column_val = 0
        # mark the column of root as 0, -1 for going left, +1 for going right
        column_mapping: dict[int, list[int]] = defaultdict(list)

        def dfs(curr_node: TreeNode | None, row: int, column: int) -> None:
            nonlocal min_column_val, max_column_val
            if not curr_node:
                return
            # have to keep track of row, to make sure the vertical column ordering
            column_mapping[column].append((row, curr_node.val))
            min_column_val = min(min_column_val, column)
            max_column_val = max(max_column_val, column)

            # iterate to next depth, left to right is important for row/col ties
            dfs(curr_node.left, row + 1, column - 1)
            dfs(curr_node.right, row + 1, column + 1)

        dfs(root, 0, 0)

        # output has to be in column order, left to right
        # but for each column list, we need to sort that by the row it ocurred in
        # Python sorts tuples by sorting of first element, ties decided by next element
        # we have to override that behavior, for ties we don't want to change positions
        return [
            [val for _, val in sorted(column_mapping[col], key=operator.itemgetter(0))]
            for col in range(min_column_val, max_column_val + 1)
        ]
