# Standard Library
import doctest


class Solution:  # noqa: D101
    VOWELS = ("a", "e", "i", "o", "u")

    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        """Return spell checked versions of the queries.

        A query will get spellchecked if it is not a perfect match to one
        of the strings in `wordlist`.
        If it is a capitalization issue, then the first value matching
        (case insensitive) will be returned.
        If the vowels are incorrect (team -> taem) then the first value matching
        (ignoring vowels) will be returned.
        If no match for the 3 cases above, return empty string.

        Args:
            wordlist (List[str]): Input of correct words
            queries (List[str]): Query words to correct

        Returns:
            List[str]: List of corrected words if there was a match.
        """

        def devowel(word: str) -> str:
            return "".join("*" if char in self.VOWELS else char for char in word)

        words_vow_table = {}
        words_cap_table = {}
        words_table = set(wordlist)
        for word in wordlist:
            low_word = word.lower()
            words_cap_table.setdefault(low_word, word)
            words_vow_table.setdefault(devowel(low_word), word)

        def solve(query: str) -> str:
            if query in words_table:
                return query
            if query.lower() in words_cap_table:
                return words_cap_table[query.lower()]
            if (tmp_word := devowel(query.lower())) in words_vow_table:
                return words_vow_table[tmp_word]
            return ""

        return list(map(solve, queries))


def main():
    """Vowel Spellchecker on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.spellchecker(["KiTe","kite","hare","Hare"],\
            ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
        ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']

    Example 2:
        >>> sol.spellchecker(["yellow"], ["YellOw"])
        ['yellow']

    Test 1:
        >>> sol.spellchecker(["ae", "aa"], ["UU"])
        ['ae']
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
