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
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        """Sort a given linked list into odd indices then followed by even indices.

        Uses constant space and linear time.

        Args:
            head (ListNode | None): Head of linked list if there are nodes

        Returns:
            ListNode | None: None if linked list of length 1 given,
                else sorted Linked list
        """
        curr = end = head
        if end is None:
            return None
        while end.next:
            end = end.next
        tail, prev, is_even = end, head, False
        if head.next is tail:
            return head
        while curr is not tail.next:
            # print("hi", curr, tail, prev, is_even, sep="--")
            if is_even:
                prev.next, curr.next, end.next, end, curr = (
                    curr.next,
                    None,
                    curr,
                    curr,
                    curr.next,
                )
                if end is tail:
                    break
                is_even = False
            else:
                prev, curr = curr, curr.next
                is_even = not is_even
        return head


def main() -> None:
    """Odd Even Linked List on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4,\
            ListNode(5))))))
        ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4, None)))))

    Example 2:
        >>> sol.oddEvenList(ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6,\
            ListNode(4, ListNode(7))))))))
        ListNode(2, ListNode(3, ListNode(6, ListNode(7, ListNode(1, ListNode(5,\
            ListNode(4, None)))))))

    Test 1:
        >>> sol.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,\
            ListNode(6, ListNode(7, ListNode(8)))))))))
        ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(2, ListNode(4, \
            ListNode(6, ListNode(8, None))))))))

    Test 2:
        >>> sol.oddEvenList(ListNode(1, ListNode(2)))
        ListNode(1, ListNode(2, None))
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
