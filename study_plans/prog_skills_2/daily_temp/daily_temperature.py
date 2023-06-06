# Standard Library
import doctest


class Solution:  # noqa: D101
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Return the number of days until warmer temperature.

        For each temperature in given array, return an array.

        Slow, O(n^2) in worst cases.

        Args:
            temperatures (List[int]): Temperature list

        Returns:
            List[int]: List of number of days for each day to get a hotter temperature
        """
        if len(temperatures) == 1:
            return [0]
        prev, decr = temperatures[0], -1
        ret_list = []
        for i, val in enumerate(temperatures[1:], start=1):
            if val > prev:
                ret_list.append(1)
                prev_day = i - 1

                while decr >= 0 and prev_day >= decr:
                    if ret_list[prev_day] == 0:
                        if temperatures[prev_day] < val:
                            ret_list[prev_day] = i - prev_day
                        else:
                            break
                    prev_day -= 1
                if ret_list[decr] != 0:
                    decr = -1

            else:
                ret_list.append(0)
                decr = i - 1 if decr == -1 else decr
            prev = val
        ret_list.append(0)  # last item is always zero
        return ret_list


def main() -> None:
    """739. Daily Temperatures on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [73, 74, 75, 71, 69, 72, 76, 73]
        >>> example_case_2 = [30, 40, 50, 60]
        >>> example_case_3 = [30, 60, 90]

    Example 1:
        >>> sol.dailyTemperatures(example_case_1)
        [1, 1, 4, 2, 1, 1, 0, 0]

    Example 2:
        >>> sol.dailyTemperatures(example_case_2)
        [1, 1, 1, 0]

    Example 3:
        >>> sol.dailyTemperatures(example_case_3)
        [1, 1, 0]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
