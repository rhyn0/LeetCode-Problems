"""Daily Challenge on LeetCode for October 31: Problem #2433 [Medium]."""
# Standard Library
import doctest
from itertools import pairwise


class Solution:  # noqa: D101
    def findArray(self, pref: list[int]) -> list[int]:
        """Return the original array of numbers.

        Given an array of prefix XOR numbers, i.e. pref[i] = arr[0] ^ ... ^ arr[i].
        """
        return [pref[0], *[num1 ^ num2 for num1, num2 in pairwise(pref)]]

    def findArraySpaceOptimized(self, pref: list[int]) -> list[int]:
        """Return the same as above using space optimized in place XOR."""
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref


def main() -> None:
    """2433. Find The Original Array of Prefix Xor on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [5,2,0,3,1]
        >>> example_case_2 = [13]

    Example 1:
        >>> sol.findArray(example_case_1)
        [5, 7, 2, 3, 2]
        >>> sol.findArraySpaceOptimized(example_case_1.copy())
        [5, 7, 2, 3, 2]

    Example 2:
        >>> sol.findArray(example_case_2)
        [13]
        >>> sol.findArraySpaceOptimized(example_case_2.copy())
        [13]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
