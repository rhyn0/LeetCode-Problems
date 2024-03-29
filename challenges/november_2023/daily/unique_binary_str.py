"""Daily Challenge for November 16 on LeetCode: Problem #1980 [Medium]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """Return a binary string not in the given list.

        The binary string must be of length n. Where n is the length of the given list.
        Each string in the given list is of length n.

        Args:
            nums (list[str]): List of length n, containing binary strings of length n

        Returns:
            str: binary string not in the given list
        """
        given_nums = {int(num, 2) for num in nums}
        for num in range(2 ** len(nums)):
            if num not in given_nums:
                return f"{num:b}".zfill(len(nums))
        return ""

    def findDifferentBinaryStringBacktrack(self, nums: list[str]) -> str:
        """Return same as above using backtracking."""
        given_nums = set(nums)
        n = len(nums)

        def backtrack(curr_str: str) -> str:
            if len(curr_str) == n:
                if curr_str not in given_nums:
                    return curr_str
                # failed, backtrack
                return ""

            add_zero = backtrack(curr_str + "0")
            if add_zero:
                # succeeded below
                return add_zero
            return backtrack(curr_str + "1")

        return backtrack("")

    def findDifferentBinaryStringCantor(self, nums: list[str]) -> str:
        """Return same as above using Cantor's Diagonal.

        This was an interesting read from the Editorial on Leetcode.
        More info:
        https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
        """
        # proof of set theory
        # by changing each digit in the binary string to be opposite
        # of the ith string's ith digit, we can create a new string
        return "".join("1" if num[i] == "0" else "0" for i, num in enumerate(nums))


def test_any_of(returned: str, options: list[str]) -> None:
    """Return True if returned is any of the options."""
    assert any(  # noqa: S101
        returned == option for option in options
    ), f"{returned} is not an option"


def main() -> None:
    """1980. Find Unique Binary String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ["01","10"]
        >>> example_case_2 = ["00","01"]
        >>> example_case_3 = ["111","011","001"]

    Example 1:
        >>> sol.findDifferentBinaryString(example_case_1)
        '00'
        >>> test_any_of(\
            sol.findDifferentBinaryStringBacktrack(example_case_2), ["10", "11"]\
            )
        >>> test_any_of(\
            sol.findDifferentBinaryStringCantor(example_case_2), ["10", "11"]\
            )

    Example 2:
        >>> sol.findDifferentBinaryString(example_case_2)
        '10'
        >>> test_any_of(\
            sol.findDifferentBinaryStringBacktrack(example_case_2), ["10", "11"]\
            )
        >>> test_any_of(\
            sol.findDifferentBinaryStringCantor(example_case_2), ["10", "11"]\
            )

    Example 3:
        >>> sol.findDifferentBinaryString(example_case_3)
        '000'
        >>> test_any_of(\
            sol.findDifferentBinaryStringBacktrack(example_case_3),\
            ["000", "010", "100", "101", "110"]\
            )
        >>> test_any_of(\
            sol.findDifferentBinaryStringCantor(example_case_3),\
            ["000", "010", "100", "101", "110"]\
            )
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
