# Standard Library
import doctest
from operator import itemgetter


class MyCalendar:
    """Booking Calendar for timeslots across a day.

    Keeps track of all valid event's start and end time.
    """

    def __init__(self) -> None:  # noqa: D107
        self.ranges: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        """Add new event with start and end time given.

        If new event conflicts with a prior event, dont add it.

        Args:
            start (int): Start time
            end (int): End time

        Returns:
            bool: True if added, False otherwise.
        """
        for exist_st, exist_end in self.ranges:
            if exist_st < end and exist_end > start:
                return False
        self.ranges.append((start, end))
        self.ranges.sort(key=itemgetter(0, 1))
        return True


def main():
    """My Calendar I on LeetCode.

    ====================================================

    Example 1:
        >>> sol = MyCalendar()
        >>> sol.book(10, 20)
        True
        >>> sol.book(15, 25)
        False
        >>> sol.book(20, 30)
        True

    Test 1:
        >>> sol = MyCalendar()
        >>> sol.book(47, 50)
        True
        >>> sol.book(33, 41)
        True
        >>> sol.book(39, 45)
        False
        >>> sol.book(33, 42)
        False

    Test 2:
        >>> sol = MyCalendar()
        >>> sol.book(97, 100)
        True
        >>> sol.book(33, 51)
        True
        >>> sol.book(89, 100)
        False
        >>> sol.book(83, 100)
        False
        >>> sol.book(75, 92)
        True
        >>> sol.book(76, 95)
        False
        >>> sol.book(19, 30)
        True
        >>> sol.book(53, 63)
        True
        >>> sol.book(8, 23)
        False
        >>> sol.book(18, 37)
        False
        >>> sol.book(87, 100)
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
