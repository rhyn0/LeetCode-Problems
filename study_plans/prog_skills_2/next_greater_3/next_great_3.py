class Solution:  # noqa: D101
    INT_MAX = 2_147_483_647

    def nextGreaterElement(self, num: int) -> int:
        """Find the smallest number that is greater than num.

        Also the number must be made up of the same digits as num.

        !!! The below does not get the correct answer. !!!

        Args:
            num (int): Number to find greater number for.

        Returns:
            int: -1 if there is no such number, else the greater number.
        """
        num_str = str(num)
        min_greater = float("inf")
        right = len(num_str) - 1
        left = right - 1
        while left != right and left >= 0:
            cmp_num = int(
                num_str[:left]
                + num_str[right]
                + num_str[left + 1 : right]
                + num_str[left]
                + num_str[right + 1 :]
            )
            if cmp_num > num:
                if cmp_num > self.INT_MAX:
                    return -1
                min_greater = min(min_greater, cmp_num)
            if left != 0:
                left -= 1
            else:
                right -= 1
        return -1 if min_greater == float("inf") else int(min_greater)

    def nextGreaterElementSolution(self, num: int) -> int:  # noqa: D102
        m = list(str(num))
        l = len(m)  # noqa: E741
        d = {}
        res = str(num)

        for i, c in enumerate(m[::-1]):
            if not d:
                d[c] = 1
            elif all(c >= x for x in d):
                d[c] = d.get(c, 0) + 1
            else:
                d[c] = d.get(c, 0) + 1
                res = "".join(m[: l - 1 - i])
                stock = sorted(d.keys())
                cplus = stock[stock.index(c) + 1]
                res += cplus
                d[cplus] -= 1
                res += "".join([x * d[x] for x in stock])
                break

        return int(res) if num < int(res) < (2**31 - 1) else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement(12))  # 21
    print(sol.nextGreaterElement(21))  # -1
    print(sol.nextGreaterElement(8))  # -1
