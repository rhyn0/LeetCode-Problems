# Standard Library
import doctest
from typing import Final


class Solution:  # noqa: D101
    NUMBER_LETTERS: Final = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> list[str]:  # spec
        """Return all combinations possible from a given telephone number.

        A keypad has letters associated with each number.
        This will build all combinations of same length as input.

        Args:
            digits (str): Input string containing digits only from 2-9

        Returns:
            List[str]: All combinations of letters from the keypad digit input
        """
        if not digits:
            return []
        ret_list = [""]
        for digit in digits:
            interval_list = [
                el + char for char in self.NUMBER_LETTERS[digit] for el in ret_list
            ]

            ret_list = list(interval_list)
        return ret_list

    def letterCombinationsDFS(self, digits: str) -> list[str]:
        """Return all combinations possible from a given telephone number."""
        size_n = len(digits)
        ret_list = []
        if size_n == 0:
            return ret_list

        def dfs(curr_len: int, tail: str = "") -> None:
            if curr_len == size_n:
                ret_list.append(tail)
                return
            for char in self.NUMBER_LETTERS[digits[curr_len]]:
                dfs(curr_len + 1, tail + char)

        dfs(0)
        return ret_list


def main() -> None:
    """Letter Combinations of a Phone Number on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.letterCombinations("23")
        ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']

    Example 2:
        >>> sol.letterCombinations("")
        []

    Example 3:
        >>> sol.letterCombinations("2")
        ['a', 'b', 'c']

    Backtracking Approach
    Example 1:
        >>> sol.letterCombinationsDFS("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    Example 2:
        >>> sol.letterCombinationsDFS("")
        []

    Example 3:
        >>> sol.letterCombinationsDFS("2")
        ['a', 'b', 'c']
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
