"""Daily Challenge on LeetCode: Problem #1095 [Medium]."""
# Standard Library
from collections import UserList
import doctest


# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# Have to implement here to get the code to run
class MountainArray(UserList):  # noqa: D101
    def get(self, index: int) -> int:  # noqa: D102
        return self[index]

    def length(self) -> int:  # noqa: D102
        return len(self)


class Solution:  # noqa: D101
    def findInMountainArray(  # noqa: D102
        self,
        target: int,
        mountain_arr: "MountainArray",
    ) -> int:
        arr_length = mountain_arr.length()
        left, right = 1, arr_length - 2
        peak_value = -1
        # find the peak
        while left < right:
            mid = (left + right) // 2
            test_val, test_right_val = mountain_arr.get(mid), mountain_arr.get(mid + 1)
            peak_value = max(peak_value, test_val, test_right_val)
            if test_val < test_right_val:
                left = mid + 1
            else:
                right = mid

        peak_index = left

        # search left monotonically increasing
        left, right = 0, peak_index
        while left < right:
            mid = (left + right) // 2
            test_val = mountain_arr.get(mid)
            if target <= test_val:
                right = mid
            else:
                left = mid + 1

        if mountain_arr.get(left) == target:
            return left

        # search right monotonically decreasing
        left, right = peak_index + 1, arr_length - 1
        while left < right:
            mid = (left + right) // 2
            test_val = mountain_arr.get(mid)
            if target < test_val:
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target:
            return left

        return -1


def main() -> None:
    """1095. Find in Mountain Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = (3, MountainArray([1, 2, 3, 4, 5, 3, 1]))
        >>> example_case_2 = (3, MountainArray([0,1,2,4,2,1]))

    Example 1:
        >>> sol.findInMountainArray(*example_case_1)
        2

    Example 2:
        >>> sol.findInMountainArray(*example_case_2)
        -1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
