"""Daily Challenge for June 1, 2025.

2929. Distribute Candies Among Children II on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 5, 2
    >>> example_case_2 = 3, 3

Example 1:
    >>> sol.distributeCandies(*example_case_1)
    3
    >>> sol.distributeCandiesMath(*example_case_1)
    3

Example 2:
    >>> sol.distributeCandies(*example_case_2)
    10
    >>> sol.distributeCandiesMath(*example_case_2)
    10
"""

# Standard Library
from math import comb


class Solution:  # noqa: D101
    def distributeCandies(self, n: int, limit: int) -> int:
        """Return the number of solutions for dividing candy between 3 children.

        All candies must be distributed and must be less than equal to the limit
        per child.

        Args:
            n (int): Total candies to distribute
            limit (int): Limit per child

        Returns:
            int: Number of solutions
        """
        return sum(
            max(
                min(limit, n - first_child_amt)
                - max(0, n - first_child_amt - limit)
                + 1,
                0,
            )
            for first_child_amt in range(min(n, limit) + 1)
        )

    ## Weekly Problem ?? Give bigger tests inputs

    def distributeCandiesMath(self, n: int, limit: int) -> int:
        """Return same as above but using math."""

        def custom_comb(x: int) -> int:
            if x < 0:
                # handle the negative case explictly
                return 0
            return comb(x, 2)

        return (
            custom_comb(n + 2)  # random distribution to children
            # remove the cases where we give limit + 1 to a child
            - 3 * custom_comb(n + 2 - (limit + 1))
            # re-add the cases where we actually gave 2 children limit + 1
            + 3 * custom_comb(n + 2 - 2 * (limit + 1))
            # remove cases where we give them all limit + 1.
            - custom_comb(n + 2 - 3 * (limit + 1))
        )
