"""Daily Challenge for April 25, 2023."""
# Standard Library
import doctest
import heapq
from typing import Any


class SmallestInfiniteSet:
    """Object that represents the set of all positive integers.

    Ability to pop off the smallest number available in the set
    Can also add positive integers back into the set to later be popped.
    """

    def __init__(self):  # noqa: D107
        self.heap: list[int] = []
        self.curr_num = 0
        self.heap_set: set[int] = set()

    def addBack(self, val: int) -> None:
        """Add value back into set of values in the set."""
        if val < 0 or val > self.curr_num or val in self.heap_set:
            return
        self.heap_set.add(val)
        heapq.heappush(self.heap, val)

    def popSmallest(self) -> int:
        """Remove smallest number available in the set."""
        if self.heap:
            popped_val = heapq.heappop(self.heap)
            self.heap_set.remove(popped_val)
            return popped_val
        self.curr_num += 1
        return self.curr_num


def test_design_inputs(func_calls: list[str], inputs: list[list[Any]]) -> list[Any]:
    """Call input functions with associated inputs and return their output as list."""
    # first index is always an initialization
    sol = SmallestInfiniteSet()
    return [None] + [
        sol.__getattribute__(func)(*args)
        for func, args in zip(func_calls[1:], inputs[1:], strict=True)
    ]


def main():
    """2336. Smallest Number in Infinite Set on LeetCode.

    ====================================================

    Setup:
        >>> sol = SmallestInfiniteSet()

    Test Methods:
        >>> test_design_inputs(\
            ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",\
            "popSmallest", "addBack", "popSmallest", "popSmallest",\
            "popSmallest"], [[], [2], [], [], [], [1], [], [], []]\
            )
        [None, None, 1, 2, 3, None, 1, 4, 5]
        >>> test_design_inputs(\
            ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",\
            "popSmallest", "addBack", "addBack", "popSmallest", "popSmallest",\
            "popSmallest"], [[], [2], [], [], [], [1], [1], [], [], []]\
            )
        [None, None, 1, 2, 3, None, None, 1, 4, 5]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
