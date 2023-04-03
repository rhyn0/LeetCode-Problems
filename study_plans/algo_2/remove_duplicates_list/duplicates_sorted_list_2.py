from __future__ import annotations

# Standard Library
import doctest


class ListNode:  # noqa: D101
    def __init__(self, value: int = 0, next_: ListNode | None = None):  # noqa: D107
        self.val = value
        self.next = next_

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode({self.val}, {self.next})"


class Solution:  # noqa: D101
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """Remove all nodes that have a duplicate value from sorted linked list.

        Args:
            head (ListNode | None): head of sorted linked list

        Returns:
            ListNode | None: all duplicates removed
        """
        tmp_head = ListNode(0, head)
        prev = tmp_head
        while head is not None:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # next one has different value
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return tmp_head.next


def main():
    """Remove Duplicates from Sorted List II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.deleteDuplicates(ListNode(1, ListNode(2, ListNode(3, ListNode(3,\
            ListNode(4, ListNode(4, ListNode(5))))))))
        ListNode(1, ListNode(2, ListNode(5, None)))

    Example 2:
        >>> sol.deleteDuplicates(ListNode(1, ListNode(1, ListNode(1, ListNode(2,\
            ListNode(3))))))
        ListNode(2, ListNode(3, None))
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
