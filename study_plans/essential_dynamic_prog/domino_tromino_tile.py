"""Essentials of Dynamic Programming General 1D Problem on LeetCode.

790. Domino and Tromino Tiling on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 3
    >>> example_case_2 = 1

Example 1:
    >>> sol.numTilings(example_case_1)
    5
    >>> sol.numTilingsSpace(example_case_1)
    5

Example 2:
    >>> sol.numTilings(example_case_2)
    1
    >>> sol.numTilingsSpace(example_case_2)
    1
"""


class Solution:  # noqa: D101
    def numTilings(self, n: int) -> int:
        """Return the number of ways to tile a 2x`n` board.

        Available tiles are a 2x1 domino and an L-shaped tromino.
        Every square on the board must be covered by a tile.

        Args:
            n (int): Extra dimension of board to tile

        Returns:
            int: Number of ways to tile modulo 10**9 + 7
        """
        mod = 10**9 + 7
        dp_perfect = [0] * (n)
        # would love to put imperfect, but too easy to mistake when reading
        dp_not_perfect = [0] * (n)
        # due to indexing being 0 based
        # each index i actually corresponds to i+1 columns
        dp_perfect[:2] = [1, 2]
        # idx i means ways to fill i columns but leave a gap at i + 1 column
        dp_not_perfect[:2] = [1, 1]
        for idx in range(2, n):
            dp_perfect[idx] = (
                dp_perfect[idx - 1] + dp_perfect[idx - 2] + 2 * dp_not_perfect[idx - 1]
            ) % mod
            dp_not_perfect[idx] = (dp_perfect[idx - 2] + dp_not_perfect[idx - 1]) % mod

        return dp_perfect[n - 1]

    def numTilingsSpace(self, n: int) -> int:
        """Return same as above using space optimized."""
        mod = 10**9 + 7
        # only need up to 2 indexes ago for each type
        if n <= 2:  # noqa: PLR2004
            return n
        perfect_prev_prev, perfect_prev = 1, 2
        imperfect_prev = 1
        perfects = [perfect_prev_prev, perfect_prev]
        for _ in range(2, n):
            perfect_prev_prev, perfect_prev, imperfect_prev = (
                perfect_prev,
                (perfect_prev + perfect_prev_prev + 2 * imperfect_prev) % mod,
                (perfect_prev_prev + imperfect_prev) % mod,
            )
            perfects.append(perfect_prev)

        return perfect_prev
