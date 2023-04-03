# Standard Library
import doctest


class Solution:  # noqa: D101
    def isHappy(self, n: int) -> bool:  # spec
        """Return if a number is happy or not.

        Happy numbers are numbers that will reach 1 after following the process of:
          1. Sum squares of digits
          2. Repeat

        Args:
            n (int): Input number

        Returns:
            bool: True if it is a happy number, False otherwise
        """
        seen_set = set()
        while n != 1:
            if n in seen_set:
                return False
            seen_set.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        return True


def main():
    """Happy Number on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.isHappy(19)
        True

    Example 2:
        >>> sol.isHappy(2)
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
