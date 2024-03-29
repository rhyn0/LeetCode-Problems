# Standard Library
from collections import defaultdict
from collections import deque
import doctest


class Solution:  # noqa: D101
    def findOrder(  # spec
        self,
        num_courses: int,
        prerequisites: list[list[int]],
    ) -> list[int]:
        """Return a topologically sorted set of classes with prerequisites.

        Prerequisites are directed edges into a course vertex.
        Uses Kahn's algorithm to find answer.

        Args:
            num_courses (int): Total number of vertices
            prerequisites (List[List[int]]): List of edges, (destination, source)

        Returns:
            List[int]: topologically sorted vertices
        """
        inbounds, outbounds = [0] * num_courses, defaultdict(list)
        for course, prereq in prerequisites:
            outbounds[prereq].append(course)
            inbounds[course] += 1
        queue, node_visits, topo_order = deque(), 0, []
        for i in range(num_courses):
            if inbounds[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            node_visits += 1
            topo_order.append(curr)
            for neighbor in outbounds[curr]:
                inbounds[neighbor] -= 1
                if inbounds[neighbor] == 0:
                    queue.append(neighbor)
        if node_visits != num_courses:
            return []
        return topo_order


def main() -> None:
    """Course Schedule II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.findOrder(2, [[1,0]])
        [0, 1]

    Example 2:
        An optional answer for this would be [0, 2, 1, 3]
        >>> sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
        [0, 1, 2, 3]

    Example 2:
        >>> sol.findOrder(1, [])
        [0]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
