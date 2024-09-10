"""Essentials of Dynamic Programming Knapsack Problem on LeetCode.

474. Ones and Zeroes on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = ["10","0001","111001","1","0"], 5, 3
    >>> example_case_2 = ["10","0","1"], 1, 1
    >>> test_case_1 = ["10","0001","111001","1","0"], 4, 3

Example 1:
    >>> sol.findMaxForm(*example_case_1)
    4
    >>> sol.findMaxFormTab(*example_case_1)
    4

Example 2:
    >>> sol.findMaxForm(*example_case_2)
    2
    >>> sol.findMaxFormTab(*example_case_2)
    2

Test 1:
    >>> sol.findMaxForm(*test_case_1)
    3
    >>> sol.findMaxFormTab(*test_case_1)
    3
"""

# Standard Library
from functools import cache


class Solution:  # noqa: D101
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """Return the maximum subset of given binary strings.

        A valid subset will have at most `m` 0's and `n` 1's.
        A set x is a subset of a set y if all elements of x are also elements of y.

        Args:
            strs (list[str]): Array of binary strings
            m (int): maximum number of 0s
            n (int): maximum number of 1s

        Returns:
            int: size of subset
        """
        count_ones = [s.count("1") for s in strs]
        count_zeroes = [s.count("0") for s in strs]
        strs_len = len(strs)

        @cache
        def dfs(index: int, num_zeroes: int = 0, num_ones: int = 0):
            if index == strs_len:
                return 0

            new_zeroes, new_ones = (
                num_zeroes + count_zeroes[index],
                num_ones + count_ones[index],
            )
            # not take
            rv = dfs(index + 1, num_zeroes, num_ones)
            if new_zeroes <= m and new_ones <= n:
                # take case
                rv = max(rv, 1 + dfs(index + 1, new_zeroes, new_ones))
            return rv

        return dfs(0)

    def findMaxFormTab(self, strs: list[str], m: int, n: int) -> int:
        """Return same as above with bottom-up approach."""
        # 3d table - outermost is the current `str`, then the limit of zeroes
        # finally the limit of ones
        len_strs = len(strs)
        count_ones = [s.count("1") for s in strs]
        count_zeroes = [s.count("0") for s in strs]
        prev_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for str_i in range(len_strs - 1, -1, -1):
            curr_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            num_zeroes, num_ones = count_zeroes[str_i], count_ones[str_i]
            for m_i, prev_row in enumerate(prev_table):
                curr_table[m_i] = prev_row[:]
                for n_i in range(n + 1):
                    # previous work
                    if m_i >= num_zeroes and n_i >= num_ones:
                        curr_table[m_i][n_i] = max(
                            curr_table[m_i][n_i],
                            1 + prev_table[m_i - num_zeroes][n_i - num_ones],
                        )
            prev_table = curr_table

        return prev_table[m][n]
