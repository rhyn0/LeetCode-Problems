"""Weekly Challenge on LeetCode: Problem #505 [Medium]."""

# Standard Library
from collections import defaultdict
from collections import deque
import doctest
from enum import IntEnum
from operator import add
from operator import sub


class MazeTypes(IntEnum):
    """Enum for types of squares in a given maze."""

    WALL = 1
    FREE = 0


def print_grid(grid: list[list], start: list[int], end: list[int]) -> None:
    """Print grid in a readable format."""
    for i in range(len(grid)):
        print(f"{i}: ", end="")  # noqa: T201
        for j in range(len(grid[i])):
            if (i, j) == tuple(start):
                print("S", end="")  # noqa: T201
            elif (i, j) == tuple(end):
                print("E", end="")  # noqa: T201
            else:
                print(grid[i][j], end="")  # noqa: T201
        print()  # noqa: T201


class Solution:  # noqa: D101
    @staticmethod
    def _valid(x: int, y: int, maze: list[list[int]]) -> bool:
        m, n = len(maze), len(maze[0])
        return 0 <= x < m and 0 <= y < n and maze[x][y] == MazeTypes.FREE

    @classmethod
    def _find_y_stop(
        cls,
        pos: tuple[int, int],
        maze: list[list[int]],
        *,
        incr: bool = True,
    ) -> tuple[int, int]:
        x, y = pos
        op = add if incr else sub
        while cls._valid(x, y, maze):
            y = op(y, 1)
        # while loop will overshoot by one, so go backwards one first
        y = op(y, -1)
        return (x, y)

    @classmethod
    def _find_x_stop(
        cls,
        pos: tuple[int, int],
        maze: list[list[int]],
        *,
        incr: bool = True,
    ) -> tuple[int, int]:
        x, y = pos
        op = add if incr else sub
        while cls._valid(x, y, maze):
            x = op(x, 1)
        # while loop will overshoot by one, so go backwards one first
        x = op(x, -1)
        return (x, y)

    def shortestDistance(  # noqa: D102
        self,
        maze: list[list[int]],
        start: list[int],
        destination: list[int],
    ) -> int:
        # do this using BFS, only adding stop points when we hit a wall
        # given an m x n matrix, 0 is free space 1 is a wall
        def squares_traveled(p1: tuple[int, int], p2: tuple[int, int]) -> int:
            # manhattan distance
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        dest_tup = tuple(destination)
        que = deque(
            [(start[0], start[1])],
        )  # position
        distance_to_point = defaultdict(lambda: float("inf"))
        distance_to_point[tuple(start)] = 0
        while que:
            curr_pos = que.popleft()
            for new_pos in [
                self._find_y_stop(curr_pos, maze, incr=True),
                self._find_y_stop(curr_pos, maze, incr=False),
                self._find_x_stop(curr_pos, maze, incr=True),
                self._find_x_stop(curr_pos, maze, incr=False),
            ]:
                segment_distance = squares_traveled(curr_pos, new_pos)
                if (
                    distance_to_point[curr_pos] + segment_distance
                    < distance_to_point[new_pos]
                ):
                    distance_to_point[new_pos] = (
                        distance_to_point[curr_pos] + segment_distance
                    )
                    que.append(new_pos)

        min_dist = distance_to_point[dest_tup]
        if isinstance(min_dist, float):
            return -1
        return min_dist


def main() -> None:
    """505. The Maze II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],\
            [0,0,0,0,0]],[0,4], [4,4])
        >>> example_case_2 = ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],\
            [0,0,0,0,0]],[0,4],[3,2])
        >>> example_case_3 = ([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],\
            [0,1,0,0,0]], [4,3],[0,1])

    Example 1:
        >>> sol.shortestDistance(*example_case_1)
        12

    Example 2:
        >>> sol.shortestDistance(*example_case_2)
        -1

    Example 3:
        >>> sol.shortestDistance(*example_case_3)
        -1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
