# Standard Library
from itertools import groupby
from itertools import pairwise


class Solution:  # noqa: D101
    def checkArithmeticSubarrays(  # spec
        self,
        nums: list[int],
        left_index: list[int],
        right_index: list[int],
    ) -> list[bool]:
        """Given list of int return subarray [left, right] is arithmetic progression.

        Arithmetic progression means difference between each element is same when sorted

        Args:
            nums (List[int]): Array of numbers
            left_index (List[int]): Left indices for the ith iteration
            right_index (List[int]): Inclusive right indices for the ith iteration

        Returns:
            List[bool]: For the ith iteration, True if arithmetic subarray,
                False otherwises
        """
        ret_list = []
        for left_ind, right_ind in zip(left_index, right_index, strict=False):
            groups = groupby(
                pairwise(sorted(nums[left_ind : right_ind + 1])),
                key=lambda x: x[1] - x[0],
            )
            ret_list.append(
                next(groups) and next(groups, False) is False,
            )
        return ret_list


if __name__ == "__main__":
    sol = Solution()
    sol.checkArithmeticSubarrays(
        [4, 6, 5, 9, 3, 7],
        left_index=[0, 0, 2],
        right_index=[2, 3, 5],
    )  # [True, False, True]
    sol.checkArithmeticSubarrays(
        [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
        left_index=[0, 1, 6, 4, 8, 7],
        right_index=[4, 4, 9, 7, 9, 10],
    )  # [False, True, False, False, True, True]
