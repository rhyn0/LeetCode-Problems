# Standard Library
import doctest


class Solution:  # noqa: D101
    def longestCommonPrefix(self, strs: list[str]) -> str:  # spec
        """Return longest common prefix of all given strs.

        Args:
            strs (List[str]): List of strings to find prefix for

        Returns:
            str: longest common prefix of strings
        """
        ret = ""
        for tup in zip(*strs, strict=False):
            if len(set(tup)) == 1:
                ret += tup[0]
            else:
                break
        return ret

    def longestCommonPrefix2(self, strs: list[str]) -> str:  # spec
        """Return longest common prefix of all given strs.

        performance increase since working backwards for strings.

        Args:
            strs (List[str]): List of strings to find prefix for.

        Returns:
            str: longest commong prefix.
        """
        prefix = strs[0]
        for cmp_str in strs[1:]:
            if not prefix:
                break
            while prefix != cmp_str[: len(prefix)]:
                prefix = prefix[:-1]
        return prefix


def main():
    """Longest Common Prefix on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.longestCommonPrefix(["flower", "flow", "flight"])
        'fl'

    Example 2:
        >>> sol.longestCommonPrefix(["dog", "racecar", "car"])
        ''
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
