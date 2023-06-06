# Standard Library
import doctest


class Solution:  # noqa: D101
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """Return number of contiguous subarrays whose product is less than k.

        Strictly less than k

        Args:
            nums (List[int]): Array of numbers to create subarrays from
            k (int): maximum number

        Returns:
            int: Number of subarrays that match condition
        """
        if k <= 1:
            return 0
        left = ret_count = 0
        prod = 1
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ret_count += right - left + 1
        return ret_count


def main() -> None:
    """Problem Name on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [10, 5, 2, 6], 100
        >>> example_case_2 = [1, 2, 3], 0
        >>> test_case_1 = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3],19

    Example 1:
        >>> sol.numSubarrayProductLessThanK(*example_case_1)
        8

    Example 2:
        >>> sol.numSubarrayProductLessThanK(*example_case_2)
        0

    Test 1:
        >>> sol.numSubarrayProductLessThanK(*test_case_1)
        18
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
