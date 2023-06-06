from __future__ import annotations

# Standard Library
import doctest


class ListNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        value: int = 0,
        next_: ListNode | None = None,
    ) -> None:
        self.val = value
        self.next = next_

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode({self.val}, {self.next})"


class Solution:  # noqa: D101
    def addTwoNumbers(  # spec
        self,
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        """Sum two numbers represented as linked list.

        Linked list head is the most significant bit.
        Guaranteed to be no leading zeroes on linked list

        Args:
            l1 (ListNode | None): Number in linked list representation
            l2 (ListNode | None): Number in linked list representation

        Returns:
            ListNode | None: Result of addition in linked list representation
        """
        l1_stack, l2_stack = [], []
        while l1 or l2:
            if l1:
                l1_stack.append(l1.val)
                l1 = l1.next
            else:
                l1_stack.insert(0, 0)
            if l2:
                l2_stack.append(l2.val)
                l2 = l2.next
            else:
                l2_stack.insert(0, 0)

        carry, prev = 0, None
        for i in range(len(l1_stack) - 1, -1, -1):
            carry, rem = divmod(l1_stack[i] + l2_stack[i] + carry, 10)
            if prev is None:
                prev = ListNode(rem)
            else:
                new = ListNode(rem)
                new.next, prev = prev, new

        if carry:
            new = ListNode(carry)
            new.next, prev = prev, new

        return prev


def main() -> None:
    """Add Two Numbers II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4))))
        ListNode(7, ListNode(8, ListNode(0, ListNode(7, None))))

    Example 2:
        >>> sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
        ListNode(8, ListNode(0, ListNode(7, None)))

    Example 3:
        >>> sol.addTwoNumbers(ListNode(), ListNode())
        ListNode(0, None)

    Test 1:
        >>> sol.addTwoNumbers(ListNode(5), ListNode(5))
        ListNode(1, ListNode(0, None))
    """  # noqa: E501


if __name__ == "__main__":
    doctest.testmod(verbose=True)
