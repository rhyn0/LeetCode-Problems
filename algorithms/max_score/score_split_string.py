# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def maxScore(self, in_str: str) -> int:  # spec
        """Return greatest score after splitting into two non-empty substrings.

        Score is the sum of number of zeroes in left substring
        and number of ones in right substring.

        Args:
            in_str (str): Input string containing only '1' or '0'

        Returns:
            int: Greatest score in string
        """
        n, array = len(in_str), list(in_str)
        great_score = 0
        for split in range(1, n):
            great_score = max(
                great_score,
                array[:split].count("0") + array[split:].count("1"),
            )

        return great_score

    def maxScorePrefix(self, in_str: str) -> int:
        """Return greatest score by using prefix sum methodology."""
        counts = Counter(in_str)
        left_points = 0
        right_points = counts["1"]
        great_score = 0
        for character in in_str[:-1]:
            if character == "0":
                left_points += 1
            else:
                right_points -= 1
            great_score = max(great_score, left_points + right_points)

        return great_score


def main() -> None:
    """Maximum Score after Splitting a String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.maxScore("011101")
        5

    Example 2:
        >>> sol.maxScore("00111")
        5

    Example 3:
        >>> sol.maxScore("1111")
        3

    Test 1:
        >>> sol.maxScore("01")
        2

    ==============================
    Prefix Methodology

    Example 1:
        >>> sol.maxScorePrefix("011101")
        5

    Example 2:
        >>> sol.maxScorePrefix("00111")
        5

    Example 3:
        >>> sol.maxScorePrefix("1111")
        3

    Test 1:
        >>> sol.maxScorePrefix("01")
        2
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
