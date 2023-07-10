"""Daily Challenge for July 5, 2023 on LeetCode."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestSubarray(self, nums: list[int]) -> int:
        """Return longest subarray of 1's after deleting one index.

        Array is made up of only 1s and 0s.

        Args:
            nums (list[int]): Array to parse through

        Returns:
            int: Length of the subarray.
        """
        left = right = 0
        best_len = 0
        deleted_idx = -1
        n = len(nums)
        while right < n:
            if nums[right] != 1:
                if deleted_idx != -1:
                    left = deleted_idx + 1
                deleted_idx = right
            right += 1
            best_len = max(best_len, right - left - 1)
            # print(f"{best_len=} in [{left}, {right})")

        return best_len

    def longestSubarrayDP(self, nums: list[int]) -> int:
        """Return same as above using more space."""
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i, val in enumerate(nums[:-1], start=1):
            if val == 1:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1
        return max(sum(item) for item in zip(left, right, strict=True))


def main() -> None:
    """1493. Longest Subarray of 1's After Deleting One Element on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,1,0,1]
        >>> example_case_2 = [0,1,1,1,0,1,1,0,1]
        >>> example_case_3 = [1,1,1]

    Example 1:
        >>> sol.longestSubarray(example_case_1)
        3
        >>> sol.longestSubarrayDP(example_case_1)
        3

    Example 2:
        >>> sol.longestSubarray(example_case_2)
        5
        >>> sol.longestSubarrayDP(example_case_2)
        5

    Example 3:
        >>> sol.longestSubarray(example_case_3)
        2
        >>> sol.longestSubarrayDP(example_case_3)
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
