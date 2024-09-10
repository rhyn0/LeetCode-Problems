"""Essentials of Dynamic Programming LIS Problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def findNumberOfLIS(self, nums: list[int]) -> int:
        """Return frequency of longest increasing subsequence length.

        Args:
            nums (list[int]): Array to create LIS from

        Returns:
            int: Frequency
        """
        n = len(nums)
        # every point starts at itself
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # valid previous state, append i to this LIS
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    # encountered another valid previous state,
                    # update count to use this one too
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_len = max(length)
        return sum(count[k] for k in range(n) if length[k] == max_len)


def main() -> None:
    """673. Number of Longest Increasing Subsequence on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,3,5,4,7]
        >>> example_case_2 = [2,2,2,2,2]

    Example 1:
        >>> sol.findNumberOfLIS(example_case_1)
        2

    Example 2:
        >>> sol.findNumberOfLIS(example_case_2)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
