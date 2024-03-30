"""Daily Challenge for June 29, 2023 on LeetCode."""

# Standard Library
from collections import defaultdict
from collections import deque
from collections.abc import Iterator
import doctest
from itertools import pairwise


class Solution:  # noqa: D101
    NEIGHBORS = (-1, 0, 1, 0, -1)

    @staticmethod
    def _start_point_and_keys(grid: list[str]) -> tuple[tuple[int, int], int]:
        """Return start point (row, col) and total number of keys."""
        start_point = -1, -1
        keys = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "@":
                    start_point = i, j
                if val.islower():
                    keys += 1

        return start_point, keys

    @staticmethod
    def _get_keylock_bitmap(char: str, num_keys: int) -> int:
        """Return an int that represents the bitmap of the given char."""
        pos = num_keys - (ord(char.lower()) - ord("a")) - 1
        return 1 << pos

    def iter_neighbors(
        self,
        pos: tuple[int, int],
    ) -> Iterator[tuple[int, int]]:
        """Return generator for neighbors that aren't walls."""
        for delta_row, delta_col in pairwise(self.NEIGHBORS):
            new_row, new_col = pos[0] + delta_row, pos[1] + delta_col
            if (
                0 <= new_row < self.row_bound
                and 0 <= new_col < self.col_bound
                and self.grid[new_row][new_col] != "#"
            ):
                yield new_row, new_col

    def shortestPathAllKeys(self, grid: list[str]) -> int:
        """Return shortest path to pickup all keys in the grid.

        Grid contains walls (#), open cells (.), and keys with their locks.
        A cell with a lock (A-F) cannot be visited unless the associated
        key (a-f) is currently held.

        Args:
            grid (list[str]): Each string is a row

        Returns:
            int: Shortest path to pickup all keys
        """
        self.grid = grid
        self.row_bound, self.col_bound = len(grid), len(grid[0])
        start_pos, num_keys = self._start_point_and_keys(grid)

        key_state_visited = defaultdict(set)
        key_state_visited[0].add(start_pos)
        q = deque()
        # (row, col), num_moves, keys_bitmap
        # 0 for the bitmap, means we have none
        q.append((start_pos, 0, 0))
        while q:
            pos, moves, curr_keys = q.popleft()
            val = grid[pos[0]][pos[1]]
            if (
                val.isupper()
                and not self._get_keylock_bitmap(val, num_keys) & curr_keys
            ):
                continue
            if val.islower():
                curr_keys |= self._get_keylock_bitmap(val, num_keys)
            if curr_keys == (1 << num_keys) - 1:
                return moves
            for new_pos in self.iter_neighbors(pos):
                if new_pos in key_state_visited[curr_keys]:
                    # switching between the same two cells is a waste of time
                    continue
                key_state_visited[curr_keys].add(new_pos)
                q.append((new_pos, moves + 1, curr_keys))
        return -1


def main() -> None:
    """864. Shortest Path to Get All Keys on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ["@.a..","###.#","b.A.B"]
        >>> example_case_2 = ["@..aA","..B#.","....b"]
        >>> example_case_3 = ["@Aa"]
        >>> test_case_1 = ["@...a",".###A","b.BCc"]

    Example 1:
        >>> sol.shortestPathAllKeys(example_case_1)
        8

    Example 2:
        >>> sol.shortestPathAllKeys(example_case_2)
        6

    Example 3:
        >>> sol.shortestPathAllKeys(example_case_3)
        -1

    Test 1:
        >>> sol.shortestPathAllKeys(test_case_1)
        10
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
