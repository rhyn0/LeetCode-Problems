# Standard Library


class Solution:  # noqa: D101
    def findRotation(  # spec
        self, mat: list[list[int]], target: list[list[int]]
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))  # True
    print(sol.findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))  # False
    print(
        sol.findRotation(
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
        )
    )  # True
    print(sol.findRotation([[1]], [[0]]))  # False
