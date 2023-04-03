# Standard Library
import doctest


class Solution:  # noqa: D101
    def findCircleNum(self, connected: list[list[int]]) -> int:  # spec
        """Return number of connected components in graph defined by connection list.

        Input is a N x N matrix representing which nodes each node is connected to

        Args:
            connected (List[List[int]]): connection matrix

        Returns:
            int: number of connected components
        """
        rows, cols = len(connected), len(connected[0])
        ret_num_prov = 0

        def dfs(x_row: int) -> None:
            connected[x_row][x_row] = 0
            for i in range(cols):
                if connected[x_row][i] == 1:
                    connected[x_row][i] = 0
                    connected[i][x_row] = 0
                    dfs(i)

        for i_row in range(rows):
            if connected[i_row][i_row] == 1:
                ret_num_prov += 1
                dfs(i_row)
        return ret_num_prov


def main():
    """Number of Provinces on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        2

    Example 2:
        >>> sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
        3

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
