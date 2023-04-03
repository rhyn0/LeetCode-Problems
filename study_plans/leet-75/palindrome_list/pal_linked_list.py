from __future__ import annotations

# Standard Library
import doctest


class ListNode:  # noqa: D101
    def __init__(self, val: int = 0, next_: ListNode | None = None):  # noqa: D107
        self.val = val
        self.next = next_

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode({self.val}, {self.next})"


class Solution:  # noqa: D101
    def isPalindrome(self, head: ListNode) -> bool:
        """Return whether given linked list is a palindrome or not.

        Args:
            head (ListNode): Head of linked list

        Returns:
            bool: True if palindrome, False otherwise
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next
        while prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        return True


def main():
    """Palindrome Linked List on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.isPalindrome(ListNode(1, ListNode(2)))
        False

    Example 2:
        >>> sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True

    Test 1:
        >>> sol.isPalindrome(ListNode(1, ListNode(2, ListNode(1, ListNode(2)))))
        False
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
