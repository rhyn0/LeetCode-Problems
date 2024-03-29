# Standard Library
import doctest


class Solution:  # noqa: D101
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Search a 2d matrix for target value.

        Each row of matrix is sorted.
        Values in later rows are all greater than those above.

        Args:
            matrix (List[List[int]]): Matrix of sorted values
            target (int): Target to find

        Returns:
            bool: True if target exists in matrix
        """
        n_size = len(matrix)
        low, high = 0, n_size - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return target in matrix[mid]

            if target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        return False


def main() -> None:
    """Search a 2D Matrix on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
        True

    Example 2:
        >>> sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
