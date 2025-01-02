"""Meta Interview Question Practice List on LeetCode.

32. Longest Valid Parentheses on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "(()"
    >>> example_case_2 = ")()())"
    >>> example_case_3 = ""

Example 1:
    >>> sol.longestValidParentheses(example_case_1)
    2

Example 2:
    >>> sol.longestValidParentheses(example_case_2)
    4

Example 3:
    >>> sol.longestValidParentheses(example_case_3)
    0
"""


class Solution:  # noqa: D101
    def longestValidParentheses(self, s: str) -> int:
        """Return the length of the longest substring of valid parentheses.

        Args:
            s (str): Input string with only parentheses

        Returns:
            int: Length of the substring
        """
        left = right = best_length = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1

            # if counts are equal, then this is a balanced set of parentheses
            if left == right:
                best_length = max(best_length, left + right)
            # else if more closing parens than opening, reset counts
            elif left < right:
                left = right = 0
        left = right = 0
        for c in reversed(s):
            if c == "(":
                left += 1
            else:
                right += 1

            # if counts are equal, then this is a balanced set of parentheses
            if left == right:
                best_length = max(best_length, left + right)
            # else if more closing parens than opening, reset counts
            # but in the reverse case, left ( are closing
            elif left > right:
                left = right = 0
        return best_length
