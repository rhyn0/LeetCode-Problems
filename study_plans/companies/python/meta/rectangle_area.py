"""Meta Interview Question Practice List on LeetCode.

223. Rectangle Area on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = -3, 0, 3, 4, 0, -1, 9, 2
    >>> example_case_2 = -2, -2, 2, 2, -2, -2, 2, 2

Example 1:
    >>> sol.computeArea(*example_case_1)
    45

Example 2:
    >>> sol.computeArea(*example_case_2)
    16
"""


class Solution:  # noqa: D101
    def computeArea(  # noqa: PLR0913
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        """Return the total area covered by two rectangles.

        Args:
            ax1 (int): bottom left x of first
            ay1 (int): bottom left y of first
            ax2 (int): top right x of first
            ay2 (int): top right y of first
            bx1 (int): bottom left x of second
            by1 (int): bottom left y of second
            bx2 (int): top right x of second
            by2 (int): top right y of second

        Returns:
            int: total area covered
        """
        area_1 = (ay2 - ay1) * (ax2 - ax1)
        area_2 = (by2 - by1) * (bx2 - bx1)
        # leftmost right corner - rightmost left corner
        overlap_x = min(ax2, bx2) - max(ax1, bx1)
        # lowest top corner - highest bottom corner
        overlap_y = min(ay2, by2) - max(ay1, by1)
        total_overlap = (
            (overlap_x * overlap_y) if overlap_y > 0 and overlap_x > 0 else 0
        )
        return area_1 + area_2 - total_overlap
