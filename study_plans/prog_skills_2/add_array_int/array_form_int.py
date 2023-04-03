# Standard Library
from itertools import zip_longest


class Solution:  # noqa: D101
    def addToArrayForm(self, num: list[int], addend: int) -> list[int]:
        """Add integer ``k`` to array form integer, return answer in array form.

        Array form shows MSB left to right.

        Args:
            num (List[int]): Number in array format
            addend (int): integer to add

        Returns:
            List[int]: Answer of addition in array format
        """
        ret_list, carry = [], 0
        for num_i, k_i in zip_longest(
            reversed(num), reversed(str(addend)), fillvalue="0"
        ):
            total = int(num_i) + int(k_i) + carry

            carry, total = divmod(total, 10)  # this is cool
            ret_list.append(total)

        if carry:
            ret_list.append(carry)

        return ret_list[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.addToArrayForm([1, 2, 0, 0], 34))  # [1, 2, 3, 4]
    print(sol.addToArrayForm([2, 7, 4], 181))  # [4, 5, 5]
    print(sol.addToArrayForm([2, 1, 5], 806))  # [1, 0, 2, 1]
    print(
        sol.addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1)
    )  # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
