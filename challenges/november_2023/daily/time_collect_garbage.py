"""Daily Challenge for November 20 on LeetCode: Problem #2391 [Medium]."""
# Standard Library
from collections import Counter
import doctest
from itertools import accumulate


class Solution:  # noqa: D101
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        """Return minimum amount of time to collect all garbage.

        There are 3 types of garbage, and each type must be picked up by a
        specific truck. Each truck can only pick up one unit of garbage in a unit
        of time. Each truck starts at the first house, and must travel to the
        next house in order.

        Args:
            garbage (list[str]): piles of garbage at each house
            travel (list[int]): time to travel between houses

        Returns:
            int: Total time to pick up all garbage in all piles
        """
        garbage_types = "MPG"
        time_spent_per_garbage = Counter()
        # truck index is correlated to the abvoe string
        truck_position = {garbage_type: 0 for garbage_type in garbage_types}
        # prefix with index 0, to simplify logic when a truck doesnt move
        travel_prefix = [0, *list(accumulate(travel))]
        for house_num, pile in enumerate(garbage):
            count = Counter(pile)
            time_spent_per_garbage.update(count)
            for garbage_type in garbage_types:
                if garbage_type in count:
                    truck_position[garbage_type] = house_num

        return sum(
            # travel is a n-1 length array
            time_spent_per_garbage[garbage_type]
            + travel_prefix[truck_position[garbage_type]]
            for garbage_type in garbage_types
        )

    def garbageCollectionNoCounter(self, garbage: list[str], travel: list[int]) -> int:
        """Return same as above using no Counter."""
        total_time = 0
        # truck index is correlated to the abvoe string
        truck_position: dict[str, int] = {}
        # prefix with index 0, to simplify logic when a truck doesnt move
        travel_prefix = [0, *list(accumulate(travel))]
        for house_num, pile in enumerate(garbage):
            for garbage_unit in pile:
                truck_position[garbage_unit] = house_num
            total_time += len(pile)

        return total_time + sum(
            travel_prefix[truck_position[garbage_type]]
            for garbage_type in truck_position
        )


def main() -> None:
    """2391. Minimum Amount of Time to Collect Garbage on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ["G","P","GP","GG"], [2,4,3]
        >>> example_case_2 = ["MMM","PGM","GP"], [3,10]

    Example 1:
        >>> sol.garbageCollection(*example_case_1)
        21
        >>> sol.garbageCollectionNoCounter(*example_case_1)
        21

    Example 2:
        >>> sol.garbageCollection(*example_case_2)
        37
        >>> sol.garbageCollectionNoCounter(*example_case_2)
        37
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
