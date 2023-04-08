"""LeetCode Daily Challenge for April 8, 2023."""
from __future__ import annotations

# Standard Library
from collections import deque
import doctest
from typing import Any


class Node:  # noqa: D101
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None) -> None:
        """Initialize node.

        Args:
            val (int, optional): index of node. Defaults to 0.
            neighbors (list[Node] | None, optional): Adjacent neighbors list.
                Defaults to None.
        """
        self.val = val
        self.neighbors = neighbors if neighbors else []

    def __repr__(self) -> str:  # noqa: D105
        return f"Node({self.val}, num_neighbors={[n.val for n in self.neighbors]})"

    def __lt__(self, other: Any) -> bool:
        """Make sorting easy for testing."""
        if not isinstance(other, Node):
            return NotImplemented
        return self.val < other.val

    def __eq__(self, other: Any) -> bool:
        """Make comparisons easy for testing."""
        if not isinstance(other, Node):
            return NotImplemented
        return self.val == other.val and self is not other


def is_cloned_graph(n1: Node, n2: Node) -> bool:
    """Return whether n1 is a cloned version of n2 or visa versa."""
    seen_nodes: set[int] = set()

    def dfs_compare(node1: Node, node2: Node) -> bool:
        if node1 != node2:
            return False
        seen_nodes.add(node1.val)
        for child1, child2 in zip(
            sorted(node1.neighbors), sorted(node2.neighbors), strict=True
        ):
            if child1.val in seen_nodes or child2.val in seen_nodes:
                continue
            if not dfs_compare(child1, child2):
                return False

        return True

    try:
        return dfs_compare(n1, n2)
    except ValueError:
        # strict zip
        return False


class Solution:  # noqa: D101
    @classmethod
    def build_new_nodes(cls, adjacency: dict[int, set[int]]) -> list[Node]:
        """Return new Nodes as a list."""
        new_nodes = [Node(i) for i in range(1, len(adjacency) + 1)]
        for node_num, adj_set in adjacency.items():
            new_nodes[node_num - 1].neighbors = [new_nodes[i - 1] for i in adj_set]

        return new_nodes

    def cloneGraph(self, node: Node | None) -> Node | None:
        """Return a deep copy of the graph given a single node of the graph.

        Uses DFS to search the whole graph, build the adjacency list
        and then reconstruct the graph.

        Args:
            node (Node | None): Starter node. If None, means the graph is empty

        Returns:
            Node | None: New cloned graph, None means graph is empty.
        """
        # empty graph
        if not node:
            return None
        adj_dict: dict[int, set[int]] = {}

        def dfs(n1: Node) -> None:
            if n1.val in adj_dict:
                return
            # init node
            adj_dict[n1.val] = set()
            # add neighbors if there are any
            for neigh_node in n1.neighbors:
                adj_dict[n1.val].add(neigh_node.val)
                dfs(neigh_node)

        # build adjacency list
        dfs(node)
        # create new nodes
        new_nodes = self.build_new_nodes(adj_dict)

        # always given Node 1 to start
        return new_nodes[0]

    def cloneGraphBFS(self, node: Node | None) -> Node | None:
        """Return same as above but using BFS."""
        if not node:
            return None

        adj_dict: dict[int, set[int]] = {}

        def bfs(n1: Node) -> None:
            que: deque[Node] = deque()
            que.append(n1)
            while que:
                curr_node = que.popleft()
                adj_dict[curr_node.val] = {n.val for n in curr_node.neighbors}

                que.extend(
                    [
                        neighbor_node
                        for neighbor_node in curr_node.neighbors
                        if neighbor_node.val not in adj_dict
                    ]
                )

        bfs(node)
        new_nodes = self.build_new_nodes(adj_dict)
        return new_nodes[0]


def main():
    """Clone Graph on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

        >>> n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
        >>> n1.neighbors = [n2, n4]
        >>> n2.neighbors = [n1, n3]
        >>> n3.neighbors = [n2, n4]
        >>> n4.neighbors = [n3, n1]
        >>> example_case_1 = n1

    Example 1:
        >>> cg = sol.cloneGraph(example_case_1)
        >>> is_cloned_graph(n1, cg)
        True
        >>> cg_bfs = sol.cloneGraphBFS(example_case_1)
        >>> is_cloned_graph(n1, cg_bfs)
        True

    Example 2:
        >>> n1.neighbors = []
        >>> cg = sol.cloneGraph(n1)
        >>> is_cloned_graph(n1, cg)
        True
        >>> cg_bfs = sol.cloneGraphBFS(n1)
        >>> is_cloned_graph(n1, cg_bfs)
        True

    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
