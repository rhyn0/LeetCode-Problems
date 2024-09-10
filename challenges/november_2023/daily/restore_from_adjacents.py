"""Daily Challenge for November 10 on LeetCode: Problem #1743 [Medium]."""

# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:  # noqa: N803
        """Restore an array from the adjacencies of the array.

        The given adjacencies do not imply any order - i.e. the adjacency [i, j]
        does not imply that the index of i is less than that of j.
        For an original array of n unique numbers (and length n), there must be n-1
        adjacencies to solve this.

        Args:
            adjacentPairs (list[list[int]]): List of adjacencies

        Returns:
            list[int]: A valid version of the original array.
        """
        values_adjacent: defaultdict[int, list[int]] = defaultdict(list)
        for num1, num2 in adjacentPairs:
            values_adjacent[num1].append(num2)
            values_adjacent[num2].append(num1)

        start_val = next(key for key, val in values_adjacent.items() if len(val) == 1)
        nums = [start_val]
        curr_adjacency = values_adjacent.pop(start_val)
        while values_adjacent:
            for val in curr_adjacency:
                if val not in values_adjacent:
                    # previously popped, so the previous value in list
                    continue
                nums.append(val)
                # only one number per adjacency can be appended
                curr_adjacency = values_adjacent.pop(val)
                break
        return nums


def main() -> None:
    """1743. Restore the Array From Adjacent Pairs on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[2,1],[3,4],[3,2]]
        >>> example_case_2 = [[4,-2],[1,4],[-3,1]]
        >>> example_case_3 = [[100000,-100000]]

    Example 1:
        >>> sol.restoreArray(example_case_1)
        [1, 2, 3, 4]

    Example 2:
        >>> sol.restoreArray(example_case_2)
        [-2, 4, 1, -3]

    Example 3:
        >>> sol.restoreArray(example_case_3)
        [100000, -100000]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
