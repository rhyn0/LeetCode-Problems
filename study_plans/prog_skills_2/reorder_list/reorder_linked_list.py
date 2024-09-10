from __future__ import annotations

# Standard Library
import doctest


class ListNode:  # noqa: D101
    def __init__(  # noqa: D107
        self,
        val: int = 0,
        _next: ListNode | None = None,
    ) -> None:
        self.val = val
        self.next = _next

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode({self.val}, {self.next})"


class Solution:  # noqa: D101
    def reorderList(self, head: ListNode) -> None:
        """Reorder given linked list to alternate from head to tail.

        So 1 -> 2 -> 3 -> 4 changes to be  1 -> 4 -> 2 -> 3.

        Args:
            head (ListNode): Head of given linked list to alter
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # beginning of second half
        prev = slow.next = None  # unlink first half from second
        while second is not None:
            second.next, prev, second = prev, second, second.next

        # prev is now the "tail" of linked list, but it is reversed
        first_h, sec_h = head, prev
        while sec_h is not None:
            first_h.next, sec_h.next, first_h, sec_h = (
                sec_h,
                first_h.next,
                first_h.next,
                sec_h.next,
            )


def main() -> None:
    """Reorder List from LeetCode.

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> lnode = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        >>> sol.reorderList(lnode)
        >>> print(lnode)
        ListNode(1, ListNode(4, ListNode(2, ListNode(3, None))))

    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
