# Standard Library
import doctest
from itertools import zip_longest


class Solution:  # noqa: D101
    def addBinary(self, a: str, b: str) -> str:  # spec
        """Add two binary numbers together.

        Numbers are binary in string representation.
        There are no leading ``'0'`` in operands or answer.

        Args:
            a (str): String rep of binary number
            b (str): String rep of binary number

        Returns:
            str: String rep of binary answer
        """
        ret_number = ["0"] * (max(len(a), len(b)) + 1)
        carry = "0"
        for i, (ca, cb) in enumerate(
            zip_longest(reversed(a), reversed(b), fillvalue="0"),
            start=1,
        ):
            ones = sum(val == "1" for val in (ca, cb, carry))
            ret_number[-i] = str(ones % 2)
            carry = str(ones // 2)
        ret_number[0] = carry

        return (
            "".join(ret_number[ret_number.index("1") :])
            if ret_number.count("1")
            else "0"
        )


def main() -> None:
    """67. Add Binary on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "11", "1"
        >>> example_case_2 = "1010", "1011"

    Example 1:
        >>> sol.addBinary(*example_case_1)
        '100'

    Example 2:
        >>> sol.addBinary(*example_case_2)
        '10101'
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
