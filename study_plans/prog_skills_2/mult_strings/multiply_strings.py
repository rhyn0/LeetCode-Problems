class Solution:  # noqa: D101
    def multiply(self, num1: str, num2: str) -> str:
        """Multiply two strings representing numbers, return result as string.

        Iterative approach.

        Args:
            num1 (str): String representing first positive number
            num2 (str): String representing second positive number

        Returns:
            str: String representing result of multiplying the two numbers together.
        """
        total = 0
        for i, c1 in enumerate(reversed(num1)):
            temp_total, power, carry = 0, 10**i, 0
            c1_val = ord(c1) - ord("0") if c1 is not None else 1
            for c2 in reversed(num2):
                c2_val = ord(c2) - ord("0") if c2 is not None else 1

                temp_val = (c1_val * c2_val) + carry
                carry = temp_val // 10
                temp_val = temp_val % 10

                temp_total += temp_val * power
                power *= 10

            temp_total += carry * power
            total += temp_total
        return str(total)


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2", "3"))  # 6
    print(sol.multiply("123", "456"))  # 56088
