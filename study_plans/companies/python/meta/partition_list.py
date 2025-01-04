"""Meta Interview Question Practice List on LeetCode.

86. Partition List on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = ListNode.build_list([1,4,3,2,5,2]), 3
    >>> example_case_2 = ListNode.build_list([2,1]), 2
    >>> self_test_1 = ListNode.build_list([3,4,5]), 2

Example 1:
    >>> sol.partition(*example_case_1).to_list()
    [1, 2, 2, 4, 3, 5]

Example 2:
    >>> sol.partition(*example_case_2).to_list()
    [1, 2]

All values are greater than the partitioning point, shouldn't change.
Self Test 1:
    >>> sol.partition(*self_test_1).to_list()
    [3, 4, 5]
"""

# Standard Library
from typing import Self


class InvalidLinkedListError(Exception):
    """Exception for an empty Linked list conversion."""

    def __init__(self, nodes: list, *args: object) -> None:
        """Default message and pass though args."""
        super().__init__(f"Invalid definition: ({','.join(nodes)})", *args)


class ListNode:  # noqa: D101
    def __init__(self, val: int = 0, next: Self | None = None):  # noqa: A002, D107
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        """Debugging representation."""
        return f"ListNode({self.val}, {self.next})"

    @classmethod
    def build_list(cls, values: list[int]) -> Self:
        """Return constructed linked list from the values."""
        if not values:
            # intentinal None build
            raise InvalidLinkedListError(values)
        head = cls(values[0])
        curr_head = head
        for val in values[1:]:
            curr_head.next = cls(val)
            curr_head = curr_head.next
        return head

    def to_list(self) -> list[int]:
        """Output from current point to end as a list."""
        output = []
        head = self
        while head:
            output.append(head.val)
            head = head.next  # type: ignore[assignment]
        return output


class Solution:  # noqa: D101
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        """Return a single linked list where all values less than x come first.

        Preserve order other than partitioning to be less than or greater than equal.

        Args:
            head (ListNode | None): Head of original linked list if any
            x (int): Value of node to compare against

        Returns:
            ListNode | None: "Sorted" linked list
        """
        # extra pointers to hold onto the list properly
        # code is a little easier to read if we use dummy node heads
        less_head = less_tail = greater_head = greater_tail = None
        if not head:
            return None
        curr: ListNode | None = head
        while curr:
            # print(curr)
            next_node = curr.next
            curr.next = None
            if curr.val < x:
                if less_head is None:
                    less_head = less_tail = curr
                else:
                    less_tail.next = curr
                    less_tail = less_tail.next
            elif greater_head is None:
                greater_head = curr
                greater_tail = curr
            else:
                greater_tail.next = curr
                greater_tail = curr
            curr = next_node
        if less_tail is None:
            less_head = head
        else:
            less_tail.next = greater_head
        return less_head
