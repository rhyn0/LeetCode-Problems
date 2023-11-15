"""Daily Challenge for November 11 on LeetCode: Problem #2642 [Hard]."""

# Standard Library
from collections import defaultdict
import doctest
import heapq
from typing import Any


class Graph:
    """For a graph of n nodes this object implements the way to calculate shortest path.

    Edges can be added in after instantiation.
    Shortest path can be found between two existing nodes.
    Edges are described as [from_node, to_node, weight].
    """

    def __init__(self, n: int, edges: list[list[int]]) -> None:  # noqa: D107
        self.num_nodes = n
        # store adjancency from nodes against to nodes and weights
        self.adjacency = defaultdict(list)
        for from_node, to_node, weight in edges:
            self.adjacency[from_node].append((to_node, weight))

    def addEdge(self, edge: list[int]) -> None:  # noqa: D102
        self.adjacency[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:  # noqa: D102
        distances = defaultdict(lambda: float("inf"))
        visited = set()
        distances[node1] = 0
        pq = [(0, node1)]
        heapq.heapify(pq)
        # print(pq)
        # print(self.adjacency.items())
        # djikstra's algorithm without tracking the path
        while pq:
            weight, node = heapq.heappop(pq)
            if node == node2:
                return weight
            if node in visited:
                continue
            # print(node, distances.items())
            visited.add(node)
            for to_node, edge_weight in self.adjacency[node]:
                if to_node in visited:
                    continue
                distances[to_node] = min(distances[to_node], weight + edge_weight)
                heapq.heappush(pq, (distances[to_node], to_node))
        # if no path found
        return -1


class FloydWarshallGraph:
    """Do same as above but using Floyd-Warshall Algorithm."""

    def __init__(self, n: int, edges: list[list[int]]) -> None:  # noqa: D107
        self.num_nodes = n
        self.adjacency = [[float("inf")] * n for _ in range(n)]
        for from_node, to_node, weight in edges:
            self.adjacency[from_node][to_node] = weight
        # initialize path to self as 0
        for node in range(n):
            self.adjacency[node][node] = 0
        # find shortest paths between all nodes by using a different node i in between
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                for k in range(self.num_nodes):
                    self.adjacency[j][k] = min(
                        self.adjacency[j][k],  # current shortest path
                        self.adjacency[j][i] + self.adjacency[i][k],  # path through i
                    )

    def addEdge(self, edge: list[int]) -> None:  # noqa: D102
        from_node, to_node, cost = edge
        # test if there exists a shorter path through the new edge
        # for all current paths from i->j
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                self.adjacency[i][j] = min(
                    self.adjacency[i][j],  # current shortest path
                    # path through new edge
                    self.adjacency[i][from_node] + cost + self.adjacency[to_node][j],
                )

    def shortestPath(self, node1: int, node2: int) -> int:  # noqa: D102
        dist = self.adjacency[node1][node2]
        return dist if dist != float("inf") else -1


def test_design_inputs(
    cls: type,
    func_calls: list[str],
    inputs: list[list[Any]],
) -> list[Any]:
    """Call input functions with associated inputs and return their output as list."""
    # first index is always an initialization
    sol = cls(*inputs[0])
    return [None] + [
        sol.__getattribute__(func)(*args)
        for func, args in zip(func_calls[1:], inputs[1:], strict=True)
    ]


def main() -> None:
    """2642. Design Graph With Shortest Path Calculator on LeetCode.

    ====================================================

    Test Methods:

    Test 1:
        >>> test_design_inputs(Graph,\
            [Graph, "shortestPath", "shortestPath", "addEdge", "shortestPath"],\
            [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3],\
                 [[1, 3, 4]], [0, 3]],\
            )
        [None, 6, -1, None, 6]
        >>> test_design_inputs(FloydWarshallGraph,\
            [Graph, "shortestPath", "shortestPath", "addEdge", "shortestPath"],\
            [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3],\
                 [[1, 3, 4]], [0, 3]],\
            )
        [None, 6, -1, None, 6]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
