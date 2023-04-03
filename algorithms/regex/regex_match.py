# Standard Library
from itertools import product


class Solution:  # noqa: D101
    def isMatch_bad(self, in_str: str, pattern: str) -> bool:
        """Failed attempt at solving.

        I looked at the solutions and realized that
        dynamic programming is a good choice.
        Solutions covered a memoization problem, which is efficient
        since we don't need every possible step for the answer.
        Tradeoff being recursion vs iteration

        The below is a tabulation approach that I thought about later.
        """

        def re_match(s_char: str, p_char: str) -> bool:
            return p_char == "." or s_char == p_char

        s_pos, s_len = 0, len(in_str)
        p_pos, p_len = 0, len(pattern)
        ast_used = False
        while s_pos < s_len and p_pos < p_len:
            if re_match(in_str[s_pos], pattern[p_pos]):
                s_pos, p_pos = s_pos + 1, p_pos + 1
            elif pattern[p_pos] == "*":
                if not ast_used:
                    ast_used = True
                    p_pos -= 1
                else:
                    p_pos += 1
                    ast_used = False
            elif p_pos < p_len - 1 and pattern[p_pos + 1] == "*":
                # no usage of this char, skip
                p_pos += 2
            else:
                return False

        return s_pos >= s_len and (
            p_pos >= p_len or pattern.find("*", p_pos) + 1 >= p_len
        )

    def isMatch(self, text: str, pattern: str) -> bool:  # spec
        """Return whether regex pattern would match against whole string.

        Use tabulation to find answer

        Args:
            text (str): Text to match
            pattern (str): Pattern to use as regex match

        Returns:
            bool: True if regex matches whole string, otherwise False
        """
        truth_table = [
            [False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)
        ]

        truth_table[0][0] = True  # empty string matches with empty string

        for col, char in enumerate(pattern, start=1):  # 1 indexed string
            if char == "*":
                truth_table[0][col] = truth_table[0][col - 2]
        # for i, s_char in enumerate(text, start=1):
        #     for j, p_char in enumerate(pattern, start=1):
        for (i, s_char), (col, p_char) in product(
            enumerate(text, start=1), enumerate(pattern, start=1)
        ):
            if p_char in {s_char, "."}:
                truth_table[i][col] = truth_table[i - 1][col - 1]
            elif p_char == "*":
                truth_table[i][col] = truth_table[i][col - 2] or (
                    pattern[col - 2] in {s_char, "."} and truth_table[i - 1][col]
                )
            else:
                truth_table[i][col] = False
        return truth_table[len(text)][len(pattern)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))  # False
    print(sol.isMatch("aa", "a*"))  # True
    print(sol.isMatch("ab", ".*"))  # True
    print(sol.isMatch("aab", "c*a*b*"))  # True
    print(sol.isMatch("aab", "c*a*b"))  # True
    print(sol.isMatch("ab", ".*c"))  # False
