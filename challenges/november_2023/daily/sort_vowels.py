"""Daily Challenge for November 13 on LeetCode: Problem #2785 [Medium]."""

# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def sortVowels(self, s: str) -> str:
        """Return the given string with the vowels sorted by ASCII value.

        Consonants should not change index between the original and output.
        Vowels are defined as uppercase or lowercase 'aeiou'.

        Args:
            s (str): String to sort the values of

        Returns:
            str: sorted vowels string
        """
        vowel_set = set("aeiou")
        consonants = [c if c.lower() not in vowel_set else "" for c in s]
        vowels = sorted(c for c in s if c.lower() in vowel_set)
        vowel_idx = 0
        for idx, c in enumerate(consonants):
            if c != "":
                continue
            consonants[idx] = vowels[vowel_idx]
            vowel_idx += 1
        return "".join(consonants)

    def sortVowelsCountSort(self, s: str) -> str:
        """Return same as above using counting sort."""

        def is_vowel(c: str) -> bool:
            # all characters are english letters
            return c.lower() in "aeiou"

        counts = Counter(c for c in s if is_vowel(c))
        output = list(s)
        sorted_vowels = sorted(counts.keys())
        vowel_idx = 0
        for idx, char in enumerate(output):
            if not is_vowel(char):
                continue
            while counts[sorted_vowels[vowel_idx]] == 0:
                vowel_idx += 1
            output[idx] = sorted_vowels[vowel_idx]
            counts[sorted_vowels[vowel_idx]] -= 1

        return "".join(output)

    def sortVowelsStack(self, s: str) -> str:
        """Return same as above using a stack."""
        v = "aeiouAEIOU"
        r = sorted([c for c in s if c in v], reverse=True)
        return "".join((r.pop() if c in v else c) for c in s)


def main() -> None:
    """2785. Sort Vowels in a String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "lEetcOde"
        >>> example_case_2 = "lYmpH"

    Example 1:
        >>> sol.sortVowels(example_case_1)
        'lEOtcede'
        >>> sol.sortVowelsCountSort(example_case_1)
        'lEOtcede'
        >>> sol.sortVowelsStack(example_case_1)
        'lEOtcede'

    Example 2:
        >>> sol.sortVowels(example_case_2)
        'lYmpH'
        >>> sol.sortVowelsCountSort(example_case_2)
        'lYmpH'
        >>> sol.sortVowelsStack(example_case_2)
        'lYmpH'
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
