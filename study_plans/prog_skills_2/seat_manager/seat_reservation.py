# Standard Library
import doctest
from heapq import heapify
from heapq import heappop
from heapq import heappush


class SeatManager:
    """Seat Reservation Manager.

    Manages reservations for a given ``n`` seats.

    Will return the lowest available seat when a reservation comes in.
    """

    def __init__(self, n: int) -> None:  # noqa: D107
        self.seats = list(range(1, n + 1))
        heapify(self.seats)

    def reserve(self) -> int:  # noqa: D102
        return heappop(self.seats)

    def unreserve(self, seat_num: int) -> None:  # noqa: D102
        heappush(self.seats, seat_num)


def main() -> None:
    """Seat Reservation Manager on LeetCode.

    ====================================================

    Setup:
        >>> sol = SeatManager(5)

    Example Set 1:
        >>> sol.reserve()
        1
        >>> sol.reserve()
        2
        >>> sol.unreserve(2)
        >>> sol.reserve()
        2
        >>> sol.reserve()
        3
        >>> sol.reserve()
        4
        >>> sol.reserve()
        5
        >>> sol.unreserve(5)
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
