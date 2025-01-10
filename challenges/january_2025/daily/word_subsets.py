"""Daily Challenge for January 10, 2025.

916. Word Subsets on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = ["amazon","apple","facebook","google","leetcode"], ["e","o"]
    >>> example_case_2 = ["amazon","apple","facebook","google","leetcode"], ["l","e"]

Example 1:
    >>> sol.wordSubsets(*example_case_1)
    ['facebook', 'google', 'leetcode']
    >>> sol.wordSubsetsFaster(*example_case_1)
    ['facebook', 'google', 'leetcode']
    >>> sol.wordSubsetsArray(*example_case_1)
    ['facebook', 'google', 'leetcode']

Example 2:
    >>> sol.wordSubsets(*example_case_2)
    ['apple', 'google', 'leetcode']
    >>> sol.wordSubsetsFaster(*example_case_2)
    ['apple', 'google', 'leetcode']
    >>> sol.wordSubsetsArray(*example_case_2)
    ['apple', 'google', 'leetcode']
"""

# Standard Library
from collections import Counter


class Solution:  # noqa: D101
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """Return the universal words of words1.

        A word 'x' is a subset of 'y' if every character in 'x' occurs in 'y'
        including multiplicity. A universal word 'a' from `words1` is one that for
        all words 'b' in `words2`, 'b' is a subset of 'a'.

        Args:
            words1 (list[str]): Possible universal words
            words2 (list[str]): Words to use as subsets

        Returns:
            list[str]: Output of universal words
        """
        counts1, counts2 = [Counter(w) for w in words1], [
            Counter(w) for w in {"".join(sorted(word)) for word in words2}
        ]
        return [
            word
            for word, count1 in zip(words1, counts1, strict=True)
            # counter does inclusion
            if all(c2 < count1 for c2 in counts2)
        ]

    def wordSubsetsFaster(self, words1: list[str], words2: list[str]) -> list[str]:
        """Return same as above but using a better algorithm."""
        max_char_2_counts = [0] * 26  # lowercase english only
        for word in words2:
            for c, count in Counter(word).most_common():
                max_char_2_counts[ord(c) - ord("a")] = max(
                    count,
                    max_char_2_counts[ord(c) - ord("a")],
                )
        rv = []
        for word in words1:
            counter = Counter(word)
            if all(
                counter.get(chr(ord("a") + i), 0) >= max_2_count
                for i, max_2_count in enumerate(max_char_2_counts)
            ):
                rv.append(word)
        return rv

    def wordSubsetsArray(self, words1: list[str], words2: list[str]) -> list[str]:
        """Return same as above but using better data structure."""
        alphabet_size = 26

        def count(word) -> list[int]:
            nonlocal alphabet_size
            ans = [0] * alphabet_size
            for c in word:
                ans[ord(c) - ord("a")] += 1
            return ans

        max_char_2_counts = [0] * alphabet_size
        for word in words2:
            max_char_2_counts = [
                max(a, b) for a, b in zip(count(word), max_char_2_counts, strict=True)
            ]
        return [
            word
            for word in words1
            if all(a >= b for a, b in zip(count(word), max_char_2_counts, strict=True))
        ]
