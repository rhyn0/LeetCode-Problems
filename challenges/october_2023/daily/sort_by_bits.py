"""Daily Challenge on LeetCode for October 30: Problem #1356 [Easy]."""
# Standard Library
from bisect import bisect_right
from collections import Counter
import doctest


class Solution:  # noqa: D101
    def sortByBits(self, arr: list[int]) -> list[int]:
        """Sort the given array of numbers by the number of 1 bits.

        Ties in count of 1 bits are broken by the number itself.
        """
        # turn each number into a binary string
        # prefer to not use bin() here to escape the leading '0b'
        counts = [(Counter(f"{n:b}")["1"], n) for n in arr]
        counts.sort()
        return [n for _, n in counts]

    @staticmethod
    def _count_bits(num: int) -> int:
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1

        return count

    def sortByBitsManipulation(self, arr: list[int]) -> list[int]:
        """Return same as above using bit manipulation."""
        # originally nested count_bits as a helper function
        # refactored to use in other solutions
        counts = [(self._count_bits(n), n) for n in arr]
        counts.sort()
        return [n for _, n in counts]

    def sortByBitsBinaryInsert(self, arr: list[int]) -> list[int]:
        """Return same as above using binary insertion sort."""
        keys = []
        output = []
        # keep a copy of the original array
        nums = sorted(arr)
        for num in nums:
            count = self._count_bits(num)
            # find the index where the count should be inserted
            # use bisect_right as the numbers are presorted in ascending order
            index = bisect_right(keys, count)
            # insert the count and the number at the same index
            keys.insert(index, count)
            output.insert(index, num)
        return output

    def sortByBitsBuiltin(self, arr: list[int]) -> list[int]:
        """Return same as above using built-in int.bit_count."""
        # use a lambda to sort by the count of 1 bits
        # then sort by the number itself
        return sorted(arr, key=lambda n: (n.bit_count(), n))

    def sortByBitsKernighan(self, arr: list[int]) -> list[int]:
        """Return same as above using Brian Kernighan Bit Count Algorithm."""

        def kernighan(num: int) -> int:
            # improvements by using AND logic instead of bit shift
            weight = 0
            while num > 0:
                weight += 1
                # this sets the right most bits to 0
                num &= num - 1
            return weight

        return sorted(arr, key=lambda n: (kernighan(n), n))


def main() -> None:
    """1356. Sort Integers by The Number of 1 Bits on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [0,1,2,3,4,5,6,7,8]
        >>> example_case_2 = [1024,512,256,128,64,32,16,8,4,2,1]

    Example 1:
        >>> sol.sortByBits(example_case_1)
        [0, 1, 2, 4, 8, 3, 5, 6, 7]
        >>> sol.sortByBitsManipulation(example_case_1)
        [0, 1, 2, 4, 8, 3, 5, 6, 7]
        >>> sol.sortByBitsBinaryInsert(example_case_1)
        [0, 1, 2, 4, 8, 3, 5, 6, 7]
        >>> sol.sortByBitsBuiltin(example_case_1)
        [0, 1, 2, 4, 8, 3, 5, 6, 7]
        >>> sol.sortByBitsKernighan(example_case_1)
        [0, 1, 2, 4, 8, 3, 5, 6, 7]

    Example 2:
        >>> sol.sortByBits(example_case_2)
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        >>> sol.sortByBitsManipulation(example_case_2)
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        >>> sol.sortByBitsBinaryInsert(example_case_2)
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        >>> sol.sortByBitsBuiltin(example_case_2)
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        >>> sol.sortByBitsKernighan(example_case_2)
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
