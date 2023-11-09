"""Weekly Challenge #2 on LeetCode: Problem #573 [Medium].

This problem has been solved before in this repository.
Check out that solve at: ../../../algorithms/squirrels
"""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def minDistance(
        self,
        _height: int,  # unused
        _width: int,  # unused
        tree: list[int],
        squirrel: list[int],
        nuts: list[list[int]],
    ) -> int:
        """Return the minimum distance traveled for squirrel to collect nuts.

        Squirrel can carry only one nut at a time, and squirrel can only travel
        in cardinal directions. All nuts must be deposited onto the tree's cell.

        Args:
            tree (list[int]): Position of the tree in the grid
            squirrel (list[int]): Starting position of the squirrel
            nuts (list[list[int]]): Location of the ith nut

        Returns:
            int: Minimum distance necessary to pickup all the nuts
        """

        def _manhat_dist(p1: list[int], p2: list[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # check distance from tree to nut
        # maximize the distance saved by having squirrel travel to this nut first
        dist_saved = -float("inf")
        total_dist_travel = 0
        for nut in nuts:
            tree_nut_dist = _manhat_dist(tree, nut)
            squirrel_nut_dist = _manhat_dist(squirrel, nut)
            dist_saved = max(dist_saved, tree_nut_dist - squirrel_nut_dist)
            # store that we always travel from tree to nut and back
            total_dist_travel += 2 * tree_nut_dist

        # apply the best savings
        if isinstance(dist_saved, float):
            # no nuts
            return -1
        return total_dist_travel - dist_saved


def main() -> None:
    """#573. Squirrel Simulation on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 5, 7, [2,2], [4,4], [[3,0], [2,5]]
        >>> example_case_2 = 1, 3, [0,1], [0,0], [[0,2]]

    Example 1:
        >>> sol.minDistance(*example_case_1)
        12

    Example 2:
        >>> sol.minDistance(*example_case_2)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
