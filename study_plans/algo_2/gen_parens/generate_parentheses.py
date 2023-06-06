# Standard Library
import doctest


class Solution:  # noqa: D101
    def generateParenthesis(self, num_parens: int) -> list[str]:  # spec
        """Return all valid combinations of N parentheses.

        A valid parenthesis is one that opens and closes.

        Args:
            num_parens (int): Number of parentheses is combinations

        Returns:
            List[str]: All combinations
        """
        ret_list = []

        def backtrack(open_num: int, close_num: int, tail: str = "") -> None:
            if open_num == num_parens == close_num:
                ret_list.append(tail)
                return
            if open_num < num_parens:
                backtrack(open_num + 1, close_num, tail + "(")
            if close_num < open_num:
                backtrack(open_num, close_num + 1, tail + ")")

        backtrack(0, 0)
        return ret_list


def main() -> None:
    """Genereate Parentheses on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.generateParenthesis(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']

    Example 2:
        >>> sol.generateParenthesis(1)
        ['()']
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
