"""Meta Interview Question Practice List on LeetCode.

25. Reverse Nodes in k-Group on LeetCode.

====================================================

Setup:
    >>> from copy import deepcopy
    >>> sol = Solution()
    >>> example_case_1 = ListNode.build_list([1,2,3,4,5]), 2
    >>> example_case_2 = ListNode.build_list([1,2,3,4,5]), 3
    >>> test_case_1 = ListNode.build_list([1,2]), 2

Example 1:
    >>> sol.reverseKGroup(*deepcopy(example_case_1)).to_list()
    [2, 1, 4, 3, 5]
    >>> sol.reverseKGroupNoSpace(*deepcopy(example_case_1)).to_list()
    [2, 1, 4, 3, 5]

Example 2:
    >>> sol.reverseKGroup(*deepcopy(example_case_2)).to_list()
    [3, 2, 1, 4, 5]
    >>> sol.reverseKGroupNoSpace(*deepcopy(example_case_2)).to_list()
    [3, 2, 1, 4, 5]

Test 1:
    >>> sol.reverseKGroup(*deepcopy(test_case_1)).to_list()
    [2, 1]
    >>> sol.reverseKGroupNoSpace(*deepcopy(test_case_1)).to_list()
    [2, 1]
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
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """Reverse each group of `k` nodes in the list and return.

        Args:
            head (ListNode | None): Original linked list to reverse
            k (int): Size of the groups to reverse inside

        Returns:
            ListNode | None: Output list, if there is one.
        """
        if head is None:
            return head
        stack: list[ListNode] = []
        ret_head = ret_tail = curr_head = head
        first_done = False
        while True:
            while curr_head and len(stack) < k:
                stack.append(curr_head)
                temp = curr_head
                curr_head = curr_head.next
                temp.next = None

            if len(stack) < k:
                # have hit the end of the list and can't reverse this group
                break
            while stack:
                if first_done:
                    ret_tail.next = stack.pop()
                    ret_tail = ret_tail.next
                else:
                    first_done = True
                    ret_tail = ret_head = stack.pop()

        for node in stack:
            # if there are leftovers make sure to link the tail to it
            ret_tail.next = node
            ret_tail = node
        return ret_head

    def reverseKGroupNoSpace(self, head: ListNode | None, k: int) -> ListNode | None:
        """Return the same as above using constant space."""

        def reverse_k_nodes(head: ListNode, num_nodes: int) -> ListNode:
            new_head, ptr = None, head
            while num_nodes:
                # track next node
                next_node = ptr.next
                # point current.next to the head of reversed list
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                num_nodes -= 1
            return new_head

        curr_head = head
        tail = ret_head = None
        while curr_head:
            count = 0
            curr_head = head
            while curr_head and count < k:
                count += 1
                curr_head = curr_head.next
            if count < k:
                # hit end of linked list before filling group, out
                break
            rev_head = reverse_k_nodes(head, k)
            if not ret_head:
                ret_head = rev_head
            if tail:
                tail.next = rev_head

            # update tail to be end of reversed section
            tail = head
            head = curr_head
        # ensure disconnect didn't happen
        if tail:
            tail.next = head
        # possible that the list is shorter than k and we make no changes
        return ret_head if ret_head else head
