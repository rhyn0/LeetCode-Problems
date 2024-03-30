"""Daily Challenge for June 23, 2023 on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestArithSeqLength(self, nums: list[int]) -> int:
        """Return length of longest arithmetic subsequence in `nums`.

        Args:
            nums (list[int]): array to search for subsequence

        Returns:
            int: length of longest subsequence
        """
        subseq_at_point_of_diff: dict[tuple[int, int], int] = {}
        for right, val in enumerate(nums):
            for left in range(right):
                diff = val - nums[left]
                # default case is 1 + 1, because a subsequence exists between
                # left and right
                subseq_at_point_of_diff[(right, diff)] = (
                    subseq_at_point_of_diff.get((left, diff), 1) + 1
                )
        return max(subseq_at_point_of_diff.values())


def main() -> None:
    """1027. Longest Arithmetic Subsequence on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [3,6,9,12]
        >>> example_case_2 = [9,4,7,2,10]
        >>> example_case_3 = [20,1,15,3,10,5,8]

    Example 1:
        >>> sol.longestArithSeqLength(example_case_1)
        4

    Example 2:
        >>> sol.longestArithSeqLength(example_case_2)
        3

    Example 3:
        >>> sol.longestArithSeqLength(example_case_3)
        4
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
