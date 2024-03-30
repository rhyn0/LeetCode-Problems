"""Daily Challenge for June 4, 2023 on LeetCode.

Previously did problem for a study plan.
"""

# Standard Library
from collections import deque
import doctest


class Solution:  # noqa: D101
    def findCircleNum(self, connected: list[list[int]]) -> int:  # spec
        """Return number of connected components in graph defined by connection list.

        Input is a N x N matrix representing which nodes each node is connected to.
        This function will modify the input object.

        Args:
            connected (List[List[int]]): connection matrix

        Returns:
            int: number of connected components
        """
        rows, cols = len(connected), len(connected[0])
        ret_num_prov = 0

        def dfs(x_row: int) -> None:
            connected[x_row][x_row] = 0
            for i in range(cols):
                if connected[x_row][i] == 1:
                    connected[x_row][i] = 0
                    connected[i][x_row] = 0
                    dfs(i)

        for i_row in range(rows):
            if connected[i_row][i_row] == 1:
                ret_num_prov += 1
                dfs(i_row)
        return ret_num_prov

    def findCircleNumBFS(self, connected: list[list[int]]) -> int:
        """Return same as above using BFS."""
        n = len(connected)  # square matrix
        visited = set()  # store node int visited
        num_provinces = 0

        def bfs(start_node: int) -> None:
            que = deque([start_node])  # nodes to visit
            while que:
                curr_node = que.popleft()
                visited.add(curr_node)
                for node, attached in enumerate(connected[curr_node]):
                    if attached == 1 and node not in visited:
                        que.append(node)

        for node in range(n):
            if node in visited:
                continue
            num_provinces += 1
            bfs(node)

        return num_provinces

    def findCircleNumFlatBFS(self, connected: list[list[int]]) -> int:
        """Return same as above using BFS with no function overhead."""
        n = len(connected)
        num_provinces = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            num_provinces += 1
            que = deque([])
            visited.add(node)
            # amazes me that by adding this outside the 'while' makes it faster
            # i guess popleft is expensive
            for adj_node in range(n):
                if adj_node == node or connected[node][adj_node] == 0:
                    continue
                que.append(adj_node)
                visited.add(adj_node)

            while que:
                curr_node = que.popleft()
                for adj_node in range(n):
                    if connected[curr_node][adj_node] == 0 or adj_node in visited:
                        continue
                    que.append(adj_node)
                    visited.add(adj_node)
        return num_provinces


def main() -> None:
    """547. Number of Provinces on LeetCode.

    ====================================================

    Setup:
        >>> from copy import deepcopy
        >>> sol = Solution()
        >>> example_case_1 = [[1,1,0],[1,1,0],[0,0,1]]
        >>> example_case_2 = [[1,0,0],[0,1,0],[0,0,1]]

    Example 1:
        >>> sol.findCircleNum(deepcopy(example_case_1))
        2
        >>> sol.findCircleNumBFS(example_case_1)
        2
        >>> sol.findCircleNumFlatBFS(example_case_1)
        2

    Example 2:
        >>> sol.findCircleNum(deepcopy(example_case_2))
        3
        >>> sol.findCircleNumBFS(example_case_2)
        3
        >>> sol.findCircleNumFlatBFS(example_case_2)
        3

    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
