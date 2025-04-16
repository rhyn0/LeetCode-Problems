"""Daily Challenge for April 16, 2025.

2537. Count the Number of Good Subarrays on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [1,1,1,1,1], 10
    >>> example_case_2 = [3,1,4,3,2,2,4], 2

Example 1:
    >>> sol.countGood(*example_case_1)
    1

Example 2:
    >>> sol.countGood(*example_case_2)
    4
"""

# Standard Library
from collections import Counter


class Solution:  # noqa: D101
    def countGood(self, nums: list[int], k: int) -> int:
        """Return number of good subarrays in the array.

        Is a good subarray if there are at least `k` distinct pairs
        of numbers. i < j for each pair arr[i] == arr[j]

        Args:
            nums (list[int]): Source of numbers
            k (int): Min number of pairs in subarray

        Returns:
            int: Number of subarrays that are good
        """
        counts: Counter[int] = Counter()
        ans = 0
        num_pairs, right = 0, -1
        n = len(nums)
        for left in range(n):
            while num_pairs < k and right + 1 < n:
                right += 1
                # if there was 1 of nums[right] before
                # we add 1 pair now, so on so forth
                num_pairs += counts[nums[right]]
                counts[nums[right]] += 1
            if num_pairs >= k:
                # if the current size works, every size greater than this
                # would also be a valid subarray
                ans += n - right
            # back off pairs by removing current left
            counts[nums[left]] -= 1
            num_pairs -= counts[nums[left]]

        return ans
