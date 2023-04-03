from __future__ import annotations


# Definition for singly-linked list.
class ListNode:  # noqa: D101
    def __init__(self, value=0, next_: ListNode | None = None):  # noqa: D107
        self.val = value
        self.next = next_

    def __repr__(self) -> str:  # noqa: D105
        return f"ListNode(val: {self.val}, next: {self.next})"


# Definition for a binary tree node.
class TreeNode:  # noqa: D101
    def __init__(  # noqa: D107
        self, value=0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:  # noqa: D105
        return f"TreeNode(val: {self.val}\nleft: {self.left}, right: {self.right})"


class Solution:  # noqa: D101
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:  # spec
        """Given a linked list, find if it is present in the given tree.

        Find possible matches to head of list and then DFS on those matches at the end.

        Args:
            head (ListNode): Linked list representation
            root (TreeNode): Binary tree to search through

        Returns:
            bool: True if path exists, False otherwise.
        """

        def check_pos_match(l_head: ListNode | None, t_root: TreeNode | None) -> bool:
            if l_head is None:
                return True
            if t_root is None:
                return False
            if l_head.val == t_root.val:
                return check_pos_match(l_head.next, t_root.left) or check_pos_match(
                    l_head.next, t_root.right
                )
            return False

        def find_pos_match(head_val: int, t_root: TreeNode | None) -> list[TreeNode]:
            if t_root is None:
                return []
            elem = []
            if head_val == t_root.val:
                elem.append(t_root)
            return (
                elem
                + find_pos_match(head_val, t_root.left)
                + find_pos_match(head_val, t_root.right)
            )

        return any(
            check_pos_match(head, match) for match in find_pos_match(head.val, root)
        )


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.isSubPath(
            ListNode(4, ListNode(2, ListNode(8))),
            TreeNode(
                1,
                left=TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
                right=(
                    TreeNode(
                        4,
                        left=TreeNode(
                            2,
                            left=TreeNode(6),
                            right=TreeNode(8, left=TreeNode(1), right=TreeNode(3)),
                        ),
                    )
                ),
            ),
        ),
    )  # True
    print(
        sol.isSubPath(
            ListNode(1, ListNode(4, ListNode(2, ListNode(6)))),
            TreeNode(
                1,
                left=TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
                right=(
                    TreeNode(
                        4,
                        left=TreeNode(
                            2,
                            left=TreeNode(6),
                            right=TreeNode(8, left=TreeNode(1), right=TreeNode(3)),
                        ),
                    )
                ),
            ),
        )
    )  # True
