# Standard Library
from collections.abc import Iterator
import doctest
from enum import IntEnum
from itertools import pairwise
from operator import add


class Solution:  # noqa: D101
    def shortestWordDistance(self, word_list: list[str], word1: str, word2: str) -> int:
        """Return shortest distance between individual words in the ``word_list``.

        ``word1`` and ``word2`` can be the same word, but refer to distinct appearances.
        This means a ``word_list`` of ['make', 'hi']
        cannot have word1 == word2 == 'make'

        Distance is calculated as the difference in indices.
        Guarantee is that a return value of 0 is impossible - if inputs are good.

        Args:
            word_list (list[str]): Layout of all words for pathfinding
            word1 (str): first word to find
            word2 (str): second word to find

        Returns:
            int: minimum distance between the words
        """

        @staticmethod
        def valid_word_pairs(index_list: list[str]) -> Iterator[tuple[int, int]]:
            for idx1, idx2 in pairwise(index_list):
                if (
                    abs(int(idx1)) == abs(int(idx2))
                    or all("-" in ind for ind in (idx1, idx2))
                    or all("-" not in ind for ind in (idx1, idx2))
                ):
                    continue
                yield (int(idx1), int(idx2))

        indices = []
        for i, word in enumerate(word_list):
            if word == word1:
                indices.append(str(i))
            if word == word2:
                indices.append("-" + str(i))
        return min(abs(add(*pair)) for pair in valid_word_pairs(indices))

    def shortestWordDistanceSpace(
        self, word_list: list[str], word1: str, word2: str
    ) -> int:
        """Return result same as above but using O(1) space.

        I like this one less.
        """
        word1_idx = word2_idx = -1
        minima = float("inf")

        def min_compare() -> int | float:
            if word1_idx == -1 or word2_idx == -1 or word1_idx == word2_idx:
                return minima
            return min(minima, abs(word1_idx - word2_idx))

        for i, word in enumerate(word_list):
            if word == word1:
                word1_idx = i

            minima = min_compare()

            if word == word2:
                word2_idx = i

            minima = min_compare()
        # if invalid problem given
        if isinstance(minima, float):
            raise TypeError("invalid")

        return minima

    def shortestWordDistanceObj(
        self, word_list: list[str], word1: str, word2: str
    ) -> int:
        """Return same as above using a custom object in the sorting list."""

        class WordMatch(IntEnum):
            WORD1 = 1
            WORD2 = 2

        indices = []
        for i, word in enumerate(word_list):
            if word == word1:
                indices.append((i, WordMatch.WORD1))
            if word == word2:
                indices.append((i, WordMatch.WORD2))

        min_dist = float("inf")
        for first_match, sec_match in pairwise(indices):
            if any(
                attr1 == attr2
                for attr1, attr2 in zip(first_match, sec_match, strict=True)
            ):
                continue
            min_dist = min(min_dist, sec_match[0] - first_match[0])

        if isinstance(min_dist, float):
            raise TypeError("invalid")

        return min_dist


def main():
    """Minimum Word Distance III on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = (["practice", "makes", "perfect", "coding", "makes"],\
            "makes", "coding")
        >>> example_case_2 = (["practice", "makes", "perfect", "coding", "makes"],\
            "makes", "makes")
        >>> test_case_1 = (["a","a","c","b"], "a", "b")
        >>> test_case_2 = (["a", "b"], "b", "a")

    Example 1:
        >>> sol.shortestWordDistance(*example_case_1)
        1
        >>> sol.shortestWordDistanceSpace(*example_case_1)
        1
        >>> sol.shortestWordDistanceObj(*example_case_1)
        1

    Example 2:
        >>> sol.shortestWordDistance(*example_case_2)
        3
        >>> sol.shortestWordDistanceSpace(*example_case_2)
        3
        >>> sol.shortestWordDistanceObj(*example_case_2)
        3

    Test 1:
        >>> sol.shortestWordDistance(*test_case_1)
        2
        >>> sol.shortestWordDistance(*test_case_1)
        2
        >>> sol.shortestWordDistanceObj(*test_case_1)
        2

    Test 2:
        >>> sol.shortestWordDistance(*test_case_2)
        1
        >>> sol.shortestWordDistance(*test_case_2)
        1
        >>> sol.shortestWordDistanceObj(*test_case_2)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
