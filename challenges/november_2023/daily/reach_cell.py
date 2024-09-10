"""Daily Challenge for November 8 on LeetCode: Problem #2849 [Medium]."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def isReachableAtTime(
        self,
        sx: int,
        sy: int,
        fx: int,
        fy: int,
        t: int,
    ) -> bool:
        """Return if finish is reachable from start in exactly `t` seconds.

        This exists in an infinite 2D grid.
        Cells of grid can be visited multiple times.
        From a cell can move to any of the adjacent 8 cells.

        Args:
            sx (int): Starting x position
            sy (int): Starting y position
            fx (int): Finish x position
            fy (int): Finish y position
            t (int): Total time to use up

        Returns:
            bool: True if possible, False otherwise
        """
        # there are min(manhat_x, manhat_y) diagonal moves used
        # this minimizes the number of moves needed
        min_number_moves = max(abs(fx - sx), abs(fy - sy))
        if min_number_moves == 0:
            # if start is finish
            return t != 1
        return t >= min_number_moves


def main() -> None:
    """2849. Determine if a Cell Is Reachable at a Given Time on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 =  2, 4, 7, 7, 6
        >>> example_case_2 =  3, 1, 7, 3, 3

    Example 1:
        >>> sol.isReachableAtTime(*example_case_1)
        True

    Example 2:
        >>> sol.isReachableAtTime(*example_case_2)
        False
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
