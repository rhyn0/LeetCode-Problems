"""Daily Challenge for June 7, 2023 on LeetCode."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def minFlips(self, a: int, b: int, c: int) -> int:
        """Return number of flips so that a|b == c.

        Operation is that a OR b would be equal to c.
        How many individual bits need to be flipped?

        Args:
            a (int): a
            b (int): b
            c (int): c

        Returns:
            int: minimum number of bits flipped
        """
        num_flips = 0
        bit_1 = 1
        while any(val > 0 for val in (a, b, c)):
            if c & bit_1:
                # need to make a flip if lowest bit not set when c's is
                num_flips += int(not (a & bit_1 or b & bit_1))
            else:
                # both need to be 0, so one flip for each that isn't
                num_flips += int(a & bit_1 != 0) + int(b & bit_1 != 0)
            a, b, c = a >> 1, b >> 1, c >> 1
        return num_flips

    def minFlipsXOR(self, a: int, b: int, c: int) -> int:
        """Return same as above using bit counting."""
        # first number of mismatches, then number of double zero mismatch
        # be careful, XOR has higher priority than OR
        return bin((a | b) ^ c).count("1") + bin(a & b & ((a | b) ^ c)).count("1")

    def minFlipsXOR2(self, a: int, b: int, c: int) -> int:
        """Return same as above using bit counting."""
        # first number of mismatches, then number of double zero mismatch
        return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()


def main() -> None:
    """1318. Minimum Flips to Make a OR b Equal to c on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = 2, 6, 5
        >>> example_case_2 = 4, 2, 7
        >>> example_case_3 = 1, 2, 3
        >>> self_test_1 = 1, 2, 2
        >>> test_case_1 = 8, 3, 5

    Example 1:
        >>> sol.minFlips(*example_case_1)
        3
        >>> sol.minFlipsXOR(*example_case_1)
        3
        >>> sol.minFlipsXOR2(*example_case_1)
        3

    Example 2:
        >>> sol.minFlips(*example_case_2)
        1
        >>> sol.minFlipsXOR(*example_case_2)
        1
        >>> sol.minFlipsXOR2(*example_case_2)
        1

    Example 3:
        >>> sol.minFlips(*example_case_3)
        0
        >>> sol.minFlipsXOR(*example_case_3)
        0
        >>> sol.minFlipsXOR2(*example_case_3)
        0

    Self Test 1:
        >>> sol.minFlips(*self_test_1)
        1
        >>> sol.minFlipsXOR(*self_test_1)
        1
        >>> sol.minFlipsXOR2(*self_test_1)
        1

    Test 1:
        >>> sol.minFlips(*test_case_1)
        3
        >>> sol.minFlipsXOR(*test_case_1)
        3
        >>> sol.minFlipsXOR2(*test_case_1)
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
