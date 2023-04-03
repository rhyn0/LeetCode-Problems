# Standard Library
import doctest
from itertools import pairwise
from itertools import product


class Solution:  # noqa: D101
    DIRS = (0, 1, 0, -1, 0)

    def exist(self, board: list[list[str]], word: str) -> bool:
        """Return if word exists in the word search board.

        Word can exist in any combination of horizontal and vertical moves.

        Args:
            board (List[List[str]]): word search
            word (str): word to search for

        Returns:
            bool: True if it exists, False otherwise
        """
        size_n, size_m = len(board), len(board[0])

        def backtrack(curr_row: int, curr_col: int, suffix: str) -> bool:
            if len(suffix) == 0:
                return True
            if (
                curr_row < 0
                or curr_row >= size_n
                or curr_col < 0
                or curr_col >= size_m
                or board[curr_row][curr_col] != suffix[0]
            ):
                return False
            board[curr_row][curr_col] = "$"
            for d_row, d_col in pairwise(self.DIRS):
                new_row, new_col = curr_row + d_row, curr_col + d_col
                if backtrack(new_row, new_col, suffix[1:]):
                    return True
            board[curr_row][curr_col] = suffix[0]
            return False

        return any(
            backtrack(row, col, word)
            for row, col in product(range(size_n), range(size_m))
        )


def main():
    """Word Search on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
        True

    Example 2:
        >>> sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
        True

    Example 3:
        >>> sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
        False

    Test 1:
        >>> sol.exist([["a"]], "a")
        True

    Test 2:
        >>> sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],\
            "ABCEFSADEESE")
        True

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
