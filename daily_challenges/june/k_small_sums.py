"""Daily Challenge for June 27, 2023 on LeetCode."""

# Standard Library
import doctest
import heapq


class Solution:  # noqa: D101
    def kSmallestPairs(
        self,
        nums1: list[int],
        nums2: list[int],
        k: int,
    ) -> list[list[int]]:
        """Return the `k` smallest pairs created from the provided arrays.

        Each pair must be of the form (nums1[i], nums2[j]) when i, j are
        constrained by 0 <= i < len(nums1), 0 <= j < len(nums2).

        Args:
            nums1 (list[int]): sorted ascending array
            nums2 (list[int]): sorted ascending array
            k (int): Number of pairs to return

        Returns:
            list[list[int]]: Smallest sum pairs
        """
        m, n = len(nums1), len(nums2)
        ans = []
        # contains which i, j we have visited for nums1, nums2 respectively
        visited = [-1] * m
        visited[0] = 0
        heap = [(nums1[0] + nums2[0], 0, 0)]

        while len(ans) < k and heap:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            # go down in the table
            if i + 1 < m and visited[i + 1] < j:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited[i + 1] = j

            # only go right when we are on first row
            if j + 1 < n and visited[i] < j + 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited[i] = j + 1

        return ans


def main() -> None:
    """373. Find K Pairs with Smallest Sums on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [1,7,11], [2,4,6], 3
        >>> example_case_2 = [1,1,2], [1,2,3], 2
        >>> example_case_3 = [1,2], [3], 3
        >>> test_case_1 = [1,2,4], [-1,1,2], 100

    Example 1:
        >>> sol.kSmallestPairs(*example_case_1)
        [[1, 2], [1, 4], [1, 6]]

    Example 2:
        >>> sol.kSmallestPairs(*example_case_2)
        [[1, 1], [1, 1]]

    Example 3:
        >>> sol.kSmallestPairs(*example_case_3)
        [[1, 3], [2, 3]]

    Test 1:
        >>> sol.kSmallestPairs(*test_case_1)
        [[1, -1], [2, -1], [1, 1], [1, 2], [2, 1], [4, -1], [2, 2], [4, 1], [4, 2]]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
