# Standard Library
from collections import Counter
from collections import defaultdict


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


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    )  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams([""]))  # [[""]]
    print(sol.groupAnagrams(["a"]))  # [["a"]]
