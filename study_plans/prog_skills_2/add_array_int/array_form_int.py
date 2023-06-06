# Standard Library
import doctest
from itertools import zip_longest


class Solution:  # noqa: D101
    def addToArrayForm(self, num: list[int], addend: int) -> list[int]:
        """Add integer ``k`` to array form integer, return answer in array form.

        Array form shows MSB left to right.

        Args:
            num (List[int]): Number in array format
            addend (int): integer to add

        Returns:
            List[int]: Answer of addition in array format
        """
        ret_list, carry = [], 0
        for num_i, k_i in zip_longest(
            reversed(num),
            reversed(str(addend)),
            fillvalue="0",
        ):
            total = int(num_i) + int(k_i) + carry

            carry, total = divmod(total, 10)  # this is cool
            ret_list.append(total)

        if carry:
            ret_list.append(carry)

        return ret_list[::-1]


def main() -> None:
    """989. Add to Array-Form of Integer on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1, 2, 0, 0], 34
        >>> example_case_2 = [2, 7, 4], 181
        >>> example_case_3 = [2, 1, 5], 806
        >>> test_case_1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1

    Example 1:
        >>> sol.addToArrayForm(*example_case_1)
        [1, 2, 3, 4]

    Example 2:
        >>> sol.addToArrayForm(*example_case_2)
        [4, 5, 5]

    Example 3:
        >>> sol.addToArrayForm(*example_case_3)
        [1, 0, 2, 1]

    Test 1:
        >>> sol.addToArrayForm(*test_case_1)
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
