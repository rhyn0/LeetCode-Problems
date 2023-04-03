# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def minimumRounds(self, tasks: list[int]) -> int:  # spec
        """Return total number of rounds to do all the given tasks.

        Tasks have a difficulty, have to do tasks of similar
        difficulty in groups of 2 or 3.

        Args:
            tasks (list[int]): list of tasks to do

        Returns:
            int: minimum rounds needed to finish all tasks.
        """
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        rounds = 0
        for diff, count in counter.items():
            if count == 1:
                return -1
            rounds += (diff // 3 + 1) if count % 3 else diff // 3

        return rounds


def main():
    """Minimum Rounds to Complete All Tasks on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.minimumRounds([2,2,3,3,2,4,4,4,4,4])
        4

    Example 2:
        >>> sol.minimumRounds([2,3,3])
        -1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
