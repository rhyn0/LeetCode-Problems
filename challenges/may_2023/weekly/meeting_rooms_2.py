"""Weekly Challenge on LeetCode for May 2023."""

# Standard Library
import doctest
import heapq
from operator import itemgetter


class Solution:  # noqa: D101
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """Return minnumber of meeting rooms needed to handle the meeting schedule.

        If meeting ends at same time one starts, the meeting room is reused.

        Args:
            intervals (list[list[int]]): List of meeting [start, end] times

        Returns:
            int: Minimum number of meeting rooms necessary
        """
        # make a copy because I'll self-impose the data integrity part
        meeting_times = intervals[:]
        meeting_times.sort(key=itemgetter(0))

        # keep track of next to free up room using a Min Heap
        provisioned_rooms = []

        heapq.heappush(provisioned_rooms, meeting_times[0][1])

        # if a room isn't available at the time of start of next meeting
        # provision another, keep track of total in the heap.
        for meet_start, meet_end in meeting_times[1:]:
            if provisioned_rooms[0] <= meet_start:
                heapq.heappop(provisioned_rooms)

            heapq.heappush(provisioned_rooms, meet_end)

        return len(provisioned_rooms)

    def minMeetingRoomsChrono(self, intervals: list[list[int]]) -> int:
        """Return same as above using chronological ordering."""
        starts = sorted(meeting[0] for meeting in intervals)
        ends = sorted(meeting[1] for meeting in intervals)

        len(intervals)
        end_idx = 0
        provisioned_rooms = 0
        for start_time in starts:
            # if meeting room is open up by start of this meeting
            # re use
            if start_time >= ends[end_idx]:
                provisioned_rooms -= 1
                end_idx += 1
            # otherwise open a new one
            provisioned_rooms += 1
        return provisioned_rooms


def main() -> None:
    """253. Meeting Rooms II on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()
        >>> example_case_1 = [[0,30],[5,10],[15,20]]
        >>> example_case_2 = [[7,10],[2,4]]
        >>> test_case_1 = [[1,5], [8,9], [8,9]]

    Example 1:
        >>> sol.minMeetingRooms(example_case_1)
        2
        >>> sol.minMeetingRoomsChrono(example_case_1)
        2

    Example 2:
        >>> sol.minMeetingRooms(example_case_2)
        1
        >>> sol.minMeetingRoomsChrono(example_case_2)
        1

    Test 1:
        >>> sol.minMeetingRooms(test_case_1)
        2
        >>> sol.minMeetingRoomsChrono(test_case_1)
        2
    """


if __name__ == "__main__":
    doctest.testmod(
        optionflags=doctest.REPORTING_FLAGS ^ doctest.FAIL_FAST
        | doctest.ELLIPSIS
        | doctest.NORMALIZE_WHITESPACE,
    )
