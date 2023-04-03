# Standard Library


class Solution:  # noqa: D101
    def plusOne(self, digits: list[int]) -> list[int]:
        """Given a list of digits representing a number, add one.

        List of digits is in order of most significant digit to
        least significant, left to right.

        Args:
            digits (List[int]): List of digits

        Returns:
            List[int]: List of digits after adding one.
        """
        return [int(tok) for tok in str(int("".join(str(d) for d in digits)) + 1)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(sol.plusOne([4, 3, 2, 1]))  # [4,3,2,2]
    print(sol.plusOne([9]))  # [1, 0]
