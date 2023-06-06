# Standard Library
import doctest


class Solution:  # noqa: D101
    def kthSmallest(self, matrix: list[list[int]], kth: int) -> int:  # spec
        """Return the ``kth`` smallest element in a sorted matrix.

        The matrix is sorted in each row and column. That is each row
        and column is guaranteed to be in non-decreasing order.
        But each row and column have no guaranteed relation to the other.

        Args:
            matrix (List[List[int]]): "Sorted" matrix
            kth (int): 1 indexed smallest number.

        Returns:
            int: kth smallest element in matrix
        """
        matrix_size = len(matrix)

        def count_left_array(mid_value: int) -> tuple[int, int, int]:
            count = 0
            # start in bottom left
            row, col = matrix_size - 1, 0
            lower, higher = matrix[0][0], matrix[-1][-1]
            while row >= 0 and col < matrix_size:
                # move right if cell in column is less than mid
                # move up if cell in column greater than mid
                if matrix[row][col] > mid_value:
                    higher = min(higher, matrix[row][col])
                    row -= 1
                else:
                    lower = max(lower, matrix[row][col])
                    # if current cell is less than mid
                    # then everything above is also less
                    count += row + 1
                    col += 1
            return count, lower, higher

        low, high = matrix[0][0], matrix[-1][-1]
        # since values are not unique, could be a range of just one value
        while low < high:
            mid = (low + high) // 2
            count, small, large = count_left_array(mid)

            if count == kth:
                return small

            if count < kth:
                low = large
            else:
                high = small
        return low


def main() -> None:
    """Kth Smallest Element in a Sorted Matrix on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
        13

    Example 2:
        >>> sol.kthSmallest([[-5]], 1)
        -5

    Test 1:
        >>> sol.kthSmallest([[1,2],[1,3]], 2)
        1

    Test 2:
        >>> sol.kthSmallest([[1,2],[3,3]], 2)
        2

    Test 3:
        >>> sol.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 2)
        3
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
