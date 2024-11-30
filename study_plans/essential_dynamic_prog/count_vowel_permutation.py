"""Essentials of Dynamic Programming General Multidimensional on LeetCode.

1220. Count Vowels Permutation on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = 1
    >>> example_case_2 = 2
    >>> example_case_3 = 5

Example 1:
    >>> sol.countVowelPermutation(example_case_1)
    5
    >>> sol.countVowelPermutationRecursive(example_case_1)
    5

Example 2:
    >>> sol.countVowelPermutation(example_case_2)
    10
    >>> sol.countVowelPermutationRecursive(example_case_2)
    10

Example 3:
    >>> sol.countVowelPermutation(example_case_3)
    68
    >>> sol.countVowelPermutationRecursive(example_case_3)
    68
"""

# Standard Library
import functools


class Solution:  # noqa: D101
    MOD = 10**9 + 7

    def countVowelPermutation(self, n: int) -> int:
        """Return the number of unique strings of length `n`.

        Every character in the string is a lowercase vowel.
        Each vowel has rules on what characters can follow it.
        'a' - can only be followed by 'e'
        'e' - can only be followed by 'a' or 'i'
        'i' - can NOT be followed by 'i'
        'o' - can only be followed by 'i' or 'u'
        'u' - can only be followed by 'a'

        Args:
            n (int): Desired length of strings

        Returns:
            int: Number of possible strings modulo 10**9 + 7
        """
        # while this breaks leetcode constraints, good code assertion
        if n < 1:
            return 0
        # base case for length 1 strings
        # represents the number of strings ending in 'a','e','i','o','u' respectfully
        a_count = e_count = i_count = o_count = u_count = 1
        for _ in range(n - 1):
            # sum ways to make a string end with respective character
            a_count, e_count, i_count, o_count, u_count = (
                # e or i or u
                (e_count + i_count + u_count) % self.MOD,
                # a or i
                (a_count + i_count) % self.MOD,
                # e o
                (e_count + o_count) % self.MOD,
                # i
                i_count % self.MOD,
                # i o
                (i_count + o_count) % self.MOD,
            )
        return (a_count + e_count + i_count + o_count + u_count) % self.MOD

    def countVowelPermutationRecursive(self, n: int) -> int:
        """Returns same as above using recursion."""
        if n < 1:
            return 0

        @functools.cache
        def helper(curr_len: int, vowel_after: str) -> int:
            if curr_len == 1:
                return 1
            # at this stage we are a string of length `curr_len - 1`
            # if we know the `curr_len` vowel is `vowel_after` how many ways do it
            if vowel_after == "a":
                return sum(helper(curr_len - 1, vowel) for vowel in "eiu") % self.MOD
            if vowel_after == "e":
                return sum(helper(curr_len - 1, vowel) for vowel in "ai") % self.MOD
            if vowel_after == "i":
                return sum(helper(curr_len - 1, vowel) for vowel in "eo") % self.MOD
            if vowel_after == "o":
                return helper(curr_len - 1, "i") % self.MOD
            # has to be u
            return sum(helper(curr_len - 1, vowel) for vowel in "io") % self.MOD

        return sum(helper(n, vowel) for vowel in "aeiou") % self.MOD
