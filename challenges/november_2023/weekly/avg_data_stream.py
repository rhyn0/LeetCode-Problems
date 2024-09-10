"""Weekly Challenge on LeetCode: Problem #346 [Easy]."""

# Standard Library
from collections import deque
import doctest
from typing import Any


class MovingAverage:
    """Implementation of computing the moving average of a data stream.

    The data stream is a sequence of integers.
    The size of the window is fixed at initialize.
    """

    def __init__(self, size: int) -> None:
        """Initialize the data structure with the size of the window."""
        self.capacity = size
        self.size = 0
        self.lru: deque[int] = deque()
        self.total = 0

    def next(self, val: int) -> float:
        """Add a new integer from stream and output current average."""
        self.total += val
        self.lru.append(val)
        self.size += 1
        if len(self.lru) > self.capacity:
            self.total -= self.lru.popleft()
            self.size -= 1
        return round(self.total / self.size, 5)


class MovingAverageCircular:
    """Perform the same as above using a circular queue."""

    def __init__(self, size: int) -> None:  # noqa: D107
        # head is the previous insertion point for values
        # total is the sum of all values in the queue
        # count is the number of items in the queue
        self.head = self.total = self.count = 0
        self.size = size
        self.queue = [0] * self.size

    def next(self, val: int) -> float:  # noqa: D102
        self.count += 1
        # find the tail point, which we willl overwrite
        tail = (self.head + 1) % self.size
        self.total = self.total - self.queue[tail] + val
        # move head
        self.head = (self.head + 1) % self.size
        # write new val at new head
        self.queue[self.head] = val
        # take min here for when count < size
        return round(self.total / min(self.size, self.count), 5)


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


def main() -> None:
    """346. Moving Average from Data Stream on LeetCode.

    ====================================================

    Test Methods:
        >>> test_design_inputs(MovingAverage,\
            [MovingAverage, "next", "next", "next", "next"],\
            [[3], [1], [10], [3], [5]],\
            )
        [None, 1.0, 5.5, 4.66667, 6.0]
        >>> test_design_inputs(MovingAverageCircular,\
            [MovingAverageCircular, "next", "next", "next", "next"],\
            [[3], [1], [10], [3], [5]],\
            )
        [None, 1.0, 5.5, 4.66667, 6.0]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
