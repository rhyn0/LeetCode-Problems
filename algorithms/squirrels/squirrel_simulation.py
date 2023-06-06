# Standard Library
import doctest
from typing import TypeAlias

Coordinate: TypeAlias = tuple[int, int] | list[int]


class Solution:  # noqa: D101
    def minDistance(  # noqa: PLR0913 # spec
        self,
        height: int,
        width: int,
        tree: list[int],
        squirrel: list[int],
        nuts: list[list[int]],
    ) -> int:
        """Return minimum distance traveled by squirrel to get all nuts to tree.

        Maximize savings of distance by choosing the most prime nut.

        Args:
            height (int): Height of the grid, UNUSED
            width (int): Width of the grid, UNUSED
            tree (List[int]): X,Y location of home tree
            squirrel (List[int]): X, Y location of squirrel at start
            nuts (List[List[int]]): List of X, Y locations of nuts on board

        Returns:
            int: Minimum distance to collect all nuts
        """
        width = width * height  # need to use

        def manhattan_distance(obj1: Coordinate, obj2: Coordinate) -> int:
            return abs(obj1[0] - obj2[0]) + abs(obj1[1] - obj2[1])

        total_distance_travel = 0
        path_diff = float("-inf")

        # point is to maximize the savings of going from squirrel start to nut
        # when compared with going from tree to nut

        for nut in nuts:
            nut_tree_dist = manhattan_distance(tree, nut)
            total_distance_travel += nut_tree_dist * 2

            path_diff = max(
                path_diff,
                nut_tree_dist - manhattan_distance(squirrel, nut),
            )

        return total_distance_travel - int(path_diff)


def main() -> None:
    """Squirrel Simulation on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.minDistance(height = 5, width = 7, tree = [2,2], squirrel = [4,4],\
            nuts = [[3,0], [2,5]])
        12

    Example 2:
        >>> sol.minDistance(height = 1, width = 3, tree = [0,1], squirrel = [0,0],\
            nuts = [[0,2]])
        3

    Test 1:
        >>> sol.minDistance(height=5, width=5, tree = [3,2], squirrel = [0,1],
        nuts = [[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],[0,0],[2,2],\
            [4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]])
        100

    Test 2:
        >>> sol.minDistance(height=9, width=9, tree = [7,2], squirrel = [7,1],
        nuts = [[3,0],[7,7],[8,8],[0,8],[2,4],[4,5],[3,5],[4,2],[1,8]])
        131
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
