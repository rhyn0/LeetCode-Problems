"""Essentials of Dynamic Programming General 1D Problem on LeetCode.

Previously solved - see `../algo_2/decode_string/decode_ways.py`


91. Decode Ways on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "12"
    >>> example_case_2 = "226"
    >>> example_case_3 = "06"
    >>> self_test_1 = "1001"

Example 1:
    >>> sol.numDecodings(example_case_1)
    2

Example 2:
    >>> sol.numDecodings(example_case_2)
    3

Example 3:
    >>> sol.numDecodings(example_case_3)
    0

Self 1:
    >>> sol.numDecodings(self_test_1)
    0
"""


class Solution:  # noqa: D101
    def numDecodings(self, s: str) -> int:
        """Return number of valid ways to decode an encoded string.

        Map A-Z to numeric value 1-26. When we decode this string
        how many ways are there to decode it with valid solutions.
        Leading zeroes don't exist in this encoding process.

        Args:
            s (str): Possibly valid encoded string

        Returns:
            int: Possible solutions
        """
        if s[0] == "0":
            # quick return because invalid
            return 0
        ones_pos_26 = {"0", "1", "2", "3", "4", "5", "6"}
        one_zero = {"0", "1"}
        # base case is that in a length 1 string, only 1 way to decode
        prev_prev_count = prev_count = 1
        for i, c in enumerate(s[1:], start=1):
            current = prev_count if c != "0" else 0
            greater_than_10 = s[i - 1] != "0"
            less_than_26 = (
                (c in ones_pos_26) if s[i - 1] == "2" else (s[i - 1] in one_zero)
            )
            if greater_than_10 and less_than_26:
                current += prev_prev_count

            prev_prev_count, prev_count = prev_count, current

        return prev_count
