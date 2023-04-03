"""Print in Order - Difficult Easy.

Suppose we have a class:
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed
after first(), and third() is executed after second().

Note:
We do not know how the threads will be scheduled in the operating system, even
though the numbers in the input seem to
imply the ordering. The input format you see is mainly to ensure our
tests' comprehensiveness.

Example 1:
```
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3]
means thread A calls first(),
thread B calls second(), and thread C calls third(). "firstsecondthird"
is the correct output.
```

Example 2:
```
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(),
and thread C calls second().
"firstsecondthird" is the correct output.
```

Constraints:
    - nums is a permutation of [1, 2, 3].
"""

# Standard Library
from collections.abc import Callable
import time


class Foo:
    """Answer for Print Order from LeetCode."""

    _FIRST_WAIT = 1
    _SECOND_WAIT = 2
    _THIRD_WAIT = 3

    def __init__(self) -> None:
        """Instantiate manager object to ensure concurrency."""
        self.current = 1

    def first(self, print_first: Callable[[], None]) -> None:
        """Print first in its thread."""
        while self.current != self._FIRST_WAIT:
            time.sleep(0.1)

        print_first()
        self.current += 1

    def second(self, print_second: Callable[[], None]) -> None:
        """Print second in its thread."""
        while self.current != self._SECOND_WAIT:
            time.sleep(0.1)

        print_second()
        self.current += 1

    def third(self, print_third: Callable[[], None]) -> None:
        """Print third in its thread."""
        while self.current != self._THIRD_WAIT:
            time.sleep(0.1)

        print_third()
        self.current += 1

    """Learnings from community solutions:
        - might make more sense to use public packages (threading)
            + locks, one for each step between functions
            + Event driven architecture makes more sense on paper for explanation
    """


# Standard Library
# rewrite here
import threading  # noqa: E402


class Foo2:
    """Solution using Event listeners."""

    def __init__(self) -> None:
        """Instantiate manager object to ensure concurrency."""
        self.event1 = threading.Event()  # control 1 -> 2
        self.event2 = threading.Event()  # control 2 -> 3

    def first(self, print_first: Callable[[], None]) -> None:
        """Print first in its thread."""
        print_first()
        self.event1.set()

    def second(self, print_second: Callable[[], None]) -> None:
        """Print second in its thread."""
        self.event1.wait()
        print_second()
        self.event2.set()

    def third(self, print_third: Callable[[], None]) -> None:
        """Print third in its thread."""
        self.event2.wait()
        print_third()
