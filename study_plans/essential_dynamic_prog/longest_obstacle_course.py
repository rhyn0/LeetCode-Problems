"""Essentials of Dynamic Programming LIS Problem on LeetCode."""

# Standard Library
from bisect import bisect_right
import doctest


class Solution:  # noqa: D101
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        """Return length of longest increasing subsequence for each index of array.

        Elements in LIS can either be greater than or equal to previous element.
        The LIS at index `i` must include `obstacles[i]`. Must preserve original
        order of `obstacles`

        Args:
            obstacles (list[int]): array of obstacle height

        Returns:
            list[int]: array of LIS length for each index
        """
        n = len(obstacles)
        length = [1] * n

        running_lis = []
        for i, height in enumerate(obstacles):
            alter_idx = bisect_right(running_lis, height)
            if alter_idx == len(running_lis):
                running_lis.append(height)
            else:
                # overwrite a large number to reduce used search space
                running_lis[alter_idx] = height
            length[i] = alter_idx + 1

        return length


def main() -> None:
    """1964. Find the Longest Valid Obstacle Course at Each Position on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,2,3,2]
        >>> example_case_2 = [2,2,1]
        >>> example_case_3 = [3,1,5,6,4,2]
        >>> self_test_1 = [2,2,1,3]

    Example 1:
        >>> sol.longestObstacleCourseAtEachPosition(example_case_1)
        [1, 2, 3, 3]

    Example 2:
        >>> sol.longestObstacleCourseAtEachPosition(example_case_2)
        [1, 2, 1]

    Example 3:
        >>> sol.longestObstacleCourseAtEachPosition(example_case_3)
        [1, 1, 2, 3, 2, 2]

    Self Test 1:
        >>> sol.longestObstacleCourseAtEachPosition(self_test_1)
        [1, 2, 1, 3]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
