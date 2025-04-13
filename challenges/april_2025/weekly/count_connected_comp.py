"""Weekly Challenge for April Week 2.

323. Number of Connected Components in an Undirected Graph on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 5,  [[0,1],[1,2],[3,4]]
    >>> example_case_2 = 5, [[0,1],[1,2],[2,3],[3,4]]

Example 1:
    >>> sol.countComponents(*example_case_1)
    2
    >>> sol.countComponentsBfs(*example_case_1)
    2
    >>> sol.countComponentsUf(*example_case_1)
    2

Example 2:
    >>> sol.countComponents(*example_case_2)
    1
    >>> sol.countComponentsBfs(*example_case_2)
    1
    >>> sol.countComponentsUf(*example_case_2)
    1
"""

# Standard Library
from collections import defaultdict
from collections import deque


class Solution:  # noqa: D101
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """Return number of connected components.

        Args:
            n (int): Number of nodes in graph
            edges (list[list[int]]): Undirected edges between nodes, no repeats

        Returns:
            int: Total number of connected components.
        """
        connections = defaultdict(set)
        visited: set[int] = set()
        connected_comps = 0
        for node_a, node_b in edges:
            connections[node_a].add(node_b)
            connections[node_b].add(node_a)

        def dfs(curr_node: int) -> None:
            if curr_node in visited:
                return
            visited.add(curr_node)
            for conn in connections[curr_node]:
                dfs(conn)
                visited.add(conn)

        for node_num in range(n):
            if node_num not in visited:
                connected_comps += 1
                dfs(node_num)

        return connected_comps

    def countComponentsBfs(self, n: int, edges: list[list[int]]) -> int:
        """Return same as above using BFS."""
        connections = defaultdict(set)
        visited: set[int] = set()
        connected_comps = 0
        for node_a, node_b in edges:
            connections[node_a].add(node_b)
            connections[node_b].add(node_a)

        def bfs(entry_node: int) -> None:
            que = deque([entry_node])
            while que:
                curr_node = que.popleft()
                if curr_node in visited:
                    continue
                visited.add(curr_node)
                que.extend(connections[curr_node])

        for node_num in range(n):
            if node_num not in visited:
                connected_comps += 1
                bfs(node_num)

        return connected_comps

    def countComponentsUf(self, n: int, edges: list[list[int]]) -> int:
        """Return same as above using Union Find."""
        roots = list(range(n))

        def parent(x: int) -> int:
            if roots[x] == x:
                return x
            # path shortening
            roots[x] = parent(roots[x])
            return roots[x]

        def merge(x: int, y: int) -> int:
            """X will now be parent of Y.

            Return how many components were removed because of merge.
            """
            parent_x, parent_y = parent(x), parent(y)
            if parent_x == parent_y:
                return 0
            # arbitrary choice that X becomes parent of Y
            # could make more balanced tree by using size or something
            roots[parent_y] = parent_x
            return 1

        # in beginning each node is a separate component
        connected_comps = n
        for edge_a, edge_b in edges:
            connected_comps -= merge(edge_a, edge_b)

        # number of unique parents
        return connected_comps
