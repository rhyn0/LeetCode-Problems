"""Daily Challenge for July 4, 2023 on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def singleNumber(self, nums: list[int]) -> int:
        """Return element that is only present once in array.

        Every element in array is repeated 3 times
        except for one element.

        Args:
            nums (list[int]): Array of nums with proper repetition

        Returns:
            int: Lone element
        """
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = (seen_once ^ num) & ~seen_twice
            seen_twice = (seen_twice ^ num) & ~seen_once

        return seen_once

    def singleNumberMath(self, nums: list[int]) -> int:
        """Return same as above using math."""
        # proof is that set of nums S = {x_1, x_2, ... x_k, y}
        # where each x number is repeated 3 times in `nums`.
        # So sum of this set is just x_1 + x_2 ... + x_k + y
        # or also SUM - y = x_1 + x_2 ... + x_k
        # so our SUM_nums = 3 * SUM - 2y
        # y = (3 * SUM - SUM_nums) / 2
        return (3 * sum(set(nums)) - sum(nums)) // 2


def main() -> None:
    """137. Single Number II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [2,2,3,2]
        >>> example_case_2 = [0,1,0,1,0,1,99]

    Example 1:
        >>> sol.singleNumber(example_case_1)
        3
        >>> sol.singleNumberMath(example_case_1)
        3

    Example 2:
        >>> sol.singleNumber(example_case_2)
        99
        >>> sol.singleNumberMath(example_case_2)
        99
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
