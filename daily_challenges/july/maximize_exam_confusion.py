"""Daily Challenge for July 7, 2023 on LeetCode."""
# Standard Library
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def maxConsecutiveAnswers(self, answer_key: str, k: int) -> int:
        """Return longest streak of the same character possible.

        Can change up to `k` characters to the opposite value.

        Args:
            answer_key (str): Initial state of character string
            k (int): Maximum allowed switches

        Returns:
            int: maximum consecutive answers
        """
        max_streak = 0
        counter = Counter()
        for i, value in enumerate(answer_key):
            counter[value] += 1

            least_commmon = min(counter["T"], counter["F"])
            if least_commmon <= k:
                max_streak += 1
            else:
                counter[answer_key[i - max_streak]] -= 1

        return max_streak

    def maxConsecutiveAnswersBinary(self, answer_key: str, k: int) -> int:
        """Return same as above using binary search for the streak size."""
        n = len(answer_key)

        def valid_streak_len(length: int) -> bool:
            counter = Counter(answer_key[:length])
            if min(counter["T"], counter["F"]) <= k:
                return True
            for right in range(length, n):
                counter[answer_key[right]] += 1
                counter[answer_key[right - length]] -= 1
                if min(counter["T"], counter["F"]) <= k:
                    return True
            return False

        left, right = 1, n
        best_streak = 0
        while left <= right:
            mid = (left + right) // 2
            if valid_streak_len(mid):
                # if valid, we want maximum len
                best_streak = mid
                left = mid + 1
            else:
                right = mid - 1
        return best_streak


def main() -> None:
    """2024. Maximize the Confusion of an Exam on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = "TTFF", 2
        >>> example_case_2 = "TFFT", 1
        >>> example_case_3 = "TTFTTFTT", 1

    Example 1:
        >>> sol.maxConsecutiveAnswers(*example_case_1)
        4
        >>> sol.maxConsecutiveAnswersBinary(*example_case_1)
        4

    Example 2:
        >>> sol.maxConsecutiveAnswers(*example_case_2)
        3
        >>> sol.maxConsecutiveAnswersBinary(*example_case_2)
        3

    Example 3:
        >>> sol.maxConsecutiveAnswers(*example_case_3)
        5
        >>> sol.maxConsecutiveAnswersBinary(*example_case_3)
        5
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
