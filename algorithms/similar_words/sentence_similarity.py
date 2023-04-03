# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def areSentencesSimilar(  # spec
        self, sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]
    ) -> bool:
        """Return if two sentences are similar or not.

        Sentence are similar if same length and each word in each sentence is similar.
        Similar words are given by the similarPairs and a word is
        always similar to itself.

        Args:
            sentence1 (list[str]): space split sentence 1
            sentence2 (list[str]): space split sentence 2
            similar_pairs (list[list[str]]): list of pairs of words that are similar

        Returns:
            bool: True if similar sentences False otherwise
        """
        if len(sentence1) != len(sentence2):
            return False

        # word can be similar to many things
        similar_dict: defaultdict[str, set[str]] = defaultdict(set)
        for w1, w2 in similar_pairs:
            similar_dict[w1].add(w2)
            similar_dict[w2].add(w1)

        for word1, word2 in zip(sentence1, sentence2, strict=True):
            if word1 == word2 or word2 in similar_dict[word1]:
                continue
            return False

        return True


def main():
    """Sentence Similarity on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.areSentencesSimilar(["great","acting","skills"],\
            ["fine","drama","talent"], [["great","fine"],["drama","acting"],\
            ["skills","talent"]])
        True

    Example 2:
        >>> sol.areSentencesSimilar(["great"], ["great"], [])
        True

    Example 3:
        >>> sol.areSentencesSimilar(["great"], ["doubleplus","good"],\
            [["great","doubleplus"]])
        False

    Test 1:
        >>> sol.areSentencesSimilar("this summer thomas get actually actually rich\
            and possess the actually great and fine vehicle every morning he drives\
            one nice car around one great city to have single super excellent super\
            as his brunch but he only eat single few fine food as some fruits he wants\
            to eat an unique and actually healthy life".split(),\
            "this summer thomas get very very rich and possess the very fine and well\
            car every morning he drives a fine car around unique great city to take any\
            really wonderful fruits as his breakfast but he only drink an few excellent\
            breakfast as a super he wants to drink the some and extremely healthy life\
            ".split(),\
            [["good","nice"],["good","excellent"],["good","well"],["good","great"],\
                ["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],\
                ["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],\
                ["wonderful","great"],["extraordinary","nice"],\
                ["extraordinary", "excellent"],["extraordinary","well"],\
                ["extraordinary","great"],["one","a"],["one","an"],["one","unique"],\
                ["one","any"],["single","a"],["single","an"],["single","unique"],\
                ["single","any"],["the","a"],["the","an"],["the","unique"],\
                ["the","any"],["some","a"],["some","an"],["some","unique"],\
                ["some","any"],["car","vehicle"],["car","automobile"],\
                ["car","truck"],["auto","vehicle"],["auto","automobile"],\
                ["auto","truck"],["wagon","vehicle"],["wagon","automobile"],\
                ["wagon","truck"],["have","take"],["have","drink"],["eat","take"],\
                ["eat","drink"],["entertain","take"],["entertain","drink"],\
                ["meal","lunch"],["meal","dinner"],["meal","breakfast"],\
                ["meal","fruits"],["super","lunch"],["super","dinner"],\
                ["super","breakfast"],["super","fruits"],["food","lunch"],\
                ["food","dinner"],["food","breakfast"],["food","fruits"],\
                ["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],\
                ["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],\
                ["keep","possess"],["very","super"],["very","actually"],\
                ["really","super"],["really","actually"],["extremely","super"],\
                ["extremely","actually"]])
        True
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
