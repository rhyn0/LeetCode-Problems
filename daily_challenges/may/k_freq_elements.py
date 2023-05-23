"""Daily Challenge Problem for May 22, 2023."""
# Standard Library
from collections import Counter
import doctest
import heapq


class Solution:  # noqa: D101
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Return k most frequent numbers from input `nums`.

        Return order is not required, can be different between runs.
        Answer for any call is unique:
            E.g. [1, 2, 3], k = 1 is not valid

        Args:
            nums (list[int]): List of numbers
            k (int): Number of most common elements to return

        Returns:
            list[int]: Top K frequent elements
        """
        counts = Counter(nums)
        return [item[0] for item in counts.most_common(k)]

    def topKFrequentNoLib(self, nums: list[int], k: int) -> list[int]:
        """Return same as above without using any imports."""
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        return sorted(count.keys(), key=count.get)[-k:]

    def topKFrequentHeap(self, nums: list[int], k: int) -> list[int]:
        """Return same as above using Heap approach."""
        return [
            item[0]
            for item in heapq.nlargest(k, Counter(nums).items(), key=lambda x: x[1])
        ]


def main():
    """347. Top K Frequent Elements on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,1,1,2,2,3], 2
        >>> example_case_2 = [1], 1

    Example 1:
        >>> sol.topKFrequent(*example_case_1)
        [1, 2]
        >>> sol.topKFrequentNoLib(*example_case_1)
        [1, 2]
        >>> sol.topKFrequentHeap(*example_case_1)
        [1, 2]

    Example 2:
        >>> sol.topKFrequent(*example_case_2)
        [1]
        >>> sol.topKFrequentNoLib(*example_case_2)
        [1]
        >>> sol.topKFrequentHeap(*example_case_2)
        [1]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE
    )
