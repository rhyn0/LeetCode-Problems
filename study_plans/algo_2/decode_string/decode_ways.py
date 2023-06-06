# Standard Library
import doctest


class Solution:  # noqa: D101
    A = 10
    Z = 26

    def numDecodings(self, in_str: str) -> int:  # spec
        """Return number of valid decodings of a string.

        A string is encoded as characters to their position in the alphabet.
        A -> 1... Z -> 26. There are multiple ways to decode a given string.
        Leading 0 numbers ("05") are not valid as they are not equivalent to "5".

        Args:
            in_str (str): Encoded string of numbers

        Returns:
            int: Number of ways to decode the string
        """
        if in_str.startswith("0"):
            return 0
        size_n = len(in_str)
        prev_prev_way, prev_way = 1, 1
        for i in range(1, size_n):
            curr_way = 0
            if in_str[i] != "0":
                curr_way += prev_way
            check_dual = int(in_str[i - 1 : i + 1])
            # two digit number string must be a valid two digit number
            if self.A <= check_dual <= self.Z:
                curr_way += prev_prev_way
            prev_prev_way, prev_way = prev_way, curr_way

        return prev_way


def main() -> None:
    """Decode Ways on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.numDecodings("12")
        2

    Example 2:
        >>> sol.numDecodings("226")
        3

    Example 3:
        >>> sol.numDecodings("06")
        0

    Test 1:
        >>> sol.numDecodings("2101")
        1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
