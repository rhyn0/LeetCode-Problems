"""208. Implement Trie (Prefix Tree) on LeetCode.

====================================================

Test Methods:
    >>> test_design_inputs(Trie,\
        [Trie, "insert", "search", "search", "startsWith", "insert", "search"],\
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],\
        )
    [None, None, True, False, True, None, True]
"""

# Standard Library
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Self


@dataclass(slots=True)
class TrieNode:
    """Dataclass to hold the prefixes."""

    is_word: bool = field(default=False)
    chars: list[Self | None] = field(default_factory=lambda: [None] * 26)


class Trie:
    """Implement a Trie (Prefix Tree) datastructure.

    Use is to check for existence of words or the existence of prefix in the tree.
    """

    def __init__(self) -> None:  # noqa: D107
        self.root = TrieNode()

    def _search(self, prefix: str) -> TrieNode | None:
        node = self.root
        for c in prefix:
            val = self._char_val(c)
            if node.chars[val] is None:
                return None
            node = node.chars[val]
        return node

    @staticmethod
    def _char_val(c: str) -> int:
        return ord(c) - ord("a")

    def insert(self, word: str) -> None:
        """Insert a word into the trie.

        Args:
            word (str): all lowercase english word
        """
        node = self.root
        for c in word:
            val = self._char_val(c)
            if node.chars[val] is None:
                node.chars[val] = TrieNode()
            node = node.chars[val]
        node.is_word = True

    def search(self, word: str) -> bool:
        """Return if the input word was previously inserted into trie.

        Args:
            word (str): Word to exact match lookup

        Returns:
            bool: True if exists, False otherwise
        """
        node = self._search(word)
        if node is None:
            return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """Return whether the given prefix exists in the tree.

        Args:
            prefix (str): lowercase english only prefix

        Returns:
            bool: True for existence, false otherwise
        """
        node = self._search(prefix)
        return node is not None


def test_design_inputs(
    cls: type,
    func_calls: list[str],
    inputs: list[list[Any]],
) -> list[Any]:
    """Call input functions with associated inputs and return their output as list."""
    # first index is always an initialization
    sol = cls(*inputs[0])
    return [None] + [
        sol.__getattribute__(func)(*args)
        for func, args in zip(func_calls[1:], inputs[1:], strict=True)
    ]


### It is likely to be a more maintainable design if TrieNode were decoupled
### From the Trie and were in charge of its data functions at a lower level
### So let's do a quick redesign


@dataclass(slots=True)
class TrieNode2:
    """Short rewrite of original."""

    chars: list[Self | None] = field(default_factory=lambda: [None] * 26)
    is_word: bool = field(default=False)

    @staticmethod
    def _char_val(c: str) -> int:
        return ord(c) - ord("a")

    def contains_char(self, c: str) -> bool:
        """Whether this node has the prefix of `c`."""
        return self.chars[self._char_val(c)] is not None

    def get(self, c: str) -> Self | None:
        """Return the node for the prefix `c`."""
        return self.chars[self._char_val(c)]

    def put(self, c: str, node: Self) -> None:
        """Store another node at the given prefix."""
        self.chars[self._char_val(c)] = node


class Trie2:
    """Now simplify logic of using TrieNode.

    Main gain is that now the Trie doesn't manage the range of acceptable characters.
    So the underlying TrieNode2 could expand to support uppercase english and this code
    is still the same.
    """

    def __init__(self) -> None:  # noqa: D107
        self.root = TrieNode2()

    def _search(self, prefix: str) -> TrieNode | None:
        node = self.root
        for c in prefix:
            if not node.contains_char(c):
                return None
            node = node.get(c)
        return node

    def insert(self, word: str) -> None:
        """Insert a word into the trie.

        Args:
            word (str): all lowercase english word
        """
        node = self.root
        for c in word:
            if not node.contains_char(c):
                node.put(c, TrieNode2())
            node = node.get(c)
        node.is_word = True

    def search(self, word: str) -> bool:
        """Return if the input word was previously inserted into trie.

        Args:
            word (str): Word to exact match lookup

        Returns:
            bool: True if exists, False otherwise
        """
        node = self._search(word)
        return node and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """Return whether the given prefix exists in the tree.

        Args:
            prefix (str): lowercase english only prefix

        Returns:
            bool: True for existence, false otherwise
        """
        node = self._search(prefix)
        return node is not None
