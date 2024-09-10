"""Daily Challenge for November 18 on LeetCode: Problem #1838 [Medium]."""

# Standard Library
import doctest
from itertools import accumulate


class Solution:  # noqa: D101
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """Return the maximum frequency of any element in `nums` after ops.

        The only operation available is to increment any element by 1.
        Can only use up to `k` operations on the entire list.

        Args:
            nums (list[int]): Starting list for the elements
            k (int): Max number of operations that can be performed

        Returns:
            int: Frequency of the most frequent element after operations
        """
        arranged = sorted(nums)
        window_sum = 0
        back = 0
        n = len(arranged)
        for front in range(n):
            window_sum += arranged[front]
            target_val = arranged[front]

            # number of operations to turn all values into target_val
            if (front - back + 1) * target_val - window_sum > k:
                # using more operations than allowed
                # reduce the size of the window by 1
                # this preserves the maximum window length
                # without another variable
                window_sum -= arranged[back]
                back += 1

        return n - back

    def maxFrequencyBinSearch(self, nums: list[int], k: int) -> int:
        """Return same as above using binary search.

        Impractical solution but kind of interesting to think about this way.
        """
        arranged = sorted(nums)
        prefix = list(accumulate(arranged))

        def find_left_edge(idx: int) -> int:
            left, right = 0, idx
            # best candidate for left most edge of the frequency window
            best = idx
            target_val = arranged[idx]
            while left <= right:
                mid = (left + right) // 2
                count = idx - mid + 1
                final_sum = count * target_val
                # mid could be 0, so prefix[mid - 1] is invalid
                original_sum = prefix[idx] - prefix[mid] + arranged[mid]
                operations_required = final_sum - original_sum

                if operations_required > k:
                    # too many operations required
                    # best left edge must be greater
                    left = mid + 1
                else:
                    best = mid
                    right = mid - 1
            return idx - best + 1

        return max(find_left_edge(idx) for idx in range(len(arranged)))


def main() -> None:
    """1838. Frequency of the Most Frequent Element on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,2,4], 5
        >>> example_case_2 = [1,4,8,13], 5
        >>> example_case_3 = [3,9,6], 2
        >>> self_test_1 = [3,3], 1

    Example 1:
        >>> sol.maxFrequency(*example_case_1)
        3
        >>> sol.maxFrequencyBinSearch(*example_case_1)
        3

    Example 2:
        >>> sol.maxFrequency(*example_case_2)
        2
        >>> sol.maxFrequencyBinSearch(*example_case_2)
        2

    Example 3:
        >>> sol.maxFrequency(*example_case_3)
        1
        >>> sol.maxFrequencyBinSearch(*example_case_3)
        1

    Self Test 1:
        >>> sol.maxFrequency(*self_test_1)
        2
        >>> sol.maxFrequencyBinSearch(*self_test_1)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
