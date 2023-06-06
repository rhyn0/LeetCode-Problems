# Standard Library
import doctest
from itertools import cycle


class Solution:  # noqa: D101
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """Given a 2D matrix, return it flattened in spiral order.

        Spiral order goes right, down, left, up starting from upper left corner.

        Args:
            matrix (List[List[int]]): Matrix given

        Returns:
            List[int]: Flattened matrix in spiral order
        """
        seen_set = set()

        def horizontal(x: int, y: int, step: int) -> tuple[list[int], int, int]:
            temp_list = []
            while 0 <= x < len(matrix[0]) and (x, y) not in seen_set:
                temp_list.append(matrix[y][x])
                seen_set.add((x, y))
                x += step
            return temp_list, x - step, y + step

        def vertical(x: int, y: int, step: int) -> tuple[list[int], int, int]:
            temp_list = []
            while 0 <= y < len(matrix) and (x, y) not in seen_set:
                temp_list.append(matrix[y][x])
                seen_set.add((x, y))
                y += step
            return temp_list, x - step, y - step

        i, j, step = 0, 0, 1
        ret_list = []
        for func in cycle((horizontal, vertical)):
            if len(seen_set) == (len(matrix) * len(matrix[0])):
                break
            val = func(i, j, step)
            ret_list.extend(val[0])
            i, j = val[1:]
            if func is vertical:
                step *= -1
        return ret_list


def main() -> None:
    """Problem Name on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> example_case_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    Example 1:
        >>> sol.spiralOrder(example_case_1)
        [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Example 2:
        >>> sol.spiralOrder(example_case_2)
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
