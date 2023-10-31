"""Weekly Challenge on LeetCode: Problem #1197 [Medium]."""
# Standard Library
from collections import deque
import doctest


class Solution:  # noqa: D101
    def minKnightMoves(self, x: int, y: int) -> int:
        """Return minimum number of chess knight moves to reach a point from origin."""
        offsets = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, -1),
            (-2, 1),
        ]
        # starting point is origin
        # (x, y, steps)
        from_origin_que: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        # (x, y) -> steps
        from_origin_dist: dict[tuple[int, int], int] = {(0, 0): 0}

        from_target_que: deque[tuple[int, int, int]] = deque([(x, y, 0)])
        from_target_dist = {(x, y): 0}

        while True:
            origin_x, origin_y, origin_steps = from_origin_que.popleft()
            if (origin_x, origin_y) in from_target_dist:
                return origin_steps + from_target_dist[(origin_x, origin_y)]

            # check for the from target side
            target_x, target_y, target_steps = from_target_que.popleft()
            if (target_x, target_y) in from_origin_dist:
                return target_steps + from_origin_dist[(target_x, target_y)]

            for d_x, d_y in offsets:
                origin_neighbor = (origin_x + d_x, origin_y + d_y)
                target_neighbor = (target_x + d_x, target_y + d_y)
                if origin_neighbor not in from_origin_dist:
                    from_origin_dist[origin_neighbor] = origin_steps + 1
                    from_origin_que.append((*origin_neighbor, origin_steps + 1))

                if target_neighbor not in from_target_dist:
                    from_target_dist[target_neighbor] = target_steps + 1
                    from_target_que.append((*target_neighbor, target_steps + 1))

    def minKnightMovesDFS(self, x: int, y: int) -> int:
        """Return same as above using a simplified offset list."""
        # can claim that path from origin to (x, y) is same as path from
        # origin to any of the rotated quadrants (-x, y), (-x, -y), (x, -y)
        # so we can just focus on the first quadrant (x, y)
        # and track from target to origin

        # additionally it can be shown that all paths from origin to points that satisfy
        # x + y == 2, will take 2 moves. so we have two simple base cases for DFS
        proven_base = 2

        def dfs(x: int, y: int) -> int:
            if (x, y) == (0, 0):
                return 0
            if x + y == proven_base:
                return 2
            return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))


def main() -> None:
    """1197. Minimum Knight Moves on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = (2, 1)
        >>> example_case_2 = (5, 5)
        >>> test_case_1 = (2, 112)

    Example 1:
        >>> sol.minKnightMoves(*example_case_1)
        1
        >>> sol.minKnightMovesDFS(*example_case_1)
        1

    Example 2:
        >>> sol.minKnightMoves(*example_case_2)
        4
        >>> sol.minKnightMovesDFS(*example_case_2)
        4

    Test 1:
        >>> sol.minKnightMoves(*test_case_1)
        56
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
