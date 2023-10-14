"""Daily Challenge for June 28, 2023 on LeetCode."""
# Standard Library
from collections import defaultdict
from decimal import Decimal
from decimal import localcontext
import doctest
import heapq


class Solution:  # noqa: D101
    def maxProbability(  # noqa: PLR0913
        self,
        n: int,
        edges: list[list[int]],
        prob_success: list[float],
        start: int,
        end: int,
    ) -> float:
        """Return maximum probability for a path between start and end nodes.

        Given a graph, and a probability of success
        for a nondirectional weighted graph. Each edge has a chance
        of successfully crossing over.

        Args:
            n (int): Number of nodes
            edges (list[list[int]]): Each edge described as [[i, j] ...]
            prob_success (list[float]): probability for each edge
            start (int): starting node
            end (int): target node

        Returns:
            float: Maximum probability, or 0.0 if no path exists
        """
        adjacencies = defaultdict(list)
        for prob, (start_edge, end_edge) in zip(prob_success, edges, strict=True):
            adjacencies[start_edge].append((end_edge, Decimal(prob)))
            adjacencies[end_edge].append((start_edge, Decimal(prob)))
        best_prob_node = [0] * n
        best_prob_node[start] = 1
        q = [(-1, start)]
        while q:
            prev_prob, node = heapq.heappop(q)
            if node == end:
                return -float(prev_prob)
            for adj_node, prob in adjacencies[node]:
                alt_prob = -prob * prev_prob
                if alt_prob > best_prob_node[adj_node]:
                    best_prob_node[adj_node] = alt_prob
                    heapq.heappush(q, (-alt_prob, adj_node))

        # failure value set by LeetCode
        return 0.0


def float_compare(x: float, y: float) -> bool:
    """Compare the given floats given constraints of problem."""
    with localcontext() as ctx:
        # Problem says, correct if they are within 10^-5 of the correct answer
        ctx.prec = 5
        return (
            ctx.compare(
                ctx.create_decimal_from_float(x),
                ctx.create_decimal_from_float(y),
            )
            == 0
        )


def main() -> None:
    """1514. Path with Maximum Probability on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2
        >>> example_case_2 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2
        >>> example_case_3 = 3, [[0,1]], [0.5], 0, 2

    Example 1:
        >>> float_compare(sol.maxProbability(*example_case_1), 0.2500)
        True

    Example 2:
        >>> float_compare(sol.maxProbability(*example_case_2), 0.3000)
        True

    Example 3:
        >>> float_compare(sol.maxProbability(*example_case_3), 0.0)
        True
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
