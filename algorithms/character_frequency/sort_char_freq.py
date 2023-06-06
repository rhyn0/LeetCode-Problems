# Standard Library
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def frequencySort(self, string_input: str) -> str:  # spec
        """Return sorted string in descending order of character frequency.

        Character frequency as number of times a character appears.
        'A' and 'a' are different characters

        Args:
            string_input (str): original string

        Returns:
            str: sorted string
        """
        # could use Counter too
        char_freq = defaultdict(int)
        for char in string_input:
            char_freq[char] += 1

        bucket_freq = [[] for _ in range(max(char_freq.values()))]
        for char, freq in char_freq.items():
            bucket_freq[freq - 1].append(char)

        return "".join(
            reversed(
                [
                    char * bucket
                    for bucket, char_list in enumerate(bucket_freq, start=1)
                    for char in char_list
                ],
            ),
        )


def main() -> None:
    """Sort Characters by Frequency on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.frequencySort("tree")
        'eert'

    Example 2:
        >>> sol.frequencySort("cccaaa")
        'aaaccc'

    Example 3:
        >>> sol.frequencySort("Aabb")
        'bbaA'

    Test 1:
        >>> sol.frequencySort("raaeaedere")
        'eeeeaaarrd'
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
