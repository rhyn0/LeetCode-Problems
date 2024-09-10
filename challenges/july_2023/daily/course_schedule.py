"""Daily Challenge for July 13, 2023 on LeetCode."""

# Standard Library
from collections import defaultdict
from collections import deque
import doctest


class Solution:  # noqa: D101
    def canFinish(self, num_courses: int, prereq: list[list[int]]) -> bool:
        """Return if possible to complete all courses with the given prerequisites.

        Prerequisite list is of form [a_i, b_i] where b_i must be taken before a_i.
        Courses are numbered from [0, num_courses)

        Args:
            num_courses (int): Total number of courses
            prereq (list[list[int]]): List of prerequisites

        Returns:
            bool: True if all courses can be completed, False otherwise
        """
        num_inbound_edges = defaultdict(int)
        node_neighbors: defaultdict[int, list[int]] = defaultdict(list)
        for to_node, from_node in prereq:
            node_neighbors[from_node].append(to_node)
            num_inbound_edges[to_node] += 1

        num_visited_nodes = 0
        q = deque(node for node in range(num_courses) if num_inbound_edges[node] == 0)
        while q:
            num_visited_nodes += 1
            curr_node = q.popleft()
            for neighbor in node_neighbors[curr_node]:
                num_inbound_edges[neighbor] -= 1
                if num_inbound_edges[neighbor] == 0:
                    q.append(neighbor)

        return num_courses == num_visited_nodes


def main() -> None:
    """207. Course Schedule on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 2, [[1,0]]
        >>> example_case_2 = 2, [[1,0],[0,1]]

    Example 1:
        >>> sol.canFinish(*example_case_1)
        True

    Example 2:
        >>> sol.canFinish(*example_case_2)
        False
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
