from __future__ import annotations

# Standard Library
import doctest


class ListNode:  # noqa: D101
    def __init__(self, value=0, _next: ListNode | None = None):  # noqa: D107
        self.val = value
        self.next = _next

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode({self.val}, {self.next})"


class Solution:  # noqa: D101
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        """Rotate a linked list to the right by k positions.

        [0, 1, 2] with k = 1 -> [2, 0, 1]
        k can be greater than length of given linked list

        Args:
            head (ListNode | None): Linkedlist to rotate, None if list is empty
            k (int): Number of positions to rotate list

        Returns:
            ListNode | None: LinkedList after rotation, can be None if None was supplied
        """
        if head is None or k == 0:
            return head
        slow = fast = head
        n_length = 0
        while fast:
            if n_length > k:
                slow = slow.next
            n_length += 1
            if fast.next is None:
                fast.next = head
                break
            fast = fast.next
        if n_length == k:
            fast.next = None
            return head
        if n_length > k:
            new_head = slow.next
            slow.next = None
            return new_head
        count, slow = 1, head
        while count < n_length - (k % n_length):
            slow = slow.next
            count += 1
        new_head = slow.next
        slow.next = None
        return new_head


def main():
    """Rotate List on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
        ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3, None)))))

    Example 2:
        >>> sol.rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4)
        ListNode(2, ListNode(0, ListNode(1, None)))

    Test 1:
        >>> sol.rotateRight(None, 1) # None

    Test 2:
        >>> sol.rotateRight(ListNode(1), 1)
        ListNode(1, None)

    Test 3:
        >>> sol.rotateRight(ListNode(1, ListNode(2)), 3)
        ListNode(2, ListNode(1, None))
    """  # noqa: E501


if __name__ == "__main__":
    doctest.testmod(verbose=True)
