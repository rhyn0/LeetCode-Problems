"""Weekly Challenge #2 of April 2023."""
# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Return mapping of nums1 values to indices in nums2.

        ``nums2`` is guaranteed to be an anagram of ``nums1``.
        Handle duplicates gracefully and only allow one-to-one mappings

        Args:
            nums1 (list[int]): Original list to map from
            nums2 (list[int]): Destination list, anagram of original

        Returns:
            list[int]: Indices to map original numbers to
        """
        idx_possib = defaultdict(list)
        for idx, val in enumerate(nums2):
            idx_possib[val].append(idx)

        return [idx_possib[val].pop() for val in nums1]

    def anagramMappingsManyOne(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Return answer to problem allowing many-to-one mappings."""
        idx_mapping = {val: idx for idx, val in enumerate(nums2)}
        return [idx_mapping[val] for val in nums1]

    def anagramMappingsBrute(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Return similar answer as above using brute force.

        Will return first index of mappings, instead of last for duplicates.
        """
        return [nums2.index(val) for val in nums1]


def main() -> None:
    """Find Anagram Mappings on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([12,28,46,32,50], [50,12,32,46,28])
        >>> example_case_2 = ([84,46], [84,46])
        >>> test_case_1 = ([1, 1], [1, 1])

    Example 1:
        >>> sol.anagramMappings(*example_case_1)
        [1, 4, 3, 2, 0]
        >>> sol.anagramMappingsManyOne(*example_case_1)
        [1, 4, 3, 2, 0]
        >>> sol.anagramMappingsBrute(*example_case_1)
        [1, 4, 3, 2, 0]

    Example 2:
        >>> sol.anagramMappings(*example_case_2)
        [0, 1]
        >>> sol.anagramMappingsManyOne(*example_case_2)
        [0, 1]
        >>> sol.anagramMappingsBrute(*example_case_2)
        [0, 1]

    Test 1:
        >>> sol.anagramMappings(*test_case_1)
        [1, 0]
        >>> sol.anagramMappingsManyOne(*test_case_1)
        [1, 1]
        >>> sol.anagramMappingsBrute(*test_case_1)
        [0, 0]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
