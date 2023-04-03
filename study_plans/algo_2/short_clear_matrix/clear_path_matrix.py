# Standard Library
from collections import deque
import doctest


class Solution:  # noqa: D101
    DIRECTIONS = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """Return shortest clear path in a matrix.

        Clear paths are ones created by paths of 0.
        Can move in any of the 8 neighbor cells.

        Args:
            grid (List[List[int]]): 2D array denoting the obstacle grid

        Returns:
            int: Length of shortest path, -1 if no such path
        """
        matrix_size = len(grid)

        def clear_neighbors(row: int, col: int):
            yield from (
                (row + d_row, col + d_col)
                for d_row, d_col in self.DIRECTIONS
                if 0 <= row + d_row < matrix_size
                and 0 <= col + d_col < matrix_size
                and grid[row + d_row][col + d_col] == 0
            )

        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        node_q = deque([(0, 0)])
        # path counts each cell visited as one length.
        grid[0][0] = 1
        while node_q:
            curr = node_q.popleft()
            curr_len = grid[curr[0]][curr[1]]
            if curr == (matrix_size - 1, matrix_size - 1):
                return curr_len

            for neigh_node in clear_neighbors(*curr):
                grid[neigh_node[0]][neigh_node[1]] = curr_len + 1
                node_q.append(neigh_node)

        return -1


def main():
    """Shortest Clear Path in Binary matrix on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.shortestPathBinaryMatrix([[0,1],[1,0]])
        2

    Example 2:
        >>> sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
        4

    Example 3:
        >>> sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])
        -1

    Test 1:
        >>> sol.shortestPathBinaryMatrix([[0]])
        1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
