"""Daily Challenge for June 24, 2023 on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def tallestBillboard(self, rods: list[int]) -> int:
        """Return tallest billboard possible given rod heights.

        Billboard must be level to be put up.
        Minimize the difference between the two distinct subsets
        of rods to be 0.

        Args:
            rods (list[int]): available rod heights

        Returns:
            int: Tallest billboard possible, 0 if no answers
        """
        diff_dict = {0: 0}
        for rod in rods:
            # ignore adding `rod` case is covered by this
            # have to do this also due to Python dictionary iteration rules
            new_dict = diff_dict.copy()
            for diff, tall_rod in diff_dict.items():
                short_rod = tall_rod - diff
                # add to tall side
                new_dict[diff + rod] = max(new_dict.get(diff + rod, 0), tall_rod + rod)

                # add rod to short side
                new_diff = abs(tall_rod - short_rod - rod)
                new_taller = max(short_rod + rod, tall_rod)
                new_dict[new_diff] = max(new_dict.get(new_diff, 0), new_taller)
            diff_dict = new_dict

        return diff_dict.get(0, 0)


def main() -> None:
    """956. Tallest Billboard on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,2,3,6]
        >>> example_case_2 = [1,2,3,4,5,6]
        >>> example_case_3 = [1,2]
        >>> self_test_1 = [3,3]

    Example 1:
        >>> sol.tallestBillboard(example_case_1)
        6

    Example 2:
        >>> sol.tallestBillboard(example_case_2)
        10

    Example 3:
        >>> sol.tallestBillboard(example_case_3)
        0

    Self Test 1:
        >>> sol.tallestBillboard(self_test_1)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
