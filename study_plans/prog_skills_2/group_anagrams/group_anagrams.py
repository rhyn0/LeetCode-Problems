# Standard Library
from collections import Counter
from collections import defaultdict
import doctest


class Solution:  # noqa: D101
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:  # spec
        """Group anagrams together and return them as List of Lists.

        Given List of words, group the anagrams together

        Args:
            strs (List[str]): Bag of words

        Returns:
            List[List[str]]: Anagrams grouped together
        """
        count_dict = defaultdict(list)
        for anagram in strs:
            count_dict[frozenset(Counter(anagram).items())].append(anagram)
        return list(count_dict.values())


def main() -> None:
    """49. Group Anagrams on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
        >>> example_case_2 = [""]
        >>> example_case_3 = ["a"]

    Example 1:
        >>> sol.groupAnagrams(example_case_1)
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    Example 2:
        >>> sol.groupAnagrams(example_case_2)
        [['']]

    Example 3:
        >>> sol.groupAnagrams(example_case_3)
        [['a']]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
