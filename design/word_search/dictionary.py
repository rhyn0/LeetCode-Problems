# Standard Library
import doctest
from typing import Any


class WordDictionary:
    """Word search data structure.

    Stores a set of words and then searches if a word is stored internally.
    The structure accepts '.' in the regex manner for wildcard matching any letter.
    """

    def __init__(self) -> None:
        """Initialize trie as empty."""
        self.trie: dict[str, Any] = {}

    def addWord(self, word: str) -> None:  # spec
        """Add word to trie structure."""
        curr_node = self.trie
        for char in word:
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        # denote that a word ends at this pathway
        curr_node["$"] = True

    def search(self, pattern: str) -> bool:
        """Return if pattern exists in stored words."""

        def search_node(word: str, curr_trie: dict) -> bool:
            for idx, char in enumerate(word):
                if char not in curr_trie:
                    return char == "." and any(
                        search_node(word[idx + 1 :], curr_trie[ch])
                        for ch in curr_trie
                        if ch != "$"
                    )
                curr_trie = curr_trie[char]
            return "$" in curr_trie

        return search_node(pattern, self.trie)


def main() -> None:
    """Design Add and Search Words Data Structure on LeetCode.

    ====================================================

    Setup:
        >>> sol = WordDictionary()

    Test Methods:
        >>> sol.addWord("bad")
        >>> sol.addWord("dad")
        >>> sol.addWord("mad")
        >>> sol.search("pad")
        False
        >>> sol.search("bad")
        True
        >>> sol.search(".ad")
        True
        >>> sol.search("b..")
        True

    Actual Tests:
        >>> sol2 = WordDictionary()
        >>> sol2.addWord("a")
        >>> sol2.addWord("a")
        >>> sol2.search(".")
        True
        >>> sol2.search("a")
        True
        >>> sol2.search("aa")
        False
        >>> sol2.search("a")
        True
        >>> sol2.search(".a")
        False
        >>> sol2.search("a.")
        False

        >>> sol3 = WordDictionary()
        >>> sol3.addWord("a")
        >>> sol3.addWord("ab")
        >>> sol3.search("a")
        True
        >>> sol3.search("a.")
        True
        >>> sol3.search("ab")
        True
        >>> sol3.search(".a")
        False
        >>> sol3.search(".b")
        True
        >>> sol3.search("ab.")
        False
        >>> sol3.search(".")
        True
        >>> sol3.search("..")
        True

    """


if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.REPORTING_FLAGS | doctest.ELLIPSIS)
