# Standard Library
import doctest


class Solution:  # noqa: D101
    def minimumAverageDistance(self, nums: list[int]) -> int:  # spec
        """Return index of minimum average distance.

        Average distance for index 'i' in the given array is calculated as
        absolute difference - rounded down to integer -
        between the average of the first 'i + 1' elements and then average
        of the remaining elements.

        Args:
            nums (List[int]): Input array

        Returns:
            int: Index of minimum, -1 if nums is empty
        """

        def _escape_zero(numer: int, denom: int) -> int:
            if denom == 0:
                # only want to escape 0 / 0
                return 0
            return numer // denom

        start_sum, n_len = sum(nums), len(nums)
        run_sum = 0
        min_val, min_index = float("inf"), -1
        for i, val in enumerate(nums, start=1):
            run_sum += val
            added_val = abs(
                _escape_zero(run_sum, i) - _escape_zero(start_sum - run_sum, n_len - i)
            )
            if added_val < min_val:
                min_val = added_val
                min_index = i - 1

        return min_index


def main():
    """Average Minimum Distance on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.minimumAverageDistance([2,5,3,9,5,3])
        3

    Example 2:
        >>> sol.minimumAverageDistance([0])
        0
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
