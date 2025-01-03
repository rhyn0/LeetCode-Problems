"""Meta Interview Question Practice List on LeetCode.

168. Excel Sheet Column Title on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 1
    >>> example_case_2 = 28
    >>> example_case_3 = 701

Example 1:
    >>> sol.convertToTitle(example_case_1)
    'A'

Example 2:
    >>> sol.convertToTitle(example_case_2)
    'AB'

Example 3:
    >>> sol.convertToTitle(example_case_3)
    'ZY'
"""


class Solution:  # noqa: D101
    def convertToTitle(self, columnNumber: int) -> str:  # noqa: N803
        """Given the (1-indexed) column number, return the Excel style column title.

        Args:
            columnNumber (int): positive number of the column number

        Returns:
            str: title of the column
        """
        output: list[str] = []
        a_value = ord("A")
        while columnNumber > 0:
            # due to 1 indexed value to column
            # 26 is our modulo but also the last valid value per character
            columnNumber -= 1  # noqa: N806
            columnNumber, char_index = divmod(columnNumber, 26)  # noqa: N806
            output.append(chr(char_index + a_value))
        return "".join(output[::-1])
