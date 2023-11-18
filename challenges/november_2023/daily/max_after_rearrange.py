"""Daily Challenge for November 15 on LeetCode: Problem #1846 [Medium]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        """Return maximum element after decrementing and rearranging.

        The operations of decrementing and rearranging must be performed
        until the given array is in the form of an increasing
        sequence with first index being 1.
        Operations that can be performed is any rearrangement and decrement of values.

        Args:
            arr (list[int]): Starting array

        Returns:
            int: Maximum value of array after operations.
        """
        new_arr = sorted(arr)
        for idx, num in enumerate(new_arr):
            if idx == 0:
                new_arr[idx] = 1
            else:
                new_arr[idx] = min(new_arr[idx - 1] + 1, num)
        return new_arr[-1]

    def maximumElementAfterDecrementingAndRearrangingNoSort(
        self,
        arr: list[int],
    ) -> int:
        """Return same as above without sorting."""
        n = len(arr)
        # count the occurrences of the number that can be j
        # where j is the increasing number in the sequence [1, n]
        count = [0] * (n + 1)
        for num in arr:
            # number can never be increased, so its only helpful up to the min
            count[min(num, n)] += 1

        ans = 1
        # must start at 1, we can ignore any duplicate 1s in the array
        for num in range(2, n + 1):
            # can't increase beyond the +1 increasing subsequence
            # but repeated numbers can be ignored for a point
            ans = min(ans + count[num], num)
        return ans


def main() -> None:
    """1846. Maximum Element After Decreasing and Rearranging on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [2, 2, 1, 2, 1]
        >>> example_case_2 = [100,1,1000]
        >>> example_case_3 = [1,2,3,4,5]

    Example 1:
        >>> sol.maximumElementAfterDecrementingAndRearranging(example_case_1)
        2
        >>> sol.maximumElementAfterDecrementingAndRearrangingNoSort(example_case_1)
        2

    Example 2:
        >>> sol.maximumElementAfterDecrementingAndRearranging(example_case_2)
        3
        >>> sol.maximumElementAfterDecrementingAndRearrangingNoSort(example_case_2)
        3

    Example 3:
        >>> sol.maximumElementAfterDecrementingAndRearranging(example_case_3)
        5
        >>> sol.maximumElementAfterDecrementingAndRearrangingNoSort(example_case_3)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
