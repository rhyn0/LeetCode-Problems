"""Essentials of Dynamic Programming LIS problem on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """Return length of longest chain of pairs.

        Pairs must be of form [left, right] where left < right.
        A chain is created by combining two pairs together,
        where pair_i precedes pair_j and the condition of
        right_i < left_j is fulfilled.

        Args:
            pairs (list[list[int]]): List of pairs

        Returns:
            int: Length
        """
        # sort the pairs by leading value first
        pairs.sort()
        lis = [pairs[0]]
        for pair in pairs[1:]:
            # either a pair is valid to chain with
            if pair[0] > lis[-1][1]:
                lis.append(pair)
            # or the pair reduces the value of the LIS right chain
            # which increases valid pair space
            elif pair[1] < lis[-1][1]:
                lis[-1] = pair
        return len(lis)


def main() -> None:
    """646. Maximum Length of Pair Chain on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1,2],[2,3],[3,4]]
        >>> example_case_2 = [[1,2],[7,8],[4,5]]
        >>> test_case_1 = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]

    Example 1:
        >>> sol.findLongestChain(example_case_1)
        2

    Example 2:
        >>> sol.findLongestChain(example_case_2)
        3

    Test 1:
        >>> sol.findLongestChain(test_case_1)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
