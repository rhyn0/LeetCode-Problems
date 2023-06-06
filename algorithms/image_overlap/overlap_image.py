# Standard Library
from collections import defaultdict
from collections.abc import Generator
import doctest


class Solution:  # noqa: D101
    def largestOverlap(  # spec
        self,
        img1: list[list[int]],
        img2: list[list[int]],
    ) -> int:
        """Return largest overlap possible between two images.

        Given two images represented as binary matrices, find the biggest overlap
        on 'pixels' where the value is 1.
        Images can be shifted in any way up/down, left/right for any number
        of moves but no rotations.

        Args:
            img1 (List[List[int]]): Image 1
            img2 (List[List[int]]): Image 2

        Returns:
            int: Maximum number of pixels that overlap between images
        """

        def ones_positions(
            image: list[list[int]],
        ) -> Generator[tuple[int, int], None, None]:
            return (
                (row_ind, col)
                for row_ind, row in enumerate(image)
                for col, val in enumerate(row)
                if val == 1
            )

        transform_vectors = defaultdict(int)

        for x_a, y_a in ones_positions(img1):
            for x_b, y_b in ones_positions(img2):
                curr_transform_vec = (x_b - x_a, y_b - y_a)
                transform_vectors[curr_transform_vec] += 1

        if not transform_vectors:
            return 0
        return max(transform_vectors.values())


def main() -> None:
    """Image Overlap on LeetCode.

    ====================================================

    Setup:
        >>> sol = Solution()

    Example 1:
        >>> sol.largestOverlap([[1,1,0],[0,1,0],[0,1,0]],[[0,0,0],[0,1,1],[0,0,1]])
        3

    Example 2:
        >>> sol.largestOverlap([[0]], [[0]])
        0

    Example 3:
        >>> sol.largestOverlap([[1]], [[1]])
        1
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
