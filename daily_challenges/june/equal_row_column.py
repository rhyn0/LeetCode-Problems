"""Daily Challenge for June 13, 2023 on LeetCode."""
# Standard Library
from collections import Counter
from collections import defaultdict
import doctest
from itertools import product


class Solution:  # noqa: D101
    def equalPairs(self, grid: list[list[int]]) -> int:
        """Return number of pairs of equal rows and columns.

        A row and column are considered equal if there elements
        are the same in the same order.

        Args:
            grid (list[list[int]]): grid to scan for matches

        Returns:
            int: Number of pairs
        """
        columns = defaultdict(list)
        len(grid)
        for row in grid:
            for j, val in enumerate(row):
                columns[j].append(val)
        count = 0
        for row, col in product(grid, columns.values()):
            if row == col:
                count += 1

        return count

    def equalPairsDict(self, grid: list[list[int]]) -> int:
        """Return same as above using a dictionary keyed off tuples."""
        row_counter = Counter(tuple(row) for row in grid)
        n = len(grid)  # n x n grid
        count = 0
        for col_idx in range(n):
            column = (grid[i][col_idx] for i in range(n))
            count += row_counter[tuple(column)]

        return count


def main() -> None:
    """2352. Equal Row and Column Pairs on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[3,2,1],[1,7,6],[2,7,7]]
        >>> example_case_2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

    Example 1:
        >>> sol.equalPairs(example_case_1)
        1
        >>> sol.equalPairsDict(example_case_1)
        1

    Example 2:
        >>> sol.equalPairs(example_case_2)
        3
        >>> sol.equalPairsDict(example_case_2)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
