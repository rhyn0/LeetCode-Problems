"""Daily Challenge for November 6 on LeetCode: Problem #1845 [Medium].

I have solved this problem before, hopefully not too similar.
Check that out at `../../../study_plans/prog_skills_2/seat_manager.
"""

# Standard Library
import doctest
import heapq
from typing import Any


class SeatManager:
    """Act as a seat reservation system for a total of `n` seats.

    Always hand out the smallest index seat available for reservations.
    Reservations can unreserve their seat at any time.
    """

    def __init__(self, n: int) -> None:  # noqa: D107
        # reservations seats are inclusive of n
        self.gen = iter(range(1, n + 1))
        self.heap = []
        # arbitrary value
        for _ in range(min(n, 5)):
            if not self._safe_heappush():
                break

    def _safe_heappush(self) -> bool:
        # Return false when failure
        try:
            heapq.heappush(self.heap, next(self.gen))
        except StopIteration:
            return False
        else:
            return True

    def reserve(self) -> int:  # noqa: D102
        # Take reservation
        reservation = heapq.heappop(self.heap)
        self._safe_heappush()
        return reservation

    def unreserve(self, n: int) -> None:  # noqa: D102
        heapq.heappush(self.heap, n)


def test_design_inputs(func_calls: list[str], inputs: list[list[int]]) -> list[Any]:
    """Call input functions with associated inputs and return their output as list."""
    # first index is always an initialization
    sol = SeatManager(*inputs[0])
    return [None] + [
        sol.__getattribute__(func)(*args)
        for func, args in zip(func_calls[1:], inputs[1:], strict=True)
    ]


def main() -> None:
    """1845. Seat Reservation Manager on LeetCode.

    ====================================================

    Test Methods:
        >>> test_design_inputs(\
            [SeatManager, "reserve", "reserve", "unreserve", "reserve", "reserve", \
                "reserve", "reserve", "unreserve"],\
            [[5], [], [], [2], [], [], [], [], [5]],\
            )
        [None, 1, 2, None, 2, 3, 4, 5, None]

    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
