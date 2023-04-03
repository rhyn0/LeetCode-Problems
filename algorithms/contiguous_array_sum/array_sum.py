# Standard Library
import doctest


class Solution:  # noqa: D101
    def checkSubarraySum(self, nums: list[int], target_sum: int) -> bool:
        """Return if a subarray that sums to `target_sum` exists.

        Must be a contiguous subarray.

        Args:
            nums (List[int]): List of numbers to use to construct subarray
            target_sum (int): number to sum the subarray to

        Returns:
            bool: True if subarray exists, False otherwise
        """
        prefix_sum = 0
        previous_mod = {0: 0}
        for index, val in enumerate(nums):
            prefix_sum += val
            curr_mod = prefix_sum % target_sum

            if curr_mod not in previous_mod:
                previous_mod[curr_mod] = (
                    index + 1
                )  # a subarray from this spot must be after i + 1
            elif previous_mod[curr_mod] < index:
                return True

        return False


def main():
    """Contiguous Subarray Sum on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.checkSubarraySum([23,2,4,6,7], 6)
        True

    Example 2:
        >>> sol.checkSubarraySum([23,2,6,4,7], 6)
        True

    Example 3:
        >>> sol.checkSubarraySum([23,2,6,4,7], 13)
        False

    Test 1:
        >>> sol.checkSubarraySum([23,2,4,6,6], 7)
        True

    Test 2:
        >>> sol.checkSubarraySum([1, 2, 12], 6)
        False

    Test 3:
        >>> sol.checkSubarraySum([0], 1)
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
