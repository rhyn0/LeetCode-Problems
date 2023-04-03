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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode | None:
        """Return linked list with nth node from end removed.

        Uses two pointers to find that location

        Args:
            head (ListNode): Linked list head
            n (int): node from end to remove

        Returns:
            ListNode | None: Linked list with node removed, or None if only node removed
        """
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            # must be len == n, remove first
            return head.next
        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return head


def main():
    """Remove Nth Node from List on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.removeNthFromEnd(ListNode(1), 1)

    Example 2:
        >>> sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4,\
            ListNode(5))))), 2)
        ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))

    Example 3:
        >>> sol.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
        ListNode(1, None)
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
