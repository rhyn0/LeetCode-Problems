# Standard Library
import doctest


class Solution:  # noqa: D101
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     ret_list, num_len = [], len(nums)
    #     for i_start, val in enumerate(nums):
    #         i_curr = (i_start + 1) % num_len
    #         while i_curr != i_start:
    #             if nums[i_curr] > val:
    #                 ret_list.append(nums[i_curr])
    #                 break
    #             i_curr = (i_curr + 1) % num_len
    #         else:
    #             ret_list.append(-1)
    #     return ret_list

    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        """Find the next greater number in a circular array, looking right.

        Return a list of the next value greater than that index when
        scanning left to right in circular array.

        Args:
            nums (List[int]): Circular array

        Returns:
            List[int]: List of greater values
        """
        ret_list, mono_stack = [-1] * len(nums), []
        for i, val in enumerate(nums):
            while mono_stack and nums[mono_stack[-1]] < val:
                ret_list[mono_stack.pop()] = val
            mono_stack.append(i)
        while mono_stack:  # circular array handling
            pop_ind = mono_stack.pop()
            pop_val = nums[pop_ind]
            for val in nums:
                if val > pop_val:
                    ret_list[pop_ind] = val
                    break
        return ret_list


def main() -> None:
    """503. Next Greater Element II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1, 2, 1]
        >>> example_case_2 = [1, 2, 3, 4, 3]

    Example 1:
        >>> sol.nextGreaterElements(example_case_1)
        [2, -1, 2]

    Example 2:
        >>> sol.nextGreaterElements(example_case_2)
        [2, 3, 4, -1, 4]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
