"""Daily Challenge for April 2, 2023."""

# Standard Library
import bisect
import doctest
from math import ceil
from operator import itemgetter


class Solution:  # noqa: D101
    @staticmethod
    def find_insertion(array: list[int], target: int) -> int:
        """Return lower bound index of where to insert `target` into `array`."""
        left, right = 0, len(array)
        while left < right:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid

        # modified from normal binary search because we don't need exact match
        return left if left < len(array) else -1

    def successfulPairs(
        self,
        spells: list[int],
        potions: list[int],
        success: int,
    ) -> list[int]:
        """Return number of spell and potion pairs that are strong enough.

        Strength for each potion and spell is the integer value in the provided
        array. A pairing between potion and spell is strong enough if it is greater
        than the provided `success`.

        Args:
            spells (list[int]): Strengths of the ith spell
            potions (list[int]): Strengths of a the ith potion
            success (int): Minimum strength to be successful pair

        Returns:
            list[int]: For each spell, the number of pairs that are successful
        """
        success_pairs = []
        num_potions = len(potions)
        potions.sort()
        for spell_strength in spells:
            min_potion_strength = ceil(success / spell_strength)
            insert_idx = self.find_insertion(potions, min_potion_strength)
            success_pairs.append((num_potions - insert_idx) if insert_idx != -1 else 0)

        return success_pairs

    def successfulPairsBuilt(
        self,
        spells: list[int],
        potions: list[int],
        success: int,
    ) -> list[int]:
        """Return same as above using `bisect` to find insertion point."""
        num_potions = len(potions)
        potions.sort()
        return [
            (
                (num_potions - insert_idx)
                if (
                    insert_idx := bisect.bisect_left(
                        potions,
                        ceil(success / spell_strength),
                    )
                )
                != -1
                else 0
            )
            for spell_strength in spells
        ]

    def successfulPairsTwo(
        self,
        spells: list[int],
        potions: list[int],
        success: int,
    ) -> list[int]:
        """Return same as above but using a two pointer method."""
        num_potions = len(potions)
        potions.sort()
        # have to map sorted indices back to original
        sorted_spells = sorted(enumerate(spells), key=itemgetter(1))
        success_pairs = [0] * len(spells)
        curr_potion_idx = num_potions - 1
        for orig_index, spell in sorted_spells:
            while curr_potion_idx >= 0 and spell * potions[curr_potion_idx] >= success:
                curr_potion_idx -= 1
            success_pairs[orig_index] = num_potions - curr_potion_idx - 1
        return success_pairs


def main() -> None:
    """2300. Successful Pairs of Spells and Potions on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([5,1,3], [1,2,3,4,5], 7)
        >>> example_case_2 = ([3,1,2], [8,5,8], 16)
        >>> test_case_1 = ([5], [1, 1, 1, 1], 3)

    Example 1:
        >>> sol.successfulPairs(*example_case_1)
        [4, 0, 3]
        >>> sol.successfulPairsBuilt(*example_case_1)
        [4, 0, 3]
        >>> sol.successfulPairsTwo(*example_case_1)
        [4, 0, 3]

    Example 2:
        >>> sol.successfulPairs(*example_case_2)
        [2, 0, 2]
        >>> sol.successfulPairsBuilt(*example_case_2)
        [2, 0, 2]
        >>> sol.successfulPairsTwo(*example_case_2)
        [2, 0, 2]

    Test 1:
        >>> sol.successfulPairs(*test_case_1)
        [4]
        >>> sol.successfulPairsBuilt(*test_case_1)
        [4]
        >>> sol.successfulPairsTwo(*test_case_1)
        [4]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
