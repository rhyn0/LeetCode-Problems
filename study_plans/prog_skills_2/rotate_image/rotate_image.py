# Standard Library


class Solution:  # noqa: D101
    def rotate(self, matrix: list[list[int]]) -> None:
        """Rotate a given matrix 90 degrees clockwise.

        Can not make another 2D matrix and rotate it there.
        Update must be done to original object.

        Args:
            matrix (List[List[int]]): In-out parameter, representing matrix to rotate.
        """
        n_size = len(matrix)
        for row in range(n_size):
            for col in range(row + 1, n_size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            matrix[row].reverse()


if __name__ == "__main__":
    sol = Solution()
    matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matr)
    print(matr)  # [[7,4,1],[8,5,2],[9,6,3]]
    sol.rotate(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    )  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
