"""Weekly Challenge 2 for June, 2025.

255. Verify Preorder Sequence in Binary Search Tree on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [5,2,1,3,6]
    >>> example_case_2 = [5,2,6,1,3]

Example 1:
    >>> sol.verifyPreorder(example_case_1)
    True
    >>> sol.verifyPreorderSpace(example_case_1)
    True

Example 2:
    >>> sol.verifyPreorder(example_case_2)
    False
    >>> sol.verifyPreorderSpace(example_case_2)
    False
"""


class Solution:  # noqa: D101
    def verifyPreorder(self, preorder: list[int]) -> bool:
        """Return whether the given array is a valid preorder traversal.

        Args:
            preorder (list[int]): integers are unique

        Returns:
            bool: Whether is valid
        """
        stack: list[int] = []
        # given that all integer node values are positive
        min_limit = -1
        for number in preorder:
            while stack and stack[-1] < number:
                min_limit = stack.pop()
            if number <= min_limit:
                return False
            stack.append(number)
        return True

    def verifyPreorderSpace(self, preorder: list[int]) -> bool:
        """Return same as above using constant space."""
        min_limit = -1
        stack_idx = 0
        for number in preorder:
            while stack_idx != 0 and preorder[stack_idx - 1] < number:
                stack_idx -= 1
                min_limit = preorder[stack_idx]
            if number < min_limit:
                return False
            # overwrite input arg
            preorder[stack_idx] = number
            stack_idx += 1
        return True
