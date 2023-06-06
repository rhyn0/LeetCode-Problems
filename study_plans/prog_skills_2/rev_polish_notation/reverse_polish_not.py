# Standard Library
import doctest
from math import ceil
import operator


class Solution:  # noqa: D101
    def evalRPN(self, tokens: list[str]) -> int:
        """Evaluate tokenized Reverse Polish Notation expression.

        Link to RPN http://en.wikipedia.org/wiki/Reverse_Polish_notation

        Args:
            tokens (List[str]): Tokenized list of expression parts in string format

        Returns:
            int: integer returned from expression
        """

        def div_to_zero(op1: int, op2: int) -> int:
            return (
                operator.floordiv(op1, op2)
                if op1 > 0 < op2 or op1 < 0 > op2
                else ceil(op1 / op2)
            )

        stack = []
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": div_to_zero,
        }

        for tok in tokens:
            if tok not in operations:
                stack.append(int(tok))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(operations[tok](left_operand, right_operand))
        return stack.pop()


def main() -> None:
    """Reverse Polish Notation on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ["2", "1", "+", "3", "*"]
        >>> example_case_2 = ["10", "6", "9", "3", "+", "-11", "*", "/",\
            "*", "17", "+", "5", "+"]
        >>> test_case_1 = ["4", "13", "5", "/", "+"]

    Example 1:
        >>> sol.evalRPN(example_case_1)
        9

    Example 1:
        >>> sol.evalRPN(example_case_2)
        22

    Test 1:
        >>> sol.evalRPN(test_case_1)
        6
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
