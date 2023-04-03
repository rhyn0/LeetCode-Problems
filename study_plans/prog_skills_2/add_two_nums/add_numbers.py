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
    def addTwoNumbers(  # spec
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """Add two Linked Lists representing numbers.

        The head of each list is the least significant digit.
        Guaranteed that there are no leading zeroes

        Args:
            l1 (ListNode | None): First number as linked list
            l2 (ListNode | None): Second number as linked list

        Returns:
            ListNode | None: Result number as linked list
        """
        carry, head = 0, ListNode()
        prev = head
        while l1 and l2:
            prev.next = ListNode((l1.val + l2.val + carry) % 10)
            carry, prev = (l1.val + l2.val + carry) // 10, prev.next
            l1, l2 = l1.next, l2.next

        if l1:
            div, rem = divmod(l1.val + carry, 10)
            l1.val = rem
            carry, prev.next = div, l1
            prev = l1
        elif l2:
            div, rem = divmod(l2.val + carry, 10)
            l2.val = rem
            carry, prev.next = div, l2
            prev = l2

        while carry:
            if prev.next is not None:
                prev.next.val, carry = (prev.next.val + carry) % 10, (
                    prev.next.val + carry
                ) // 10
                prev = prev.next
            else:
                prev.next = ListNode(carry)
                carry = 0

        return head.next


def main():
    """Add Two Numbers on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
        ListNode(7, ListNode(0, ListNode(8, None)))

    Example 2:
        >>> sol.addTwoNumbers(ListNode(), ListNode())
        ListNode(0, None)

    Example 1:
        >>> sol.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9)))), ListNode(9, ListNode(9)))
        ListNode(8, ListNode(9, ListNode(0, ListNode(0, ListNode(1, None)))))
    """  # noqa: E501


if __name__ == "__main__":
    doctest.testmod(verbose=True)
