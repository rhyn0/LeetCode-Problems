"""Daily Challenge for July 1, 2023 on LeetCode."""

# Standard Library
import doctest


class Solution:  # noqa: D101
    MAX_INT = 10**9

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        """Return the minimum unfairness of a distribution of cookies to `k` kids.

        Each 'cookie' in `cookies` is a bag and can not be broken apart.
        All bags must be distributed. Unfairness is the maximum number
        of cookies any one child ends up with.

        Args:
            cookies (list[int]): array of cookie bag sizes
            k (int): number of children to distribute to

        Returns:
            int: minimum unfairness
        """
        curr_children = [0] * k
        n = len(cookies)

        def backtrack(cookie_idx: int, zero_children: int) -> int:
            # dont go down this branch since not enough cookies for all children
            if n - cookie_idx < zero_children:
                return self.MAX_INT

            if cookie_idx == n:
                return max(curr_children)
            answer = self.MAX_INT
            for i in range(k):
                # if this removes a zero child
                zero_children -= int(bool(curr_children[i] == 0))
                curr_children[i] += cookies[cookie_idx]
                answer = min(answer, backtrack(cookie_idx + 1, zero_children))

                # reset for next iteration
                curr_children[i] -= cookies[cookie_idx]
                zero_children += int(bool(curr_children[i] == 0))
            return answer

        return backtrack(0, k)

    def distributeCookiesBranchBound(self, cookies: list[int], k: int) -> int:
        """Return same as above using a different bounding method."""
        curr_children = [0] * k
        n = len(cookies)
        min_unfairness = self.MAX_INT
        # sorting gives us the best possibility to try a one item partition
        cookies.sort(reverse=True)

        def backtrack(cookie_idx: int, unfairness: int) -> None:
            # dont go down this branch since not enough cookies for all children
            nonlocal min_unfairness
            # bound is based on current known min_unfairness
            if unfairness >= min_unfairness:
                return

            if cookie_idx == n:
                min_unfairness = unfairness
                return

            for i in range(k):
                curr_children[i] += cookies[cookie_idx]
                curr_unfairness = max(unfairness, curr_children[i])
                backtrack(cookie_idx + 1, curr_unfairness)

                # reset for next iteration
                curr_children[i] -= cookies[cookie_idx]
                # this can best stop redoing a top-level check.
                # redistributing the first cookie bag to all `k` kids is a waste
                if curr_children[i] == 0:
                    break

        backtrack(0, 0)
        return min_unfairness


def main() -> None:
    """2305. Fair Distribution of Cookies on LeetCode.

    ====================================================

    Setup:
        >>> from copy import deepcopy
        >>> sol = Solution()
        >>> example_case_1 = [8,15,10,20,8], 2
        >>> example_case_2 = [6,1,3,2,2,4,1,2], 3

    Example 1:
        >>> sol.distributeCookies(*example_case_1)
        31
        >>> sol.distributeCookiesBranchBound(*deepcopy(example_case_1))
        31

    Example 2:
        >>> sol.distributeCookies(*example_case_2)
        7
        >>> sol.distributeCookiesBranchBound(*deepcopy(example_case_2))
        7
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
