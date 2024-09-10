"""Daily Challenge for November 4 on LeetCode: Problem #1503 [Medium]."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        """Return the last moment when ants fall out of a plank.

        Ants that collide will switch direction instantaneously on the spot.
        """
        max_time = 0
        for ant in left:
            # these are facing left, moving towards 0
            max_time = max(max_time, ant)
        for ant in right:
            # these are facing right, moving towards n
            max_time = max(max_time, n - ant)

        return max_time

    def getLastMomentSimple(self, n: int, left: list[int], right: list[int]) -> int:
        """Return same as above with simpler calculations."""
        max_time = 0
        if left:
            max_time = max(*left, max_time)
        if right:
            max_time = max(n - min(right), max_time)
        return max_time


def main() -> None:
    """1503. Last Moment Before All Ants Fall Out of a Plank on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 4, [4,3], [0,1]
        >>> example_case_2 = 7,  [], [0,1,2,3,4,5,6,7]
        >>> example_case_3 =  7, [0,1,2,3,4,5,6,7], []

    Example 1:
        >>> sol.getLastMoment(*example_case_1)
        4
        >>> sol.getLastMomentSimple(*example_case_1)
        4

    Example 2:
        >>> sol.getLastMoment(*example_case_2)
        7
        >>> sol.getLastMomentSimple(*example_case_2)
        7

    Example 3:
        >>> sol.getLastMoment(*example_case_3)
        7
        >>> sol.getLastMomentSimple(*example_case_3)
        7
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
