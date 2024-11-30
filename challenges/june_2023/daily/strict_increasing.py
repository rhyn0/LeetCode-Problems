"""Daily Challenge on June 17, 2023 on LeetCode."""

# Standard Library
from bisect import bisect_right
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    MAX_INT = 10**9

    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        """Return number of operations needed to make `arr1` strictly increasing.

        An operation is to take any number from `arr2` and overwrite
        a value in `arr1`. E.g. given 0 <= i < arr1.length and 0 <= j < arr2.length
        can do arr1[i] = arr2[j].

        Args:
            arr1 (list[int]): Array to get in strictly increasing order
            arr2 (list[int]): Reserve of numbers to use in operations

        Returns:
            int: Minimum number of operations needed
        """
        arr2.sort()
        n2 = len(arr2)
        dp = {-1: 0}
        for val in arr1:
            new_dp = defaultdict(lambda: 10**9)
            for prev, prev_val in dp.items():
                if val > prev:
                    new_dp[val] = min(new_dp[val], prev_val)
                a2_idx = bisect_right(arr2, prev)
                if a2_idx < n2:
                    new_dp[arr2[a2_idx]] = min(new_dp[arr2[a2_idx]], 1 + prev_val)
            dp = new_dp
        return min(dp.values()) if dp else -1


def main() -> None:
    """1187. Make Array Strictly Increasing on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,5,3,6,7], [1,3,2,4]
        >>> example_case_2 = [1,5,3,6,7], [4,3,1]
        >>> example_case_3 = [1,5,3,6,7], [1,6,3,3]

    Example 1:
        >>> sol.makeArrayIncreasing(*example_case_1)
        1

    Example 2:
        >>> sol.makeArrayIncreasing(*example_case_2)
        2

    Example 3:
        >>> sol.makeArrayIncreasing(*example_case_3)
        -1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
