# Standard Library
import doctest
from operator import itemgetter


class Solution:  # noqa: D101
    def maximumUnits(self, box_types: list[list[int]], truck_size: int) -> int:
        """Find maximum value of knapsack if each item has constant weight.

        Limited by space of truckSize find the highest value truck that
        can be made with the given boxes.
        Pretty much a greedy algorithm but mathematically true.

        Args:
            box_types (List[List[int]]): list of lists
                each sublist is the number of that box with the value of that box
            truck_size (int): Maximum number of boxes on truck

        Returns:
            int: Maximized value for truck with given parameters.
        """
        truck_value = 0
        for items, value in sorted(box_types, key=itemgetter(1), reverse=True):
            truck_value += min(truck_size, items) * value
            truck_size -= items
            if truck_size <= 0:
                break
        return truck_value


def main() -> None:
    """1710. Maximum Units on a Truck on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[1, 3], [2, 2], [3, 1]], 4
        >>> example_case_2 = [[5, 10], [2, 5], [4, 7], [3, 9]], 10

    Example 1:
        >>> sol.maximumUnits(*example_case_1)
        8

    Example 2:
        >>> sol.maximumUnits(*example_case_2)
        91
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
