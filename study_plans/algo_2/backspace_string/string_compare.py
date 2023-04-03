# Standard Library
from collections.abc import Generator
import doctest
from itertools import zip_longest


class Solution:  # noqa: D101
    def backspaceCompare(self, string: str, test: str) -> bool:  # spec
        """Return whether given strings are equal after evaluating backspaces.

        The character '#' denotes a backspace.
        Deleting empty text will cause it to be blank.

        Args:
            string (str): given string
            test (str): Comparator string

        Returns:
            bool: True if equal after backspaces, False otherwise
        """
        s_skip, t_skip = 0, 0
        new_s, new_t = [], []
        for s_ch, t_ch in zip_longest(reversed(string), reversed(test), fillvalue=""):
            if s_ch == "#":
                s_skip += 1
            elif not s_skip and s_ch:
                new_s.append(s_ch)
            else:
                s_skip -= 1

            if t_ch == "#":
                t_skip += 1
            elif not t_skip and t_ch:
                new_t.append(t_ch)
            else:
                t_skip -= 1
        # print("".join(new_s), "".join(new_t), sep="\n" + "=" * 10 + "\n")
        return all(sch == tch for sch, tch in zip_longest(new_s, new_t))

    def backspaceCompareGen(self, string: str, test: str) -> bool:  # noqa: D102
        def string_build(in_str: str) -> Generator[str, None, None]:
            skip_ch = 0
            for ch in reversed(in_str):
                if ch == "#":
                    skip_ch += 1
                elif skip_ch:
                    skip_ch -= 1
                else:
                    yield ch

        return all(
            sch == tch
            for sch, tch in zip_longest(string_build(string), string_build(test))
        )


def main():
    """Backspace Compare String on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.backspaceCompare("ab#c", "ad#c")
        True

    Example 2:
        >>> sol.backspaceCompare("ab##", "c#d#")
        True

    Example 3:
        >>> sol.backspaceCompare("a#c", "b")
        False

    Test 1:
        >>> sol.backspaceCompare("xywrrmp", "xywrrmu#p")
        True

    Example 1:
        >>> sol.backspaceCompareGen("ab#c", "ad#c")
        True

    Example 2:
        >>> sol.backspaceCompareGen("ab##", "c#d#")
        True

    Example 3:
        >>> sol.backspaceCompareGen("a#c", "b")
        False

    Test 1:
        >>> sol.backspaceCompareGen("xywrrmp", "xywrrmu#p")
        True
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
