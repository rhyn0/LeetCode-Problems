from __future__ import annotations

# Standard Library
import doctest


class ListNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        next_: ListNode | None = None,
    ) -> None:
        self.val = val
        self.next = next_

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode({self.val}, {self.next})"


class Solution:  # noqa: D101
    def sortList(self, head: ListNode | None) -> ListNode | None:  # spec
        """Given singly linked list, return it sorted in ascending order.

        Uses O(log n) space due to recursion

        Args:
            head (ListNode | None): Linked list, or None if no nodes

        Returns:
            ListNode | None: Sorted linked list, or None if no input
        """

        def merge_sort(f_head: ListNode) -> ListNode:
            if f_head.next is None:
                return f_head

            slow, fast = f_head, f_head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            sec_head, slow.next = slow.next, None
            f_head, sec_head = merge_sort(f_head), merge_sort(sec_head)
            dummy = ListNode()
            tail = dummy
            while f_head and sec_head:
                if f_head.val > sec_head.val:
                    tail.next = sec_head
                    sec_head.next, sec_head = None, sec_head.next
                else:
                    tail.next = f_head
                    f_head.next, f_head = None, f_head.next
                tail = tail.next
            tail.next = f_head or sec_head
            return dummy.next

        if head is None:
            return None
        return merge_sort(head)


def main() -> None:
    """Sort List on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

    Example 2:
        >>> sol.sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))
        ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5, None)))))
    """  # noqa: E501


if __name__ == "__main__":
    doctest.testmod(verbose=True)
