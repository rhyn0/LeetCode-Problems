class Solution:  # noqa: D101
    def strStr(self, haystack: str, needle: str) -> int:  # spec
        """Find the string needle in the given string haystack.

        Manual implementation of str.index it seems.

        Args:
            haystack (str): Long string to search in
            needle (str): string target to find

        Returns:
            int: Position of needle in haystack, -1 if it doesn't exist.
        """
        if len(needle) == 0:
            return 0
        endpoint = -len(needle) + 1 or None
        for i, char in enumerate(haystack[slice(endpoint)]):
            if char == needle[0] and haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("hello", "ll"))  # 2
    print(sol.strStr("aaaaa", "bba"))  # -1
    print(sol.strStr("aaa", ""))  # 0
    print(sol.strStr("a", "a"))  # 0
