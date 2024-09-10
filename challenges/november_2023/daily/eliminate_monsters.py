"""Daily Challenge for November 7 on LeetCode: Problem #1921 [Medium]."""

# Standard Library
import doctest
import math


class Solution:  # noqa: D101
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        """Return maximum number of monsters that can be eliminated based on inputs.

        Weapon can only be fired once per minute, starts charged.
        If monster reaches 0 distance, at start of minute then you lose.

        Args:
            dist (list[int]): Monster i distance from you
            speed (list[int]): Monster i speed approaching you

        Returns:
            int: Number of monsters that can be eliminated
        """
        for idx, turns_to_arrive in enumerate(
            # sort ascending
            sorted(
                # ceil since extra turn for the remainder
                math.ceil(distance / monster_speed)
                for distance, monster_speed in zip(dist, speed, strict=True)
            ),
        ):
            # can only eliminate one monster per time slot
            # each index of the monster array is a time
            # so if a monster arrives faster than their position in the array
            # we can't eliminate in time
            if turns_to_arrive <= idx:
                return idx
        return len(dist)


def main() -> None:
    """1921. Eliminate Maximum Number of Monsters on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,3,4], [1,1,1]
        >>> example_case_2 = [1,1,2,3], [1,1,1,1]
        >>> example_case_3 = [3,2,4], [5,3,2]

    Example 1:
        >>> sol.eliminateMaximum(*example_case_1)
        3

    Example 2:
        >>> sol.eliminateMaximum(*example_case_2)
        1

    Example 3:
        >>> sol.eliminateMaximum(*example_case_3)
        1
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
