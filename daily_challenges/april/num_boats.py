"""Daily Challenge for April 3, 2023."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """Return number of boats needed to save the people if boat has weight limit.

        Each person has a weight given by `people[i]`, and a boat has a
        seat limit of 2 people. Total weight of people can not exceed the limit.
        Uses a greedy solution to pack the heaviest person available with the lightest.

        Args:
            people (list[int]): Weights of the people
            limit (int): Weight limit of the boat

        Returns:
            int: Number of boats needed to save all the people
        """
        sorted_people = sorted(people)
        lighter_person, heavy_person = 0, len(people) - 1
        used_boats = 0
        while lighter_person <= heavy_person:
            # if heaviest and lightest fit on boat, do it
            if sorted_people[lighter_person] + sorted_people[heavy_person] <= limit:
                lighter_person += 1
            heavy_person -= 1
            used_boats += 1

        return used_boats


def main():
    """881. Boats to Save People on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ([1,2], 3)
        >>> example_case_2 = ([3,2,2,1], 3)
        >>> example_case_3 = ([3,5,3,4], 5)
        >>> test_case_1 = ([5,1,4,2], 6)
        >>> test_case_2 = ([2, 2], 6)

    Example 1:
        >>> sol.numRescueBoats(*example_case_1)
        1

    Example 2:
        >>> sol.numRescueBoats(*example_case_2)
        3

    Example 3:
        >>> sol.numRescueBoats(*example_case_3)
        4

    Test 1:
        >>> sol.numRescueBoats(*test_case_1)
        2

    Test 2:
        >>> sol.numRescueBoats(*test_case_2)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        # ^ doctest.REPORT_ONLY_FIRST_FAILURE
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
