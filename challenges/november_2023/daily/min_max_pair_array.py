"""Daily Challenge for November 17 on LeetCode: Problem #1877 [Medium]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def minPairSum(self, nums: list[int]) -> int:
        """Return the minimum possible maximum pair sum.

        Maximum pair sum is the maximum of all pairs of `nums` elements.
        Each number in `nums` must be used exactly once.

        Args:
            nums (list[int]): Even length array of numbers to use

        Returns:
            int: The minimum value of the maximum pair sum
        """
        arranged = sorted(nums)
        # value of each num in nums is positive >=0
        max_pair_sum = 0
        left, right = 0, len(arranged) - 1
        while left < right:
            max_pair_sum = max(max_pair_sum, arranged[left] + arranged[right])
            left += 1
            right -= 1
        return max_pair_sum


def main() -> None:
    """1877. Minimize Maximum Pair Sum in Array on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [3,5,2,3]
        >>> example_case_2 = [3,5,4,2,4,6]
        >>> self_test_1 = [3,6,4,2,4,6]
        >>> test_case_1 = [4,1,5,1,2,5,1,5,5,4]

    Example 1:
        >>> sol.minPairSum(example_case_1)
        7

    Example 2:
        >>> sol.minPairSum(example_case_2)
        8

    Self Test 1:
        >>> sol.minPairSum(self_test_1)
        9

    Test 1:
        >>> sol.minPairSum(test_case_1)
        8
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
