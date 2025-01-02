"""Meta Interview Question Practice List on LeetCode.

131. Palindrome Partitioning on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "aab"
    >>> example_case_2 = "a"

Example 1:
    >>> sol.partition(example_case_1)
    [['a', 'a', 'b'], ['aa', 'b']]

Example 2:
    >>> sol.partition(example_case_2)
    [['a']]
"""


class Solution:  # noqa: D101
    def partition(self, s: str) -> list[list[str]]:
        """Return all possible partitions of s such that each substring is a palindrome.

        Args:
            s (str): String to partition

        Returns:
            list[list[str]]: List of each partition possible
        """
        results: list[list[str]] = []
        start_end_is_palindrome = set()
        n = len(s)

        def dfs(curr_result: list[str], start: int):
            nonlocal results, start_end_is_palindrome, n, s
            if start >= n:
                # no more string to work with, so we have a valid group
                # need a copy otherwise previous frame will mess with it
                results.append(curr_result.copy())
            for end in range(start, n):
                # palindrome if the characters at start and end are equivalent
                # and one of: the length of the substring is less than equal to 2
                # or the substring from start+1 to end-1 is also a palindrome.
                if s[start] == s[end] and (
                    end - start <= 2  # noqa: PLR2004
                    or (start + 1, end - 1) in start_end_is_palindrome
                ):
                    start_end_is_palindrome.add((start, end))
                    curr_result.append(s[start : end + 1])
                    dfs(curr_result, end + 1)
                    curr_result.pop()

        dfs([], 0)
        return results
