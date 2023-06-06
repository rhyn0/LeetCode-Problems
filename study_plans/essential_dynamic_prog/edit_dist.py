"""Practice Problem from Essential Dynamic Programming Plan."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    @staticmethod
    def _get_table_relations(
        grid: list[list[int]],
        row: int,
        col: int,
    ) -> tuple[int, int, int]:
        # hardcoded reliance on the below, diagonal bottom right, and right
        return (grid[row + 1][col], grid[row + 1][col + 1], grid[row][col + 1])

    def minDistance(self, word1: str, word2: str) -> int:
        """Calculate the edit distance between the two words.

        To edit the words, we can either insert, replace, or delete
        a character. Each of those operations costs 1.
        Edit distance would be the number of operations need to make both
        words match.

        Args:
            word1 (str): first word, canonically the starting point
            word2 (str): second word, canonically the target

        Returns:
            int: Edit distance to convert word1 to word2.
        """
        word1_len, word2_len = len(word1), len(word2)
        dp = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]

        # fill bottom row for word2 is empty string case
        for i in range(word2_len + 1):
            dp[-1][i] = word2_len - i
        # fill right column for word1 is empty string case
        for j in range(word1_len + 1):
            dp[j][-1] = word1_len - j

        for i in range(word1_len - 1, -1, -1):
            for j in range(word2_len - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(self._get_table_relations(dp, i, j))

        return dp[0][0]

    def minDistance1D(self, word1: str, word2: str) -> int:
        """Returns same as above using 1D array."""
        word1_len, word2_len = len(word1), len(word2)
        # padding for empty string
        prev_dp = [word2_len - i for i in range(word2_len + 1)]
        dp = prev_dp[:]
        for word1_idx in range(word1_len - 1, -1, -1):
            # as we go backwards from empty string case on word1,
            # while keeping word2 as empty string, the value increases by 1
            dp[-1] = prev_dp[-1] + 1
            for word2_idx in range(word2_len - 1, -1, -1):
                if word1[word1_idx] == word2[word2_idx]:
                    dp[word2_idx] = prev_dp[word2_idx + 1]
                else:
                    dp[word2_idx] = 1 + min(
                        self._get_table_relations([dp, prev_dp], 0, word2_idx),
                    )
            prev_dp = dp[:]
        return dp[0]


def main() -> None:
    """72. Edit Distance on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "horse", "ros"
        >>> example_case_2 = "intention", "execution"
        >>> test_case_1 = "", "rose"
        >>> test_case_2 = "rose", ""
        >>> test_case_3 = "", ""
        >>> test_case_4 = "hello", "hello"

    Example 1:
        >>> sol.minDistance(*example_case_1)
        3
        >>> sol.minDistance1D(*example_case_1)
        3

    Example 2:
        >>> sol.minDistance(*example_case_2)
        5
        >>> sol.minDistance1D(*example_case_2)
        5

    Test 1:
        >>> sol.minDistance(*test_case_1)
        4
        >>> sol.minDistance1D(*test_case_1)
        4

    Test 2:
        >>> sol.minDistance(*test_case_2)
        4
        >>> sol.minDistance1D(*test_case_2)
        4

    Test 3:
        >>> sol.minDistance(*test_case_3)
        0
        >>> sol.minDistance1D(*test_case_3)
        0

    Test 4:
        >>> sol.minDistance(*test_case_4)
        0
        >>> sol.minDistance1D(*test_case_4)
        0
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
