"""Meta Interview Question Practice List on LeetCode.

1331. Rank Transform of an Array on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [40,10,20,30]
    >>> example_case_2 = [100,100,100]
    >>> example_case_3 = [37,12,28,9,100,56,80,5,12]

Example 1:
    >>> sol.arrayRankTransform(example_case_1)
    [4, 1, 2, 3]
    >>> sol.arrayRankTransformOrderedMap(example_case_1)
    [4, 1, 2, 3]

Example 2:
    >>> sol.arrayRankTransform(example_case_2)
    [1, 1, 1]
    >>> sol.arrayRankTransformOrderedMap(example_case_2)
    [1, 1, 1]

Example 3:
    >>> sol.arrayRankTransform(example_case_3)
    [5, 3, 4, 2, 8, 6, 7, 1, 3]
    >>> sol.arrayRankTransformOrderedMap(example_case_3)
    [5, 3, 4, 2, 8, 6, 7, 1, 3]
"""


class Solution:  # noqa: D101
    def arrayRankTransform(self, nums: list[int]) -> list[int]:
        """Transform the given array of numbers to output their rank in the array.

        Rank starts at 1 for the smallest number.

        Args:
            nums (list[int]): Numbers to rank

        Returns:
            list[int]: Rank of the number at each index
        """
        # need the unique values
        sort_nums = {v: k for k, v in enumerate(sorted(set(nums)), start=1)}
        return [sort_nums[num] for num in nums]

    def arrayRankTransformOrderedMap(self, nums: list[int]) -> list[int]:
        """Return same as above using an ordered map for number lookup."""
        # sort the numbers, and insert into dictionary
        # since python3.7, dictionaries are ordered by insertion order
        # don't need set deduplication as duplicate keys are next to each other
        # won't ruin insertion order.
        num_to_index: dict[int, list[int]] = {num: [] for num in sorted(nums)}
        # iterate all nums and add occurrence index to the mapping
        for i, num in enumerate(nums):
            num_to_index[num].append(i)
        rank = 1
        # make a new array as to not overwrite argument
        rv = [0] * len(nums)
        for idxs in num_to_index.values():
            for idx in idxs:
                rv[idx] = rank
            rank += 1
        return rv
