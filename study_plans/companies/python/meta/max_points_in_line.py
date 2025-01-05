"""Meta Interview Question Practice List on LeetCode.

149. Max Points on a Line on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[1,1],[2,2],[3,3]]
    >>> example_case_2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

Example 1:
    >>> sol.maxPoints(example_case_1)
    3

Example 2:
    >>> sol.maxPoints(example_case_2)
    4
"""

# Standard Library
from collections import defaultdict


class Solution:  # noqa: D101
    def maxPoints(self, points: list[list[int]]) -> int:
        """Return the maximum number of points that are colinear.

        Args:
            points (list[list[int]]): List of points [x,y]

        Returns:
            int: Maximum colinear points
        """
        seen_max = 0
        n = len(points)
        if n == 1:
            return 1
        for i, (pt_x, pt_y) in enumerate(points):
            seen_slopes: defaultdict[float, int] = defaultdict(int)
            for other_x, other_y in points[i + 1 :]:
                rise = other_y - pt_y
                run = other_x - pt_x
                slope = (rise / run) if run != 0 else float("inf")
                seen_slopes[slope] += 1
            seen_max = max(seen_max, max(seen_slopes.values()) + 1)
            if seen_max == n - i:
                # every point from i on is colinear, no later index will be greater
                break
        return seen_max
