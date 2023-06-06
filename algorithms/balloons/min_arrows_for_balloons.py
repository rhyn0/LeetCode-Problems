# Standard Library
import doctest
from operator import itemgetter


class Solution:  # noqa: D101
    def findMinArrowShots(self, points: list[list[int]]) -> int:  # spec
        """Return minimum number of arrows to pop all balloons.

        Balloons are defined by a start edge and end edge on an axis.
        Arrows pop all balloons above a certain point on that axis.

        By sorting the end edge of balloons in the array, can guarantee
        that all edges after current are greater than or equal to current.
        Then as long as the start edge of the next one is less than current end edge
        there exists an overlap point between current and the next one.

        Args:
            points (list[list[int]]): list of balloon edge definitions

        Returns:
            int: Number of arrows needed
        """
        points.sort(key=itemgetter(1, 0))
        arrows = 1
        _, least_end = points[0]
        for next_start, next_end in points[1:]:
            if next_start > least_end:
                arrows += 1
                least_end = next_end

        return arrows


def main() -> None:
    """Minimum Number of Arrows to Burst Balloons on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
        2

    Example 2:
        >>> sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
        4

    Example 3:
        >>> sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
        2
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
