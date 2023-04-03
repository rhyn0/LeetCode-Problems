class Solution:  # noqa: D101
    def lengthOfLastWord(self, s: str) -> int:  # spec
        """Return length of last word in a string.

        Word is given by set of characters not interrupted by spaces

        Args:
            s (str): String to parse

        Returns:
            int: Length of last word in string
        """
        # return len(s.split()[-1])
        curr_len, last = 0, 0
        for char in s:
            if char.isspace():
                if curr_len != 0:
                    curr_len, last = 0, curr_len
            else:
                curr_len += 1
        return curr_len or last


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("hello world"))  # 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))  # 6
