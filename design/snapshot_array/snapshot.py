# Standard Library
from bisect import bisect_right
import doctest
from typing import Any


class SnapshotArray:
    """Object to store historical snapshots of an array."""

    def __init__(self, length: int) -> None:  # noqa: D107
        self.snapshots = 0
        self.historical_array = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:  # spec
        """Set index of array to be `val`.

        Sets the value in the current version.

        Args:
            index (int): index to modify, must be < length
            val (int): value
        """
        self.historical_array[index].append([self.snapshots, val])

    def snap(self) -> int:
        """Make a new snapshot.

        Returns:
            int: the snapshot's id to index by
        """
        self.snapshots += 1
        return self.snapshots - 1

    def get(self, index: int, snap_id: int) -> int:
        """Get value of index for a previous snapshot.

        Args:
            index (int): index of array, must be < length
            snap_id (int): snapshot to return value from

        Returns:
            int: value
        """
        last_snap_change_idx = bisect_right(
            self.historical_array[index],
            [snap_id, 1e9],
        )
        return self.historical_array[index][last_snap_change_idx - 1][1]


def test_design_inputs(func_calls: list[str], inputs: list[list[Any]]) -> list[Any]:
    """Call input functions with associated inputs and return their output as list."""
    # first index is always an initialization
    sol = SnapshotArray(*inputs[0])
    return [None] + [
        sol.__getattribute__(func)(*args)
        for func, args in zip(func_calls[1:], inputs[1:], strict=True)
    ]


def main() -> None:
    """1146. Snapshot Array on LeetCode.

    ====================================================

    Test Methods:
        >>> test_design_inputs(\
            ["SnapshotArray","set","snap","set","get"],\
            [[3],[0,5],[],[0,6],[0,0]],\
            )
        [None, None, 0, None, 5]

        >>> test_design_inputs(\
            ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"],\
            [[1],[0,15],[],[],[],[0,2],[],[],[0,0]],\
            )
        [None, None, 0, 1, 2, 15, 3, 4, 15]
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
