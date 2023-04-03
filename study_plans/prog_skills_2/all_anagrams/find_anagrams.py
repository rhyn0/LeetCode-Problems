# Standard Library
from collections import Counter


class Solution:  # noqa: D101
    def findAnagrams(self, s: str, p: str) -> list[int]:  # spec
        """Given random characters ``s``, return indices where anagrams of ``p`` occur.

        Anagrams are scramblings of the same count and characters of a different phrase.

        Args:
            s (str): Ramble of characters
            p (str): Match the anagrams to this

        Returns:
            List[int]: List of indices
        """
        if len(p) > len(s):
            return []
        p_len, p_count, s_count = len(p), Counter(p), Counter(s[: len(p)])
        ret_list = [0] if p_count == s_count else []
        for left, char in enumerate(s[p_len:], start=0):
            s_count.subtract(s[left])
            s_count.update(char)
            if p_count == s_count:
                ret_list.append(left + 1)
        return ret_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print(sol.findAnagrams("abab", "ab"))  # [0, 1, 2]
