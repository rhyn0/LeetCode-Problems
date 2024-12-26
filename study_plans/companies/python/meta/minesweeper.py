"""Meta Interview Question Practice List on LeetCode.

529. Minesweeper on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3,0]
    >>> example_case_2 = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], [1,2]

Example 1:
    >>> sol.updateBoard(*example_case_1)
    [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    >>> sol.updateBoardDfs(*example_case_1)
    [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]

Example 2:
    >>> sol.updateBoard(*example_case_2)
    [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    >>> sol.updateBoardDfs(*example_case_2)
    [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
"""  # noqa: E501

# Standard Library
from collections import deque
from collections.abc import Iterator
from typing import ClassVar


class Solution:  # noqa: D101
    directions: ClassVar = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def updateBoard(
        self,
        board: list[list[str]],
        click: list[int],
    ) -> list[list[str]]:
        """Play a singular click of the game minesweeper.

        Args:
            board (list[list[str]]): Current board state for Minesweeper
            click (list[int]): [row, col] representation of the next click

        Returns:
            list[list[str]]: The new board state
        """
        # adjacency is calculated for 8 squares around us. While on board
        n, m = len(board), len(board[0])

        def neighbors(row: int, col: int) -> Iterator[tuple[int, int]]:
            for drow, dcol in self.directions:
                if (
                    (drow == 0 and dcol == 0)
                    or not (0 <= row + drow < n)
                    or not (0 <= col + dcol < m)
                ):
                    continue
                yield (row + drow, col + dcol)

        # personal choice to not modify the input arguments,
        # removing this copy speeds it up considerably.
        return_board = [row[:] for row in board]
        que: deque[tuple[int, int]] = deque([tuple(click)])
        while que:
            curr_click_row, curr_click_col = que.popleft()
            # determine action for current click
            # if it is a bomb, we return early
            if return_board[curr_click_row][curr_click_col] == "M":
                return_board[curr_click_row][curr_click_col] = "X"
                return return_board
            if return_board[curr_click_row][curr_click_col] == "E":
                # have to calculate if squares nearby are mines or not
                num_mines = sum(
                    return_board[neighbor_row][neighbor_col] == "M"
                    for neighbor_row, neighbor_col in neighbors(
                        curr_click_row,
                        curr_click_col,
                    )
                )
                if num_mines == 0:
                    return_board[curr_click_row][curr_click_col] = "B"
                    que.extend(
                        neighbor
                        for neighbor in neighbors(curr_click_row, curr_click_col)
                        if return_board[neighbor[0]][neighbor[1]] == "E"
                    )
                else:
                    return_board[curr_click_row][curr_click_col] = str(num_mines)

        return return_board

    def updateBoardDfs(
        self,
        board: list[list[str]],
        click: list[int],
    ) -> list[list[str]]:
        """Return same as above using DFS methodology."""
        n, m = len(board), len(board[0])
        # don't modify input arguments
        return_board = [row[:] for row in board]
        # handle first click is Mine separately
        if return_board[click[0]][click[1]] == "M":
            return_board[click[0]][click[1]] = "X"
            return return_board

        def dfs(row: int, col: int) -> bool:
            """Return whether square was mine or not."""
            if not (0 <= row < n and 0 <= col < m):
                # off board
                return False
            if return_board[row][col] == "M":
                return True

            if return_board[row][col] == "E":
                num_mines = sum(
                    return_board[row + drow][col + dcol] == "M"
                    for drow, dcol in self.directions
                    if 0 <= row + drow < n and 0 <= col + dcol < m
                )
                if num_mines == 0:
                    return_board[row][col] = "B"
                    for drow, dcol in self.directions:
                        dfs(row + drow, col + dcol)
                else:
                    return_board[row][col] = str(num_mines)
            return False

        dfs(click[0], click[1])
        return return_board
