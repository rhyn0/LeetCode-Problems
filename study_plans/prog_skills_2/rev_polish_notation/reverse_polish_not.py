# Standard Library
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

        def div_to_zero(op1, op2) -> int:
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(
        sol.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )  # 22
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))  # 6
