# Standard Library
import doctest
from functools import cache


class Solution:  # noqa: D101
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:  # spec
        """Return all paths from node 0 to last node in a DAG.

        Args:
            graph (List[List[int]]): list of all the nodes that the ith node connects to

        Returns:
            List[List[int]]: List of all pathways, from 0 to end, available
        """
        size_n = len(graph)
        # memo_nodes: Dict[int, List[List[int]]] = dict()

        @cache
        def dfs(node: int) -> list[list[int]]:
            if node == size_n - 1:
                return [[node]]
            # elif node in memo_nodes:
            #     return memo_nodes[node]
            ret_lists = []
            for child in graph[node]:
                ret_lists.extend([[node, *lower_path] for lower_path in dfs(child)])
            # memo_nodes[node] = ret_lists
            # return memo_nodes[node]
            return ret_lists

        return dfs(0)


def main() -> None:
    """All Paths from Source to Target on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.allPathsSourceTarget([[1,2],[3],[3],[]])
        [[0, 1, 3], [0, 2, 3]]

    Example 2:
        >>> sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
        [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
