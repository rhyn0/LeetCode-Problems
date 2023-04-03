# Standard Library
import doctest


class Solution:  # noqa: D101
    def leastInterval(self, tasks: list[str], n: int) -> int:  # spec
        """Schedule a list of tasks in shortest amount of time possible.

        There is a cooldown time between doing the same task `n`.
        Return the length of time to do the tasks.
        Each task takes 1 unit of time and can idle
        while cooling down to do same task.

        Args:
            tasks (List[str]): List of tasks represented as string characters
            n (int): length of cooldown period

        Returns:
            int: units of time to finish all tasks
        """
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        freq.sort()
        freq_max = freq.pop()
        idle_time = (freq_max - 1) * n
        while freq and idle_time > 0:
            idle_time -= min(freq_max - 1, freq.pop())
        idle_time = max(idle_time, 0)  # make sure idle isn't negative
        return len(tasks) + idle_time


def main():
    """Task Scheduler on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
        8

    Example 2:
        >>> sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0)
        6

    Example 3:
        >>> sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
        16

    Test 1:
        Should be A->B->C->A->B->C->D->A->B->C->D->E
        >>> sol.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2)
        12
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
