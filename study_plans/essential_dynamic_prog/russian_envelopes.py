"""Essentials of Dynamic Programming LIS Problem on LeetCode."""

# Standard Library
from bisect import bisect_left
import doctest


class Solution:  # noqa: D101
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """Return longest increasing sequence of envelopes.

        An envelope is defined as a list of [height, width] and the constraint
        is that previous envelopes in the sequence need to fit inside
        the later envelopes in both dimensions.

        Args:
            envelopes (list[list[int]]): Array of envelopes, order irrelevant

        Returns:
            int: Length of longest subsequence of envelopes
        """
        # will sort by leading element and tie break using second element
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        subseq_w = [envelopes[0][1]]
        for _, width in envelopes[1:]:
            if width > subseq_w[-1]:
                subseq_w.append(width)
            else:
                alter_idx = bisect_left(subseq_w, width)
                subseq_w[alter_idx] = width

        return len(subseq_w)


def main() -> None:
    """354. Russian Doll Envelopes on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[5,4],[6,4],[6,7],[2,3]]
        >>> example_case_2 = [[1,1],[1,1],[1,1]]
        >>> test_case_1 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],\
                [6,360],[7,380]]

    Example 1:
        >>> sol.maxEnvelopes(example_case_1)
        3

    Example 2:
        >>> sol.maxEnvelopes(example_case_2)
        1

    Test 1:
        >>> sol.maxEnvelopes(test_case_1)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
