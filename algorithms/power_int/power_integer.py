class Solution:
    """Answer attempt for Power Integer from LeetCode."""

    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        """Return list of numbers that can be made from unique powers using x, y."""

        def find_powers(x_pow: int, y_pow: int) -> None:
            num = x**x_pow + y**y_pow
            if (
                num <= bound
                and (x_pow, y_pow, num) not in power_list
                and (y_pow, x_pow, num) not in power_list
            ):
                power_list.add((x_pow, y_pow, num))
            else:
                # num has gone outside bound so we must stop
                return
            if x != 1:
                find_powers(x_pow + 1, y_pow)
            if y != 1:
                find_powers(x_pow, y_pow + 1)

        power_list = set()
        find_powers(0, 0)
        return list({item[2] for item in power_list})
