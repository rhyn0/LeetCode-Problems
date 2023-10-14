"""LeetCode Daily Challenge for April 9, 2023.

Doing after the day.
"""
# Standard Library
from collections import deque
import doctest
from typing import Final


class Solution:  # noqa: D101
    COLOR_START: Final[int] = ord("a")
    COLOR_RANGE: Final = 26  # lowercase english alphabet only
    INF: Final = 10**5 + 1  # special overflow number for errors in DFS

    @classmethod
    def calculate_adjacency_degree(
        cls,
        colors: str,
        edge_list: list[list[int]],
        *,
        bidir: bool = True,
    ) -> tuple[list[list[int]], list[int]]:
        """Return adjacency list and in degree for each node in given."""
        adj_list = [[] for _ in range(len(colors))]
        indegree = [0] * len(colors)
        for node_from, node_to in edge_list:
            adj_list[node_from].append(node_to)
            if bidir:
                adj_list[node_to].append(node_from)
            indegree[node_to] += 1

        return adj_list, indegree

    @staticmethod
    def get_starting_nodes(in_degree: list[int]) -> list[int]:
        """Return list of nodes with in degree of 0."""
        return [i for i, degree in enumerate(in_degree) if degree == 0]

    @classmethod
    def update_color_counts(
        cls,
        color_path_counts: list[list[int]],
        curr_node: int,
        neighbor: int,
        *,
        inward: bool = True,
    ) -> list[list[int]]:
        """Update the color path lengths between current node and a neighbor.

        Depending on traversal direction, either results need to be stored in
        `curr_node` or `neighbor`.

        Args:
            color_path_counts (list[list[int]]): all color path counts
            curr_node (int): current node
            neighbor (int): neighbor to reference work from
            inward (bool, optional): Topological order. Defaults to True.

        Returns:
            list[list[int]]: Update color path counts
        """
        update_node = neighbor if inward else curr_node
        for poss_color in range(cls.COLOR_RANGE):
            color_path_counts[update_node][poss_color] = max(
                color_path_counts[curr_node][poss_color],
                color_path_counts[neighbor][poss_color],
            )
        return color_path_counts

    def largestPathValue(self, colors: str, edge_list: list[list[int]]) -> int:
        """Return largest path color value for a given graph.

        If graph contains cycles, return -1.
        The color value is the number of the same color nodes on a path.
        Nodes are indexed by value, starting at 0

        Args:
            colors (str): Color for each node
            edge_list (list[list[int]]): List of all edges, form of [from, to]

        Returns:
            int: Largest color path
        """
        adjacency_list, degree_list = self.calculate_adjacency_degree(colors, edge_list)
        que = deque(self.get_starting_nodes(degree_list))

        color_path_counts = [[0] * 26 for _ in range(len(colors))]
        answer = num_nodes_seen = 0
        while que:
            curr_node = que.popleft()
            color_path_counts[curr_node][ord(colors[curr_node]) - self.COLOR_START] += 1
            answer = max(
                answer,
                color_path_counts[curr_node][ord(colors[curr_node]) - self.COLOR_START],
            )
            num_nodes_seen += 1

            for neighbor in adjacency_list[curr_node]:
                color_path_counts = self.update_color_counts(
                    color_path_counts,
                    curr_node,
                    neighbor,
                )

                degree_list[neighbor] -= 1
                if degree_list[neighbor] == 0:
                    que.append(neighbor)

        return -1 if num_nodes_seen < len(colors) else answer

    def largestPathValueDFS(self, colors: str, edge_list: list[list[int]]) -> int:
        """Return same as above using DFS."""
        num_nodes = len(colors)
        max_path_color = 0
        visited, stack_state = [False] * num_nodes, [False] * num_nodes
        color_counts = [[0] * self.COLOR_RANGE for _ in range(num_nodes)]
        adj_list, _ = self.calculate_adjacency_degree(colors, edge_list, bidir=False)

        def dfs(curr_node: int, counts: list[list[int]]) -> int:
            if stack_state[curr_node]:
                return self.INF
            if visited[curr_node]:
                return counts[curr_node][ord(colors[curr_node]) - self.COLOR_START]
            stack_state[curr_node] = True
            visited[curr_node] = True
            for neighbor in adj_list[curr_node]:
                if dfs(neighbor, counts) == self.INF:
                    return self.INF
                counts = self.update_color_counts(
                    counts,
                    curr_node,
                    neighbor,
                    inward=False,
                )
            counts[curr_node][ord(colors[curr_node]) - self.COLOR_START] += 1
            stack_state[curr_node] = False
            return counts[curr_node][ord(colors[curr_node]) - self.COLOR_START]

        for node in range(num_nodes):
            max_path_color = max(max_path_color, dfs(node, color_counts))

        return max_path_color if max_path_color != self.INF else -1


def main() -> None:
    """Largest Color Value in a Directed Graph on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ("abaca", [[0,1],[0,2],[2,3],[3,4]])
        >>> example_case_2 = ("a", [[0, 0]])
        >>> test_case_1 = ("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],\
            [6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]])
        >>> test_case_2 = ("nnllnzznn", [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],\
            [5,6],[6,7],[7,8]])

    Example 1:
        >>> sol.largestPathValue(*example_case_1)
        3
        >>> sol.largestPathValueDFS(*example_case_1)
        3

    Example 2:
        >>> sol.largestPathValue(*example_case_2)
        -1
        >>> sol.largestPathValueDFS(*example_case_2)
        -1

    Test 1:
        >>> sol.largestPathValue(*test_case_1)
        3
        >>> sol.largestPathValueDFS(*test_case_1)
        3

    Test 2:
        >>> sol.largestPathValue(*test_case_2)
        5
        >>> sol.largestPathValueDFS(*test_case_2)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
