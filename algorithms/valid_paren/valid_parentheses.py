class Solution:  # noqa: D101
    def isValid(self, in_str: str) -> bool:  # spec
        """Return if string is a valid set of open/close parentheses.

        Valid only if each pair is open closed in order and with itself.

        Args:
            in_str (str): string of only parentheses

        Returns:
            bool: True if valid, False otherwise
        """
        stack = []
        open_close_pairs = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        for char in in_str:
            if char in open_close_pairs:
                stack.append(char)
            elif len(stack) and char == open_close_pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))  # true
    print(sol.isValid("()[]{}"))  # true
    print(sol.isValid("(]"))  # false
    print(sol.isValid("{"))  # false
    print(sol.isValid("}"))  # false
