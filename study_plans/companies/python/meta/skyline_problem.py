"""Meta Interview Question Practice List on LeetCode.

218. The Skyline Problem on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    >>> example_case_2 = [[0,2,3],[2,5,3]]

Example 1:
    >>> sol.getSkyline(example_case_1)
    [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

Example 2:
    >>> sol.getSkyline(example_case_2)
    [[0, 3], [5, 0]]
"""


class Solution:  # noqa: D101
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        """Return the skyline outline of the given buildings.

        The given points are the left points of any line segments.
        Gaps between buildings will count as the skyline outline and
        should have height 0. The last point of the outline should also be
        height 0 as the end of the skyline.

        Args:
            buildings (list[list[int]]): List of buildings described as [left, right, height]

        Returns:
            list[list[int]]: List of skyline outline points
        """  # noqa: E501
        # get all the edges of the buildings and sort by x value
        edges = sorted({x for building in buildings for x in building[:2]})
        n = len(edges)
        roots = list(range(n))
        # what index does each edge value map to
        edge_idx_lookup = {edge: i for i, edge in enumerate(edges)}
        # go by descending height over buildings, don't mess with input values
        height_buildings = sorted(buildings, key=lambda x: -x[2])
        heights = [0] * n

        def uf_find(x: int) -> int:
            nonlocal roots
            if x != roots[x]:
                # path shortening
                roots[x] = uf_find(roots[x])
            return roots[x]

        def uf_union(x: int, y: int):
            nonlocal roots
            roots[x] = roots[y]

        for left, right, height in height_buildings:
            left_idx, right_idx = edge_idx_lookup[left], edge_idx_lookup[right]
            while left_idx < right_idx:
                # get their roots
                left_idx = uf_find(left_idx)

                # if the root of left side is still in this building, we update heights
                if left_idx < right_idx:
                    uf_union(left_idx, right_idx)
                    heights[left_idx] = height
                    left_idx += 1

        rv = []
        for i, h in enumerate(heights):
            if i == 0 or heights[i - 1] != h:
                rv.append([edges[i], h])
        return rv
