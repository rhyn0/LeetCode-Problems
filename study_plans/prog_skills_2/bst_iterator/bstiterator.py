from __future__ import annotations

# Standard Library
from collections.abc import Generator
import doctest


class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:  # noqa: D105
        return f"TreeNode({self.val}, left={self.left}, right={self.right})"


class BSTIterator:
    """Binary Search Tree Iterator.

    Iterates over tree in-order.
    """

    def __init__(self, root: TreeNode) -> None:
        """Initialize the iterator given a Tree.

        Tree must contain at least 1 node.

        Args:
            root (TreeNode): tree root node
        """
        self.it = self._iterate(root)
        self._next = next(self.it, None)

    def hasNext(self) -> bool:  # spec
        """Return whether there is another value in tree.

        Returns:
            bool: Whether there are more values to iterate over in tree
        """
        return self._next is not None

    def next(self) -> int | None:
        """Return next value in tree for in-order.

        Can return None if finished the tree.

        Returns:
            int | None: int for values of Tree, otherwise None
        """
        res, self._next = self._next, next(self.it, None)
        return res

    def _iterate(self, node: TreeNode | None) -> Generator[int, None, None]:
        if node is None:
            return
        yield from self._iterate(node.left)
        yield node.val
        yield from self._iterate(node.right)


def main() -> None:
    """Binary Search Tree Iterator on LeetCode.

    ====================================================

    Setup:
        >>> tree = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        >>> sol = BSTIterator(tree)

    Example 1:
        >>> sol.next()
        3

    Example 2:
        >>> sol.hasNext()
        True
        >>> sol.next()
        7
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
