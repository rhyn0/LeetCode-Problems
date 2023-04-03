# Standard Library
import doctest


class Solution:  # noqa: D101
    BOARD_EDGE = -2

    def findBall(self, grid: list[list[int]]) -> list[int]:  # spec
        """Find good drop points for ball on pegboard.

        Given a list of pegboard pathways, return List of drop points that go through.
        If grid is ``1`` at a point, it goes downwards to right
        if ``-1`` goes downwards to left.

        Args:
            grid (List[List[int]]): Pegboard path

        Returns:
            List[int]: Column where ball hits bottom if dropped in ith column
        """
        n, m = len(grid), len(grid[0])
        dp = [[self.BOARD_EDGE] * m for _ in range(n + 1)]
        dp[-1] = list(range(m))

        def dfs(row: int, col: int) -> int:
            if dp[row][col] != self.BOARD_EDGE:
                return dp[row][col]
            if col < m - 1 and grid[row][col] == 1 == grid[row][col + 1]:
                dp[row][col] = dfs(row + 1, col + 1)
            elif col > 0 and grid[row][col] == -1 == grid[row][col - 1]:
                dp[row][col] = dfs(row + 1, col - 1)
            else:
                dp[row][col] = -1
            return dp[row][col]

        return [dfs(0, i) for i in range(m)]


def main():
    """Where will the Ball Fall on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],\
            [-1,-1,-1,-1,-1]])
        [1, -1, -1, -1, -1]

    Example 2:
        >>> sol.findBall([[-1]])
        [-1]

    Example 3:
        >>> sol.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,\
            -1,-1]])
        [0, 1, 2, 3, 4, -1]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
