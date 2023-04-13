"""LeetCode Daily Challenge for April 9, 2023.

Doing after the day.
"""
# Standard Library
from collections import deque
import doctest


class Solution:  # noqa: D101
    COLOR_START = ord("a")
    COLOR_RANGE = 26  # lowercase english alphabet only

    @classmethod
    def calculate_adjacency_degree(
        cls, colors: str, edge_list: list[list[int]]
    ) -> tuple[list[list[int]], list[int]]:
        """Return adjacency list and in degree for each node in given."""
        adj_list = [[] for _ in range(len(colors))]
        indegree = [0] * len(colors)
        for node_from, node_to in edge_list:
            adj_list[node_from].append(node_to)
            adj_list[node_to].append(node_from)
            indegree[node_to] += 1

        return adj_list, indegree

    @staticmethod
    def get_starting_nodes(in_degree: list[int]) -> list[int]:
        """Return list of nodes with in degree of 0."""
        return [i for i, degree in enumerate(in_degree) if degree == 0]

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
                for poss_color in range(self.COLOR_RANGE):
                    color_path_counts[neighbor][poss_color] = max(
                        color_path_counts[curr_node][poss_color],
                        color_path_counts[neighbor][poss_color],
                    )

                degree_list[neighbor] -= 1
                if degree_list[neighbor] == 0:
                    que.append(neighbor)

        return -1 if num_nodes_seen < len(colors) else answer


def main():
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

    Example 2:
        >>> sol.largestPathValue(*example_case_2)
        -1

    Test 1:
        >>> sol.largestPathValue(*test_case_1)
        3

    Test 2:
        >>> sol.largestPathValue(*test_case_2)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
