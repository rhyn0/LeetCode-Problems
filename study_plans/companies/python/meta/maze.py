"""Meta Interview Question Practice List on LeetCode.

490. The Maze on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]
    >>> example_case_2 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2]
    >>> example_case_3 = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]

Example 1:
    >>> sol.hasPath(*example_case_1)
    True
    >>> sol.hasPathCompact(*example_case_1)
    True

Example 2:
    >>> sol.hasPath(*example_case_2)
    False
    >>> sol.hasPathCompact(*example_case_2)
    False

Example 3:
    >>> sol.hasPath(*example_case_3)
    False
    >>> sol.hasPathCompact(*example_case_3)
    False
"""  # noqa: E501

# Standard Library
from collections import deque
from itertools import pairwise


class Solution:  # noqa: D101
    @staticmethod
    def _valid_roll(pos: tuple[int, int], maze: list[list[int]]) -> bool:
        row, col = pos
        n, m = len(maze), len(maze[0])
        return 0 <= row < n and 0 <= col < m and maze[row][col] == 0

    @staticmethod
    def _find_y_stop(
        pos: tuple[int, int],
        maze: list[list[int]],
        *,
        look_up: bool = True,
    ) -> tuple[int, int]:
        """Find the next stop point in this column.

        Look up = True, means go in -row direction else +row
        """
        row, col = pos
        delta = -1 if look_up else 1
        while Solution._valid_roll((row + delta, col), maze):
            row += delta
        return (row, col)

    @staticmethod
    def _find_x_stop(
        pos: tuple[int, int],
        maze: list[list[int]],
        *,
        look_left: bool = True,
    ) -> tuple[int, int]:
        """Find the next stop point in this row.

        Look left = True, means go in -col direction else +col
        """
        row, col = pos
        delta = -1 if look_left else 1
        while Solution._valid_roll((row, col + delta), maze):
            col += delta
        return (row, col)

    def hasPath(
        self,
        maze: list[list[int]],
        start: list[int],
        destination: list[int],
    ) -> bool:
        """Return whether a ball in a maze can make it to `destination` from `start`.

        Args:
            maze (list[list[int]]): The list of cells in maze, 1 is walls.
                Surrounded by walls.
            start (list[int]): [row, col] of the starting position
            destination (list[int]): [row,col] of the goal point

        Returns:
            bool: Whether a path exists for start -> destination
        """
        que: deque[tuple[int, int]] = deque([tuple(start)])
        visited: set[tuple[int, int]] = set()
        while que:
            curr_pos = que.popleft()
            if curr_pos[0] == destination[0] and curr_pos[1] == destination[1]:
                return True
            visited.add(curr_pos)
            up_stop = self._find_y_stop(curr_pos, maze)
            down_stop = self._find_y_stop(curr_pos, maze, look_up=False)
            left_stop = self._find_x_stop(curr_pos, maze)
            right_stop = self._find_x_stop(curr_pos, maze, look_left=False)
            que.extend(
                pos
                for pos in (up_stop, down_stop, left_stop, right_stop)
                if pos not in visited
            )

        return False

    def hasPathCompact(
        self,
        maze: list[list[int]],
        start: list[int],
        destination: list[int],
    ) -> bool:
        """Return same as above, but with all local code.

        No other functions.
        """
        n, m = len(maze), len(maze[0])
        # useful for pairwise iterations over dy,dx
        directions = [-1, 0, 1, 0, -1]
        que: deque[list[int]] = deque()
        que.append(start)
        # can have save memory by using a set here, as we don't need to
        # store visited points for intermediary spots
        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True
        while que:
            curr_pos = que.popleft()
            if curr_pos == destination:
                return True
            for drow, dcol in pairwise(directions):
                row, col = curr_pos
                while 0 <= row < n and 0 <= col < m and maze[row][col] == 0:
                    row += drow
                    col += dcol
                # broke the condition, so we overshot by one
                row -= drow
                col -= dcol
                if not visited[row][col]:
                    visited[row][col] = True
                    que.append([row, col])

        return False
