"""Practice Problem from Essential Dynamic Programming Plan."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """Return the minimum deletion cost necessary to make the strings equal.

        Deletion cost is determined as the ASCII value of the character deleted

        Args:
            s1 (str): first string to modify
            s2 (str): second string to modify

        Returns:
            int: Sum of ASCII values of deleted characters
        """

        # start with 2D case for ease
        def dp_relation(s1_idx: int, s2_idx: int, grid: list[list[int]]) -> int:
            """Return value for the recursive relation."""
            s1_char_val, s2_char_val = ord(s1[s1_idx]), ord(s2[s2_idx])
            return min(
                grid[s1_idx + 1][s2_idx] + s1_char_val,  # delete s1 character
                grid[s1_idx][s2_idx + 1] + s2_char_val,  # delete s2 character
                grid[s1_idx + 1][s2_idx + 1] + s1_char_val + s2_char_val,
            )

        n, m = len(s1), len(s2)
        # string1 as rows, string2 as columns
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for base_row in range(n - 1, -1, -1):
            dp[base_row][-1] = dp[base_row + 1][-1] + ord(s1[base_row])

        for base_col in range(m - 1, -1, -1):
            dp[-1][base_col] = dp[-1][base_col + 1] + ord(s2[base_col])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp_relation(i, j, dp)

        return dp[0][0]

    def minimumDeleteSum1D(self, s1: str, s2: str) -> int:
        """Return same as above using a 1D array."""
        n, m = len(s1), len(s2)
        prev_dp = [0]
        for idx in range(m - 1, -1, -1):
            prev_dp.append(ord(s2[idx]) + prev_dp[m - idx - 1])
        prev_dp = list(reversed(prev_dp))  # noqa: FURB187

        dp = prev_dp[:]
        for i in range(n - 1, -1, -1):
            dp[-1] = prev_dp[-1] + ord(s1[i])
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[j] = prev_dp[j + 1]
                else:
                    s1_chr_val, s2_chr_val = ord(s1[i]), ord(s2[j])
                    dp[j] = min(
                        prev_dp[j] + s1_chr_val,
                        dp[j + 1] + s2_chr_val,
                        prev_dp[j + 1] + s1_chr_val + s2_chr_val,
                    )

            prev_dp = dp[:]
        return dp[0]


def main() -> None:
    """712. Minimum ASCII Delete Sum for Two Strings on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "sea", "eat"
        >>> example_case_2 = "delete", "leet"
        >>> example_case_3 = "xz", "yz"

    Example 1:
        >>> sol.minimumDeleteSum(*example_case_1)
        231
        >>> sol.minimumDeleteSum1D(*example_case_1)
        231

    Example 2:
        >>> sol.minimumDeleteSum(*example_case_2)
        403
        >>> sol.minimumDeleteSum1D(*example_case_2)
        403

    Example 3:
        >>> sol.minimumDeleteSum(*example_case_3)
        241
        >>> sol.minimumDeleteSum1D(*example_case_3)
        241
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
