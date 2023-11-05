"""Daily Challenge for November 5 on LeetCode: Problem #1535 [Medium]."""
# Standard Library
import doctest


class Solution:  # noqa: D101
    def getWinner(self, arr: list[int], k: int) -> int:
        """Return the winning number of the array game.

        Indices 0 and 1 fight, maximum number wins and stays at index 0.
        Loser gets moved to the end of the array. Game ends when a winner
        gets to a winning streak of `k` games.

        Numbers in `arr` must be unique to guarantee a winner.

        Args:
            arr (list[int]): Numbers in the competition
            k (int): Win streak to declare winner

        Returns:
            int: winning number
        """
        # do without modifying the original
        if k >= len(arr):
            # needs to win matches against all other numbers + 1 at least
            # so must be max
            return max(arr)
        sim_arr = arr.copy()
        win_streak = 0
        prev_winner = sim_arr[0]
        while win_streak < k:
            pop_idx = 1 if sim_arr[0] > sim_arr[1] else 0
            sim_arr.append(sim_arr.pop(pop_idx))
            win_streak = (win_streak + 1) if prev_winner == sim_arr[0] else 1
            prev_winner = sim_arr[0]

        return sim_arr[0]

    def getWinnerInplace(self, arr: list[int], k: int) -> int:
        """Return same as above with modifications in existing array."""
        if k >= len(arr):
            # needs to win matches against all other numbers + 1 at least
            # so must be max
            return max(arr)
        win_streak = 0
        prev_winner = arr[0]
        while win_streak < k:
            pop_idx = 1 if arr[0] > arr[1] else 0
            arr.append(arr.pop(pop_idx))
            win_streak = (win_streak + 1) if prev_winner == arr[0] else 1
            prev_winner = arr[0]

        return arr[0]

    def getWinnerRuntimeOptimize(self, arr: list[int], k: int) -> int:
        """Return same as above with an optimized simulation algorithm."""
        n = len(arr)
        max_num = max(arr)
        if k >= n:
            # needs to win matches against all other numbers + 1 at least
            # so must be max
            return max_num

        # instead of actually pop and appending numbers, we can use a two pointer
        # to simulate where 0 and 1 are.
        curr_winner, curr_challenger = 0, 1
        win_streak = 0
        while win_streak < k:
            if arr[curr_winner] == max_num:
                # the maximum number will never lose
                break
            if arr[curr_winner] < arr[curr_challenger]:
                curr_winner = curr_challenger
                # when the challenger wins, it causes one win to be erased.
                win_streak = 0
            win_streak += 1
            curr_winner, curr_challenger = curr_winner % n, (curr_challenger + 1) % n

        return arr[curr_winner]


def main() -> None:
    """1535. Find the Winner of an Array Game on LeetCode.

    ====================================================

    Setup:
        >>> from copy import deepcopy
        >>> sol = Solution()
        >>> example_case_1 = [2,1,3,5,4,6,7], 2
        >>> example_case_2 = [3,2,1], 10

    Example 1:
        >>> sol.getWinner(*example_case_1)
        5
        >>> sol.getWinnerInplace(*deepcopy(example_case_1))
        5
        >>> sol.getWinnerRuntimeOptimize(*deepcopy(example_case_1))
        5

    Example 2:
        >>> sol.getWinner(*example_case_2)
        3
        >>> sol.getWinnerInplace(*deepcopy(example_case_2))
        3
        >>> sol.getWinnerRuntimeOptimize(*deepcopy(example_case_2))
        3
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
