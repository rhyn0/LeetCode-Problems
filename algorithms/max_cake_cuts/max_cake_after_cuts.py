# Standard Library
import doctest
from itertools import pairwise


class SolutionFailed:  # noqa: D101
    def maxArea(  # spec
        self,
        height: int,
        width: int,
        horiz_cuts: list[int],
        vert_cuts: list[int],
    ) -> int:
        """Find maximum contiguous area of cake given the set of cuts to be made.

        !!!INCOMPLETE!!!

        Args:
            height (int): height of cake in 2d plane
            width (int): width of cake in 2d plane
            horiz_cuts (List[int]): List of cuts to be made after given number
                of elements in height
            vert_cuts (List[int]): List of cuts to be made after given number
                of elements in width.

        Returns:
            int
        """
        top, bottom, left, right = 0, height, 0, width
        for i, cut in enumerate(horiz_cuts):
            adj_cut, adj_h = cut - top, bottom - top
            if adj_cut < adj_h / 2:
                top = max(top, cut)
            elif adj_cut == adj_h / 2 and i != len(horiz_cuts) - 1:
                bottom = cut
                break
            else:
                bottom = min(bottom, cut)
        for i, cut in enumerate(vert_cuts):
            adj_cut, adj_w = cut - left, right - left
            if adj_cut < adj_w / 2:
                left = max(left, cut)
            elif adj_cut == adj_w / 2 and i != len(horiz_cuts) - 1:
                right = cut
                break
            else:
                right = min(right, cut)
        return ((bottom - top) * (right - left)) % (10**9 + 7)


# After a quick hint, the following was attempted.


class Solution:  # noqa: D101
    def maxArea(  # spec
        self,
        h: int,
        w: int,
        horiz_cuts: list[int],
        vertical_cuts: list[int],
    ) -> int:
        """Find maximum contiguous area of cake given the set of cuts to be made.

        Takes whole set of cuts in direction and finds greatest gap between them.

        Args:
            h (int): height of cake in 2d plane
            w (int): width of cake in 2d plane
            horiz_cuts (List[int]): List of cuts to be made after given
                number of elements in height
            vertical_cuts (List[int]): List of cuts to be made after given
                number of elements in width.

        Returns:
            int
        """
        horiz_cuts.extend([0, h])
        vertical_cuts.extend([0, w])
        h_max = max(pairwise(sorted(horiz_cuts)), key=lambda t: t[1] - t[0])
        w_max = max(pairwise(sorted(vertical_cuts)), key=lambda t: t[1] - t[0])
        h_max, w_max = h_max[1] - h_max[0], w_max[1] - w_max[0]
        return (h_max * w_max) % (10**9 + 7)


def main() -> None:
    """1465. Maximum Area of a Piece of Cake on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 5, 4, [1, 2, 4], [1, 3]
        >>> example_case_2 = 5, 4, [3, 1], [1]
        >>> test_case_1 = 5, 4, [3], [3]
        >>> test_case_2 = 5, 2, [3, 1, 2], [1]

    Example 1:
        >>> sol.maxArea(*example_case_1)
        4

    Example 2:
        >>> sol.maxArea(*example_case_2)
        6

    Test 1:
        >>> sol.maxArea(*test_case_1)
        9

    Test 2:
        >>> sol.maxArea(*test_case_2)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
