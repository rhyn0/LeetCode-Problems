"""528. Random Pick with Weight on LeetCode.

====================================================

Since this design is related to randomness, during testing we will use a seed value.

Test Methods:

    >>> import random
    >>> random.seed(456787654)
    >>> test_design_inputs(Solution,\
        ["Solution", "pickIndex"],\
        [[[1]],[]],\
        )
    [None, 0]
    >>> test_design_inputs(SolutionBinSearch,\
        ["Solution", "pickIndex"],\
        [[[1]],[]],\
        )
    [None, 0]
    >>> test_design_inputs(Solution,\
        ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"],\
        [[[1,3]],[],[],[],[],[]],\
        )
    [None, 1, 1, 0, 1, 0]
    >>> test_design_inputs(SolutionBinSearch,\
        ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"],\
        [[[1,3]],[],[],[],[],[]],\
        )
    [None, 0, 0, 1, 1, 1]
"""

# Standard Library
from itertools import accumulate
from random import randint
from typing import Any


class Solution:
    """Randomly pick values from the given list of values.

    Probability of an item being picked is `value / sum(w)`.
    """

    def __init__(self, w: list[int]) -> None:  # noqa: D107
        self.total_sum = sum(w)
        self.prefix_sum = list(accumulate(w))

    def pickIndex(self) -> int:
        """Return the index of the picked number."""
        random_num = randint(1, self.total_sum)
        for i, x in enumerate(self.prefix_sum):
            if random_num < x:
                return i
        # possible to reach here with inputs like [1]
        return 0


class SolutionBinSearch:
    """Randomly pick values from the given list of values using binary search.

    Probability of an item being picked is `value / sum(w)`.
    """

    def __init__(self, w: list[int]) -> None:  # noqa: D107
        self.total_sum = sum(w)
        self.prefix_sum = list(accumulate(w))

    def pickIndex(self) -> int:
        """Return the index of the picked number."""
        random_num = randint(1, self.total_sum)
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if self.prefix_sum[mid] < random_num:
                low = mid + 1
            else:
                high = mid
        return low


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
