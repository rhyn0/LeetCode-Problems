# Standard Library


class Solution:  # noqa: D101
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        """Return smallest difference in array after being modified by k.

        Each val in nums array must be modified by +k or -k.

        Args:
            nums (List[int]): Nums array
            k (int): value to modify each value by

        Returns:
            int: Smallest difference between min and max after modification
        """
        if len(nums) == 1:
            return 0
        srt_nums = sorted(nums)
        diff = srt_nums[-1] - srt_nums[0]
        for i, val in enumerate(srt_nums[:-1]):
            local_min = min(srt_nums[0] + k, srt_nums[i + 1] - k)
            local_max = max(srt_nums[-1] - k, val + k)
            diff = min(diff, local_max - local_min)
        return diff


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestRangeII([1], 0))  # 0
    print(sol.smallestRangeII([0, 10], 2))  # 6
    print(sol.smallestRangeII([1, 3, 6], 3))  # 3
