# Standard Library
import doctest


class Solution:  # noqa: D101
    def findRotation(  # spec
        self,
        mat: list[list[int]],
        target: list[list[int]],
    ) -> bool:
        """Return whether matrix can be rotated to match target.

        Args:
            mat (List[List[int]]): Original matrix
            target (List[List[int]]): End matrix to make

        Returns:
            bool: True if possible, False otherwise
        """

        def rotate(targ_copy: list[list[int]]) -> list[list[int]]:
            n_size = len(targ_copy)
            for row in range(n_size):
                for col in range(row + 1, n_size):
                    targ_copy[row][col], targ_copy[col][row] = (
                        targ_copy[col][row],
                        targ_copy[row][col],
                    )
                targ_copy[row].reverse()
            return targ_copy

        # mat_copy = deepcopy(mat)
        if mat == target:
            return True
        for _ in range(3):
            mat = rotate(mat)
            if mat == target:
                return True

        return False


def main() -> None:
    """1886. Determine Whether Matrix Can Be Obtained By Rotation on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[0, 1], [1, 0]], [[1, 0], [0, 1]]
        >>> example_case_2 = [[0, 1], [1, 1]], [[1, 0], [0, 1]]
        >>> example_case_3 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]],\
            [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
        >>> test_case_1 = [[1]], [[0]]

    Example 1:
        >>> sol.findRotation(*example_case_1)
        True

    Example 2:
        >>> sol.findRotation(*example_case_2)
        False

    Example 3:
        >>> sol.findRotation(*example_case_3)
        True

    Test 1:
        >>> sol.findRotation(*test_case_1)
        False
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
