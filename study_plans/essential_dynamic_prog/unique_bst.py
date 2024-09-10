"""Essentials of Dynamic Programming Tree Problem on LeetCode.

96. Unique Binary Search Trees on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 3
    >>> example_case_2 = 2

Example 1:
    >>> sol.numTrees(example_case_1)
    5
    >>> sol.numTreesCatalan(example_case_1)
    5

Example 2:
    >>> sol.numTrees(example_case_2)
    2
    >>> sol.numTreesCatalan(example_case_2)
    2
"""


class Solution:  # noqa: D101
    def numTrees(self, n: int) -> int:
        """Return the number of structurally unique BSTs given n nodes.

        Assume nodes are [1,2,3,...,n]. For each index i, the number of unique
        binary search trees that can be formed is dependent on the size of the
        left and right subsequence (i - 1) and (n - i).

        Args:
            n (int): Number of nodes

        Returns:
            int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]

    def numTreesCatalan(self, n: int) -> int:
        """Returns same as above using Catalan numbers.

        More info: https://en.wikipedia.org/wiki/Catalan_number
        """
        # C_0 = 1, C_n = 2(2n - 1) * C_{n-1} / n + 1
        # can build forward relationship as
        # C_0 = 1, C_{n + 1} = 2(2n + 1) * C_n / (n + 2)
        catalan = 1
        for i in range(n):
            catalan = 2 * (2 * i + 1) * catalan / (i + 2)
        return int(catalan)
