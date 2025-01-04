"""Meta Interview Question Practice List on LeetCode.

151. Reverse Words in a String on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "the sky is blue"
    >>> example_case_2 = "  hello world  "
    >>> example_case_3 = "a good   example"

Example 1:
    >>> sol.reverseWords(example_case_1)
    'blue is sky the'

Example 2:
    >>> sol.reverseWords(example_case_2)
    'world hello'

Example 3:
    >>> sol.reverseWords(example_case_3)
    'example good a'
"""


class Solution:  # noqa: D101
    def reverseWords(self, s: str) -> str:
        """Return the string given but with the words in reverse order.

        Words are sequences of non-whitespace characters separated
        by whitespace characters. When returning, only use 1 space to
        separate words, do not preserve original whitespace.

        Args:
            s (str): String of words to reverse

        Returns:
            str: Reversed order words string
        """
        return " ".join(x.strip() for x in reversed(s.split()))
