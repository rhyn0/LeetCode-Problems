"""Daily Challenge on LeetCode for October 17: Problem #1361 [Medium]."""
# Standard Library
from collections import deque
import doctest


class UnionFind:
    """Object to handle the logic of doing UnionFind on a graph."""

    def __init__(self, n: int) -> None:
        """Initialize the UnionFind graph."""
        self.num_components = n
        # every node is its own parent until we union them
        self.parent = list(range(n))

    def find(self, node: int) -> int:
        """Find the parent of the given node."""
        if node == self.parent[node]:
            return node
        # path compression for optimization
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, parent: int, child: int) -> bool:
        """Union the two components, returning whether a Union was done or not."""
        parent1 = self.find(parent)
        parent2 = self.find(child)
        if child != parent2 or parent1 == parent2:
            return False
        self.parent[parent2] = parent1
        self.num_components -= 1
        return True


class Solution:  # noqa: D101
    def validateBinaryTreeNodes(
        self,
        n: int,
        left_child: list[int],
        right_child: list[int],
    ) -> bool:
        """Return whether a given binary tree is valid.

        Binary tree is displayed as a list of child nodes on each side of the ith node.

        Args:
            n (int): Number of nodes
            left_child (list[int]): Left child of the ith node, -1 if None
            right_child (list[int]): right child of the ith node, -1 if None

        Returns:
            bool: True if the binary tree is valid, False otherwise
        """
        if n == 1:
            return True
        # this value strictly applies to my union array to show that we haven't
        # touched this node yet
        parent = list(range(n))

        def find_parent(node: int) -> int:
            # Find the parent of the known component
            if node == parent[node]:
                return node
            return find_parent(parent[node])

        def union(node1: int, node2: int) -> bool:
            # Union the two components, making node1 the parent
            parent1 = find_parent(node1)
            parent2 = find_parent(node2)
            if parent1 == parent2:
                return False
            parent[node2] = parent1
            return True

        for i, (left, right) in enumerate(zip(left_child, right_child, strict=True)):
            # on first touch, set a node's parent to itself
            # if this value is already initialized, then it does nothing
            if left != -1 and not union(i, left):
                return False
            if right != -1 and not union(i, right):
                return False
        return len(set(map(find_parent, parent))) == 1

    def validateBinaryTreeNodesUFOop(
        self,
        n: int,
        left_child: list[int],
        right_child: list[int],
    ) -> bool:
        """Return same as above using UnionFind class."""
        uf = UnionFind(n)
        for i, (left, right) in enumerate(zip(left_child, right_child, strict=True)):
            if left != -1 and not uf.union(i, left):
                return False
            if right != -1 and not uf.union(i, right):
                return False

        return uf.num_components == 1

    def validateBinaryTreeNodesDFS(
        self,
        n: int,
        left_child: list[int],
        right_child: list[int],
    ) -> bool:
        """Return same as above using Depth First Search."""

        def find_root() -> int:
            # return root node based on nodes that are never children
            children = set(left_child) | set(right_child)
            if len(set(range(n)).difference(children)) > 1:
                # if more than one node is missing, then its multiple disjoint sets
                return -1
            for node in range(n):
                if node not in children:
                    return node
            return -1

        root_num = find_root()
        if root_num == -1:
            return False

        seen = {root_num}
        # use stack to do DFS, go all the way right then left
        stack = [root_num]
        while stack:
            node = stack.pop()
            for child in (left_child[node], right_child[node]):
                if child == -1:
                    continue
                if child in seen:
                    return False
                seen.add(child)
                stack.append(child)
        # make sure we visit all nodes
        return len(seen) == n

    def validateBinaryTreeNodesBFS(
        self,
        n: int,
        left_child: list[int],
        right_child: list[int],
    ) -> bool:
        """Return same as above using BFS."""

        def find_root() -> int:
            # return root node based on nodes that are never children
            children = set(left_child) | set(right_child)
            if len(set(range(n)).difference(children)) > 1:
                # if more than one node is missing, then its multiple disjoint sets
                return -1
            for node in range(n):
                if node not in children:
                    return node
            return -1

        root_num = find_root()
        if root_num == -1:
            return False

        seen = {root_num}
        # use queue to do BFS, go level by level from root
        stack = deque([root_num])
        while stack:
            node = stack.popleft()
            for child in (left_child[node], right_child[node]):
                if child == -1:
                    continue
                if child in seen:
                    return False
                seen.add(child)
                stack.append(child)
        # make sure we visit all nodes
        return len(seen) == n


def main() -> None:
    """1361. Validate Binary Tree Nodes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = (4, [1,-1,3,-1],[2,-1,-1,-1])
        >>> example_case_2 = (4, [1,-1,3,-1], [2,3,-1,-1])
        >>> example_case_3 = (2, [1,0], [-1,-1])
        >>> test_case_1 = (4, [1,0,3,-1], [-1,-1,-1,-1])
        >>> test_case_2 = (3, [-1,2,-1], [-1,-1,-1])

    Example 1:
        >>> sol.validateBinaryTreeNodes(*example_case_1)
        True
        >>> sol.validateBinaryTreeNodesUFOop(*example_case_1)
        True
        >>> sol.validateBinaryTreeNodesDFS(*example_case_1)
        True
        >>> sol.validateBinaryTreeNodesBFS(*example_case_1)
        True

    Example 2:
        >>> sol.validateBinaryTreeNodes(*example_case_2)
        False
        >>> sol.validateBinaryTreeNodesUFOop(*example_case_2)
        False
        >>> sol.validateBinaryTreeNodesDFS(*example_case_2)
        False
        >>> sol.validateBinaryTreeNodesBFS(*example_case_2)
        False

    Example 3:
        >>> sol.validateBinaryTreeNodes(*example_case_3)
        False
        >>> sol.validateBinaryTreeNodesUFOop(*example_case_3)
        False
        >>> sol.validateBinaryTreeNodesDFS(*example_case_3)
        False
        >>> sol.validateBinaryTreeNodesBFS(*example_case_3)
        False

    Test 1:
        >>> sol.validateBinaryTreeNodes(*test_case_1)
        False
        >>> sol.validateBinaryTreeNodesUFOop(*test_case_1)
        False
        >>> sol.validateBinaryTreeNodesDFS(*test_case_1)
        False
        >>> sol.validateBinaryTreeNodesBFS(*test_case_1)
        False

    Test 2:
        >>> sol.validateBinaryTreeNodes(*test_case_2)
        False
        >>> sol.validateBinaryTreeNodesUFOop(*test_case_2)
        False
        >>> sol.validateBinaryTreeNodesDFS(*test_case_2)
        False
        >>> sol.validateBinaryTreeNodesBFS(*test_case_2)
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
