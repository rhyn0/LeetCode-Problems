"""Meta Interview Question Practice List on LeetCode.

1768. Merge Strings Alternately on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "abc", "pqr"
    >>> example_case_2 = "ab", "pqrs"
    >>> example_case_3 = "abcd", "pq"

Example 1:
    >>> sol.mergeAlternately(*example_case_1)
    'apbqcr'

Example 2:
    >>> sol.mergeAlternately(*example_case_2)
    'apbqrs'

Example 3:
    >>> sol.mergeAlternately(*example_case_3)
    'apbqcd'
"""


class Solution:  # noqa: D101
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Return the merged string between the two words.

        Characters should alternate between the two strings
        starting with `word1` unless one string is longer than the other.

        Args:
            word1 (str): First word to merge
            word2 (str): second word to merge with

        Returns:
            str: Merged words
        """
        n, m = len(word1), len(word2)
        output = []
        for i in range(min(n, m)):
            output.append(word1[i])
            output.append(word2[i])
        if m > n:
            output.extend(word2[n:])
        elif n > m:
            output.extend(word1[m:])
        return "".join(output)
