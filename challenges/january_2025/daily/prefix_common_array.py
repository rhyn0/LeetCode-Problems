"""Daily Challenge for January 14, 2025.

2657. Find the Prefix Common Array of Two Arrays on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [1,3,2,4], [3,1,2,4]
    >>> example_case_2 = [2,3,1], [3,1,2]

Example 1:
    >>> sol.findThePrefixCommonArray(*example_case_1)
    [0, 2, 3, 4]

Example 2:
    >>> sol.findThePrefixCommonArray(*example_case_2)
    [0, 1, 3]
"""


class Solution:  # noqa: D101
    def findThePrefixCommonArray(
        self,
        A: list[int],  # noqa: N803
        B: list[int],  # noqa: N803
    ) -> list[int]:
        """Return the prefix common array of the two given permutation lists.

        The permutation list contains all numbers from 1 to `n` in some order.
        Common array is the number of common elements at or before index `i` of
        both `A` and `B`.

        Args:
            A (list[int]): Permutation list one
            B (list[int]): Permutation list two

        Returns:
            list[int]: Prefix common array of lengths
        """
        answer = []
        n = len(A)
        # notice that this is length n, max index of n - 1. So we need to -1 values
        seen_values = [0] * n
        common_values = 0
        for i in range(n):
            seen_values[A[i] - 1] += 1
            if seen_values[A[i] - 1] == 2:  # noqa: PLR2004
                common_values += 1

            seen_values[B[i] - 1] += 1
            if seen_values[B[i] - 1] == 2:  # noqa: PLR2004
                common_values += 1
            answer.append(common_values)
        return answer
