"""Weekly Challenge on LeetCode: Problem #2355 [Hard]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def maximumBooks(self, books: list[int]) -> int:
        """Return maximum number of books that can be taken from the given shelves.

        Shelves must be taken from contiguously. For shelf i, the number of books
        taken must be strictly greater than the number of shelves taken on shelf i - 1.

        Args:
            books (list[int]): Number of books per shelf.

        Returns:
            int: Maximum number of books per shelf.
        """

        def calculateSum(left: int, right: int) -> int:
            # If only considering this shelf (left == right) sum is books[right]
            # otherwise, we get books[right] + books[right - 1] - 1 + ...
            # which is (books[right - 0] - 0) + ...
            # which is (books[i - j] - j) + ...
            # maximized only when difference between elements is 1
            # so we can turn this into a square plus triangle to get final formula
            cnt = min(books[right], right - left + 1)
            return (2 * books[right] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * len(books)
        for i in range(len(books)):
            # pop while items cause the sequence to be decreasing
            while stack and books[stack[-1]] - stack[-1] > books[i] - i:
                stack.pop()

            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                dp[i] = dp[stack[-1]] + calculateSum(stack[-1] + 1, i)

            stack.append(i)

        return max(dp)


def main() -> None:
    """2355. Maximum Number of Books You Can Take on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [8,5,2,7,9]
        >>> example_case_2 = [7,0,3,4,5]
        >>> example_case_3 = [8,2,3,7,3,4,0,1,4,3]

    Example 1:
        >>> sol.maximumBooks(example_case_1)
        19

    Example 2:
        >>> sol.maximumBooks(example_case_2)
        12

    Example 3:
        >>> sol.maximumBooks(example_case_3)
        13
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
