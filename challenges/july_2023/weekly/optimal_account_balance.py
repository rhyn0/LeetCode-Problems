"""Weekly Challenge for Week 1 of July, 2023 on LeetCode."""
# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    MAX_INT = 10**5

    def minTransfers(self, transactions: list[list[int]]) -> int:
        """Return minimum transfers necessary to make all balances even.

        Transactions is a list of transactions [from_id, to_id, amount].
        Even balance would be a zero amount.

        Args:
            transactions (list[list[int]]): List of transactions

        Returns:
            int: Min transfers needed
        """
        balances = defaultdict(int)
        for from_id, to_id, amount in transactions:
            balances[from_id] -= amount
            balances[to_id] += amount

        balance_list = [balance for balance in balances.values() if balance != 0]
        n = len(balance_list)

        def backtrack(balance_idx: int) -> int:
            # this only checks balances forward from `balance_idx`
            while balance_idx < n and balance_list[balance_idx] == 0:
                balance_idx += 1
            # this while loop removes recursive overhead on consecutive zeroes
            # if all zero, we don't need to anymore transactions
            if balance_idx == n:
                return 0

            cost_for_level = self.MAX_INT

            for recipient_idx in range(balance_idx + 1, n):
                # only a valid recipient if their balances are of oppsite signs
                if balance_list[balance_idx] * balance_list[recipient_idx] > 0:
                    continue
                # since only need forward check, never modify balance_idx value
                balance_list[recipient_idx] += balance_list[balance_idx]
                cost_for_level = min(cost_for_level, 1 + backtrack(balance_idx + 1))
                balance_list[recipient_idx] -= balance_list[balance_idx]

            return cost_for_level

        return backtrack(0)


def main() -> None:
    """465. Optimal Account Balancing on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[0,1,10],[2,0,5]]
        >>> example_case_2 = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
        >>> test_case_1 = [[2,0,5],[3,4,4]]
        >>> test_case_2 = [[1,0,1],[2,1,1]]
        >>> test_case_3 = [[0,3,2],[1,4,3],[2,3,2],[2,4,2]]

    Example 1:
        >>> sol.minTransfers(example_case_1)
        2

    Example 2:
        >>> sol.minTransfers(example_case_2)
        1

    Test 1:
        >>> sol.minTransfers(test_case_1)
        2

    Test 2:
        >>> sol.minTransfers(test_case_2)
        1

    Test 3:
        >>> sol.minTransfers(test_case_3)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        ^ doctest.FAIL_FAST
        ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
