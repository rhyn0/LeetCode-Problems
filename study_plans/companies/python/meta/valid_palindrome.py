"""Meta Interview Question Practice List on LeetCode.

125. Valid Palindrome on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "A man, a plan, a canal: Panama"
    >>> example_case_2 = "race a car"
    >>> example_case_3 = " "

Example 1:
    >>> sol.isPalindrome(example_case_1)
    True
    >>> sol.isPalindromeTwoPoint(example_case_1)
    True

Example 2:
    >>> sol.isPalindrome(example_case_2)
    False
    >>> sol.isPalindromeTwoPoint(example_case_2)
    False

Example 3:
    >>> sol.isPalindrome(example_case_3)
    True
    >>> sol.isPalindromeTwoPoint(example_case_3)
    True
"""


class Solution:  # noqa: D101
    def isPalindrome(self, s: str) -> bool:
        """Return whether the given string is a valid palindrome.

        Ignore non-alphanumeric characters. Reminder that "" is a
        valid palindrome.

        Args:
            s (str): string to check for palindrome

        Returns:
            bool: True if is a palindrome, False otherwise
        """
        stripped = [c.lower() for c in s if c.isalnum()]
        n = len(stripped)
        return all(stripped[i] == stripped[n - i - 1] for i in range(n // 2))

    def isPalindromeTwoPoint(self, s: str) -> bool:
        """Return same as above using two pointer methodology."""
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left >= right:
                break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
