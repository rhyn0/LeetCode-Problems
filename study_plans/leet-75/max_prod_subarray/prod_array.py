# Standard Library
import doctest


class Solution:  # noqa: D101
    def maxProduct(self, nums: list[int]) -> int:  # spec
        """Return greatest product of subarray given an array.

        Need to track a decreasing streak,
        an increasing streak and the greatest maximum seen.

        Args:
            nums (List[int]): Given array

        Returns:
            int: greatest product
        """
        if not nums:
            return 0
        result, curr_max, curr_min = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            curr_max, curr_min = max(num, curr_max * num, curr_min * num), min(
                num,
                curr_max * num,
                curr_min * num,
            )
            result = max(result, curr_max)
        return result


def main() -> None:
    """Maximum Product Subarray on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.maxProduct([2, 3, -2, 4])
        6

    Example 2:
        >>> sol.maxProduct([-2,0,-1])
        0

    Test 1:
        >>> sol.maxProduct([-4, -3, -2])
        12
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
