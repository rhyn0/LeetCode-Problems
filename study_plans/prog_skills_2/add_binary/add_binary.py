# Standard Library
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
            zip_longest(reversed(a), reversed(b), fillvalue="0"), start=1
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))  # 100
    print(sol.addBinary("1010", "1011"))  # 10101
