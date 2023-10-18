"""Daily Challenge on LeetCode for October 18: Problem #2050 [Hard]."""
# Standard Library
from collections import defaultdict
from collections import deque
import doctest


class Solution:  # noqa: D101
    def mininumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """Return the minimum amount of time to complete all the courses.

        Courses can be taken at the same time, but a course cannot be taken until
        all of its prerequisites are completed. The amount of time a course takes is
        given by time[i - 1]. Courses are numbered from 1 to n.

        Args:
            n (int): Number of courses.
            relations (list[list[int]]): Listing of prerequisites, [prev, next]
            time (list[int]): Amount of time to complete each course.

        Returns:
            int: Minimum amount of time to complete all.
        """
        outbound_edges = defaultdict(list)
        inbound_degree = [0] * n
        for prev_node, next_node in relations:
            inbound_degree[next_node - 1] += 1
            outbound_edges[prev_node - 1].append(next_node - 1)

        # max time to reach each node starting from a zero prereq course
        max_time = [0] * n
        # enqueue all courses with no prerequisites
        queue = deque()
        for course, degree in enumerate(inbound_degree):
            if degree == 0:
                queue.append(course)
                max_time[course] = time[course]

        while queue:
            course = queue.popleft()
            for next_node in outbound_edges[course]:
                max_time[next_node] = max(
                    max_time[next_node],
                    max_time[course] + time[next_node],
                )
                inbound_degree[next_node] -= 1
                if inbound_degree[next_node] == 0:
                    queue.append(next_node)

        return max(max_time)


def main() -> None:
    """2050. Parallel Courses III on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = (3, [[1,3],[2,3]], [3,2,5])
        >>> example_case_2 = (5,[[1,5],[2,5],[3,5],[3,4],[4,5]],[1,2,3,4,5])
        >>> test_case_1 = (9, [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],\
            [4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]],\
                 [9,5,9,5,8,7,7,8,4])

    Example 1:
        >>> sol.mininumTime(*example_case_1)
        8

    Example 2:
        >>> sol.mininumTime(*example_case_2)
        12

    Test 1:
        >>> sol.mininumTime(*test_case_1)
        32
    """


if __name__ == "__main__":
    Solution().mininumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5])
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
