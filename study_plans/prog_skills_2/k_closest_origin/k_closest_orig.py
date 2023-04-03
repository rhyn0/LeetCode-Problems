# Standard Library
from math import sqrt


class Solution:  # noqa: D101
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:  # spec
        """Return list of k closest points to origin in Cartesian plane.

        Distance is calculated by euclidean distance.

        Args:
            points (List[List[int]]): List of all points. Points form [x, y]
            k (int): Number of nearest points to return

        Returns:
            List[List[int]]: k nearest points to origin
        """
        # from queue import PriorityQueue
        # q = PriorityQueue(maxsize=len(points))
        # for p in points:
        #     q.put((sqrt(p[0] ** 2 + p[1] ** 2), p))
        # return [q.get()[1] for _ in range(k)]
        que = [(sqrt(p[0] ** 2 + p[1] ** 2), p) for p in points]
        return [p for _, p in sorted(que, key=lambda x: x[0])][:k]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))  # [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # [[3, 3], [-2, 4]]
