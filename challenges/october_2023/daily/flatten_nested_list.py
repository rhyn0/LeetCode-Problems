# Standard Library
from abc import ABC
from abc import abstractmethod
from collections.abc import Iterator
import doctest


class NestedInteger:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int | None = None,
        list_: list | None = None,
    ) -> None:
        self._integer = val if val is not None else 0
        self._list = list_ if list_ is not None else []
        self.is_integer = val is not None

    def isInteger(self) -> bool:  # noqa: D102
        return self.is_integer

    def getInteger(self) -> int:  # noqa: D102
        return self._integer

    def getList(self) -> list:  # noqa: D102
        return self._list


class NestedIteratorABC(ABC):
    """ABC to allow for simple interface design."""

    @abstractmethod
    def next(self) -> int:  # noqa: A003
        """Return the next integer value of the iterator."""

    @abstractmethod
    def hasNext(self) -> bool:
        """Return if there are more values for the iterator to return."""


class NestedIterator(NestedIteratorABC):  # noqa: D101
    def __init__(self, nestedList: list[NestedInteger]) -> None:  # noqa: D107, N803
        self.data = self._flatten(nestedList)
        self._curr_idx = 0
        self._hasNext = self._curr_idx < len(self.data)

    def _flatten(self, nested_list: list[NestedInteger]) -> list[int]:
        """Flatten nested list into list of integers."""
        res = []
        for val in nested_list:
            if val.isInteger():
                res.append(val.getInteger())
            else:
                res.extend(self._flatten(val.getList()))
        return res

    def next(self) -> int:  # noqa: A003, D102
        item = self.data[self._curr_idx]
        self._curr_idx += 1
        self._hasNext = self._curr_idx < len(self.data)
        return item

    def hasNext(self) -> bool:  # noqa: D102
        return self._hasNext


class NestedIteratorGen(NestedIteratorABC):  # noqa: D101
    def __init__(self, nested_list: list[NestedInteger]) -> None:  # noqa: D107
        self._gen = self._int_generator(nested_list)
        # value peeked from the generator
        self._peeked = None

    def _int_generator(self, nested_list: list[NestedInteger]) -> Iterator[int]:
        """Yield integers from nested list."""
        for val in nested_list:
            if val.isInteger():
                yield val.getInteger()
            else:
                yield from self._int_generator(val.getList())

    def next(self) -> int | None:  # noqa: A003
        """Return the next integer value of the iterator."""
        # call hasNext to prep the peeked value
        if not self.hasNext():
            return None
        item, self._peeked = self._peeked, None
        return item

    def hasNext(self) -> bool:
        """Return if there are more values for the iterator to return."""
        # repeatd calls to hasNext should not advance the generator
        if self._peeked is not None:
            return True
        try:
            self._peeked = next(self._gen)
        except StopIteration:
            return False
        return True


def consume_iterator(iterator: NestedIteratorABC) -> list[int]:
    """Consume iterator and return list of values."""
    res = []
    while iterator.hasNext():
        res.append(iterator.next())
    return res


def create_iterator(
    vals: list[list[int] | int],
    cls: type = NestedIterator,
) -> NestedIteratorABC:
    """Map input to NestedInteger's and create iterator over that."""

    def helper(item: int | list) -> NestedInteger:
        if isinstance(item, int):
            return NestedInteger(val=item)
        nested_list = []
        for val in item:
            result = helper(val)
            if result.isInteger():
                nested_list.append(result)
            else:
                nested_list.extend(result.getList())

        return NestedInteger(list_=nested_list)

    return cls([helper(val) for val in vals])


def main() -> None:
    """341. Flatten Nested List Iterator on LeetCode.

    ====================================================

    Test Methods:
        >>> consume_iterator(create_iterator([[1,1],2,[1,1]]))
        [1, 1, 2, 1, 1]
        >>> consume_iterator(create_iterator([1,[4,[6]]]))
        [1, 4, 6]
        >>> consume_iterator(create_iterator([[1,1],2,[1,1]], cls=NestedIteratorGen))
        [1, 1, 2, 1, 1]
        >>> consume_iterator(create_iterator([1,[4,[6]]], cls=NestedIteratorGen))
        [1, 4, 6]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
