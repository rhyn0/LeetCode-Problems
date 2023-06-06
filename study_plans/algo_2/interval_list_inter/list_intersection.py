# Standard Library
import doctest


class Solution:  # noqa: D101
    def intervalIntersection(  # spec
        self,
        first: list[list[int]],
        second: list[list[int]],
    ) -> list[list[int]]:
        """Return intersection of the lists of intervals.

        Given lists of intervals must be disjoint and sorted.

        Args:
            first (List[List[int]]): First list of intervals
            second (List[List[int]]): Second list of intervals

        Returns:
            List[List[int]]: Merge interval list
        """
        ret_intersect = []
        first_n, second_m = len(first), len(second)
        f_ind = s_ind = 0
        while f_ind < first_n and s_ind < second_m:
            common_start, common_end = max(first[f_ind][0], second[s_ind][0]), min(
                first[f_ind][1],
                second[s_ind][1],
            )
            if common_start <= common_end:
                ret_intersect.append([common_start, common_end])

            if first[f_ind][1] == second[s_ind][1]:
                f_ind += 1
                s_ind += 1
            elif first[f_ind][1] < second[s_ind][1]:
                f_ind += 1
            else:
                s_ind += 1

        return ret_intersect


def main() -> None:
    """Interval List Intersection on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],\
            [[1,5],[8,12],[15,24],[25,26]])
        [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    Example 1:
        >>> sol.intervalIntersection([[1,3],[5,9]], [])
        []
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
