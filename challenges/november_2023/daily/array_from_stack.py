"""Daily Challenge for November 3 on LeetCode: Problem #1441 [Medium]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """Build `target` from a stream of numbers 1 to `n`.

        Use only stack operations (push to top, pop from top) to do this.

        Args:
            target (list[int]): Target array to build, strictly increasing
            n (int): Range of numbers for the stream

        Returns:
            list[str]: Output of operations in order
        """
        operation_list = []
        target_index = 0
        for i in range(1, n + 1):
            operation_list.append("Push")
            if i != target[target_index]:
                operation_list.append("Pop")
            else:
                target_index += 1
            if target_index == len(target):
                break
        return operation_list


def main() -> None:
    """1441. Build an Array With Stack Operations on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,3], 3
        >>> example_case_2 = [1,2,3], 3
        >>> example_case_3 = [1,2], 4

    Example 1:
        >>> sol.buildArray(*example_case_1)
        ['Push', 'Push', 'Pop', 'Push']

    Example 2:
        >>> sol.buildArray(*example_case_2)
        ['Push', 'Push', 'Push']

    Example 3:
        >>> sol.buildArray(*example_case_3)
        ['Push', 'Push']
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
