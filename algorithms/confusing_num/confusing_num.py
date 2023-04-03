# Standard Library
import doctest


class Solution:  # noqa: D101
    # numbers and what they rotate to be
    ROTATIONS = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    STR_ROTATIONS = {str(k): str(val) for k, val in ROTATIONS.items()}

    def confusingNumber(self, num: int) -> bool:  # spec
        """Reverse and then rotate the string digit by digit.

        Uses the string version of the number to go digit by digit.

        Args:
            num (int): Number to reverse

        Returns:
            bool: Whether the number is confusing or not
        """
        rotate_num = ""
        for digit in reversed(str(num)):
            if digit not in self.STR_ROTATIONS:
                return False
            rotate_num += self.STR_ROTATIONS[digit]

        return int(rotate_num) != num

    def confusingNumberInt(self, num: int) -> bool:
        """Return whether the number is confusing or not.

        Does not use strings to get answer

        Args:
            num (int): Number to rotate

        Returns:
            bool: Whether the number is confusing or not
        """
        work_num = num
        rotate_num = 0
        while work_num > 0:
            digit = work_num % 10
            if digit not in self.ROTATIONS:
                return False
            rotate_num = rotate_num * 10 + self.ROTATIONS[digit]
            work_num //= 10

        return rotate_num != num


def main():
    """Confusing Number on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.confusingNumber(6)
        True
        >>> sol.confusingNumber(6) == sol.confusingNumberInt(6)
        True

    Example 2:
        >>> sol.confusingNumber(89)
        True
        >>> sol.confusingNumber(89) == sol.confusingNumberInt(89)
        True

    Example 3:
        >>> sol.confusingNumber(11)
        False
        >>> sol.confusingNumber(11) == sol.confusingNumberInt(11)
        True

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
