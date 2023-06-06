# Standard Library
import doctest
from itertools import product


class Solution:  # noqa: D101
    ROW_MAX, COL_MAX = 0, 0

    def dfs(self, board: list[list[str]], row: int, col: int) -> None:
        """Depth First Search the board to change O's."""
        if board[row][col] != "O":
            return
        board[row][col] = "E"
        if row < self.ROW_MAX - 1:
            self.dfs(board, row + 1, col)
        if row > 0:
            self.dfs(board, row - 1, col)
        if col < self.COL_MAX - 1:
            self.dfs(board, row, col + 1)
        if col > 0:
            self.dfs(board, row, col - 1)

    def solve(self, board: list[list[str]]) -> None:
        """Modify board to capture surrounded 'O's.

        Will modify board in place

        Args:
            board (List[List[str]]): Board of X's and O's.
        """
        self.ROW_MAX, self.COL_MAX = len(board), len(board[0])

        border = list(product(range(self.ROW_MAX), (0, self.COL_MAX - 1))) + list(
            product((0, self.ROW_MAX - 1), range(self.COL_MAX)),
        )
        for b_row, b_col in border:
            self.dfs(board, b_row, b_col)

        for row in range(self.ROW_MAX):
            for col in range(self.COL_MAX):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "E":
                    board[row][col] = "O"


def main() -> None:
    """Surrounded Regions on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",\
            "X","X"]]
        >>> sol.solve(board)
        >>> print(board)
        [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', \
            'X', 'X']]

    Example 2:
        >>> board = [["X"]]
        >>> sol.solve(board)
        >>> print(board)
        [['X']]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
