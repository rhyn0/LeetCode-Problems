"""Daily Challenge for April 14, 2025.

1534. Count Good Triplets on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [3,0,1,1,9,7], 7, 2, 3
    >>> example_case_2 = [1,1,2,2,3], 0, 0, 1

Example 1:
    >>> sol.countGoodTriplets(*example_case_1)
    4

Example 2:
    >>> sol.countGoodTriplets(*example_case_2)
    0
"""


class Solution:  # noqa: D101
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """Return the number of unique good triplets.

        A good triplet is one that satisfies the condition of choosing the
        indices of arr i,j,k such that:
            - 0 <= i < j < k < arr.length
            - |arr[i] - arr[j]| <= a
            - |arr[j] - arr[k]| <= b
            - |arr[i] - arr[k]| <= c

        Args:
            arr (list[int]): Source of numbers
            a (int): first limit
            b (int): second limit
            c (int): third limit

        Returns:
            int: Number of good triples in the array
        """
        ans = 0
        # how many numbers are less than this index
        prefix_counts = [0] * 1001  # max value constraint is 1000
        # can choose j, k first and then find a valid range for i
        for j, j_val in enumerate(arr):
            for k_val in arr[j + 1 :]:
                if abs(j_val - k_val) > b:
                    continue
                lj, rj = j_val - a, j_val + a
                lk, rk = k_val - c, k_val + c

                # overlapping section that satisfies final two constraints
                rightmost_left = max(0, lj, lk)
                leftmost_right = min(1000, rj, rk)

                if rightmost_left <= leftmost_right:
                    ans += prefix_counts[leftmost_right] - (
                        0 if rightmost_left == 0 else prefix_counts[rightmost_left - 1]
                    )
            # update prefix array that we saw a value of `j_val`
            for x in range(j_val, 1001):
                prefix_counts[x] += 1

        return ans
