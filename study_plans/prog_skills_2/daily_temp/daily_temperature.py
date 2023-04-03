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


if __name__ == "__main__":
    """This is a slow implementation and not a fully optimized one.

    Should have iterated from the back.
    """
    sol = Solution()
    print(
        sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    )  # [1, 1, 4, 2, 1, 1, 0, 0]
    print(sol.dailyTemperatures([30, 40, 50, 60]))  # [1, 1, 1, 0]
    print(sol.dailyTemperatures([30, 60, 90]))  # [1, 1, 0]
