class Solution:  # noqa: D101
    def repeatedSubstringPattern(self, in_str: str) -> bool:  # spec
        """Return if there if s is made up of a repeated substr.

        Contiguous substring, must be more than one repeat.

        Args:
            in_str (str): Original string possibly made up of a repeated pattern

        Returns:
            bool: True if made up of repeated pattern, False otherwise
        """
        s_len = len(in_str)
        for substr_len in reversed(range(1, s_len // 2 + 1)):
            if (s_len / substr_len).is_integer():
                substr = in_str[:substr_len]
                if substr * (s_len // substr_len) == in_str:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))  # True
    print(sol.repeatedSubstringPattern("aba"))  # False
    print(sol.repeatedSubstringPattern("abcabcabcabc"))  # True
