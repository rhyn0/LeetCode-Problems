"""Daily Challenge from April 18, 2023."""
import doctest
from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def build_tree(data):
    if data == None or len(data) == 0:
        return None

    treeNodeQueue = []
    integerQueue = []

    for i in range(1, len(data)):
        integerQueue.append(data[i])

    treeNode = TreeNode(data[0])
    treeNodeQueue.append(treeNode)

    while integerQueue:
        leftVal = integerQueue.pop(0) if integerQueue else None
        rightVal = integerQueue.pop(0) if integerQueue else None

        current = treeNodeQueue.pop(0)

        if leftVal is not None:
            left = TreeNode(leftVal)
            current.left = left
            treeNodeQueue.append(left)
        if rightVal is not None:
            right = TreeNode(rightVal)
            current.right = right
            treeNodeQueue.append(right)

    return treeNode


class Solution:  # noqa: D101
    def longestZigZag(self, root: TreeNode | None) -> int:
        @cache
        def dfs(node: TreeNode | None) -> list[int]:
            if node is None:
                return [-1, -1]

            left = dfs(node.left)
            left[1] += 1

            right = dfs(node.right)
            right[0] += 1

            print(f"Returning max of {left} and max of {right} at {node.val}")

            return [max(left), max(right)]

        return max(dfs(root))


def main():
    """Longest ZigZag Path in a Binary Tree on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = build_tree([1,None,2,3,4,None,None,5,6,None,7,None,None,None,8,None,9])
        >>> example_case_2 = build_tree([1,1,1,None,1,None,None,1,1,None,1])
        >>> example_case_3 = build_tree([1])

    Example 1:
        >>> sol.longestZigZag(example_case_1)
        3

    Example 2:
        >>> sol.longestZigZag(example_case_2)
        4

    Example 3:
        >>> sol.longestZigZag(example_case_3)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        # ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
