# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def lemonadeChange(self, bills: list[int]) -> bool:  # spec
        """Run a lemonade stand with exact change.

        Only accept 5, 10, 20 dollar bills. A lemonade costs 5 dollars.

        Args:
            bills (List[int]): List of customers and what bills they pay with

        Returns:
            bool: True if able to give exact change for everyone, False otherwise
        """
        five_bill, ten_bill = 5, 10
        change_d = defaultdict(int)
        for bill in bills:
            # print(change_d, bill)
            if bill == five_bill:
                # no change necessary
                pass
            elif bill == ten_bill:
                if not change_d[five_bill]:
                    return False
                change_d[five_bill] -= 1
            # below cases are for 20 dollar bill
            elif change_d[ten_bill] and change_d[5]:
                change_d[ten_bill] -= 1
                change_d[five_bill] -= 1
            elif change_d[five_bill] >= 3:  # noqa: PLR2004 # fifteen dollars
                change_d[five_bill] -= 3
            else:
                return False
            change_d[bill] += 1
        return True


def main():
    """Lemonade Change on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.lemonadeChange([5, 5, 5, 10, 20])
        True

    Example 2:
        >>> sol.lemonadeChange([5,5,10,10,20])
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
