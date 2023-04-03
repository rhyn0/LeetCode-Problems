# Standard Library
import doctest


class BrowserHistory:
    """Class to store a user's browser history.

    Allows for visiting new pages and traversing recent pages.
    """

    def __init__(self, homepage: str):
        """Start browser at a specific page."""
        self._curr_idx = 0
        self.pages = [homepage]

    def visit(self, new_page: str) -> None:
        """Visit new page.

        Remove all forward history from current history.
        """
        self.pages[self._curr_idx + 1 :] = [new_page]
        self._curr_idx += 1

    def back(self, num_pages: int) -> str:
        """Move *num_pages* back in history.

        Reaching the homepage means return the homepage.
        """
        self._curr_idx = max(self._curr_idx - num_pages, 0)
        return self.pages[self._curr_idx]

    def forward(self, num_pages: int) -> str:
        """Move *num_pages* forward in history.

        Reaching the newest page means return the newest page.
        """
        self._curr_idx = min(self._curr_idx + num_pages, len(self.pages) - 1)
        return self.pages[self._curr_idx]


def main():
    """Design Browser History on LeetCode.

    ====================================================

    Setup:
        >>> sol = BrowserHistory("leetcode.com")

    Test Methods:
        >>> sol.visit("google.com")
        >>> sol.visit("facebook.com")
        >>> sol.visit("youtube.com")
        >>> sol.back(1)
        'facebook.com'
        >>> sol.back(1)
        'google.com'
        >>> sol.forward(1)
        'facebook.com'
        >>> sol.visit("linkedin.com")
        >>> sol.forward(2)
        'linkedin.com'
        >>> sol.back(2)
        'google.com'
        >>> sol.back(7)
        'leetcode.com'
    """


if __name__ == "__main__":
    doctest.testmod(
        verbose=True, optionflags=doctest.REPORTING_FLAGS | doctest.ELLIPSIS
    )
