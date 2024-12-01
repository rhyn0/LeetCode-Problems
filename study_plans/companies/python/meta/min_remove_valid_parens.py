"""Meta Interview Question Practice List on LeetCode.

1249. Minimum Remove to Make Valid Parentheses on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "lee(t(c)o)de)"
    >>> example_case_2 = "a)b(c)d"
    >>> example_case_3 = "))(("

Example 1:
Also acceptable: "lee(t(co)de)" , "lee(t(c)ode)"
    >>> sol.minRemoveToMakeValid(example_case_1)
    'lee(t(c)o)de'
    >>> sol.minRemoveToMakeValidTime(example_case_1)
    'lee(t(c)o)de'
    >>> sol.minRemoveToMakeValidTwoPass(example_case_1)
    'lee(t(c)o)de'

Example 2:
    >>> sol.minRemoveToMakeValid(example_case_2)
    'ab(c)d'
    >>> sol.minRemoveToMakeValidTime(example_case_2)
    'ab(c)d'
    >>> sol.minRemoveToMakeValidTwoPass(example_case_2)
    'ab(c)d'

Example 3:
    >>> sol.minRemoveToMakeValid(example_case_3)
    ''
    >>> sol.minRemoveToMakeValidTime(example_case_3)
    ''
    >>> sol.minRemoveToMakeValidTwoPass(example_case_3)
    ''
"""


class Solution:  # noqa: D101
    def minRemoveToMakeValid(self, s: str) -> str:
        """Return a valid parentheses string with maximum length.

        Only action allowed is to remove parenthesis characters e.g '(' ')'
        Empty string is also a valid parenthesis string.

        Args:
            s (str): Input string to derive from

        Returns:
            str: Maximum length string with valid parentheses
        """
        open_stack = []
        close_stack = []
        for i, char in enumerate(s):
            if char == "(":
                open_stack.append(i)
            elif char == ")":
                if open_stack:
                    open_stack.pop()
                else:
                    close_stack.append(i)
        tobe_removed_chars = {*open_stack, *close_stack}
        return "".join(c for i, c in enumerate(s) if i not in tobe_removed_chars)

    def minRemoveToMakeValidTime(self, s: str) -> str:
        """Return same as above with improvements on list->set conversion."""
        stack = []
        tobe_removed_chars = set()
        for i, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack.append(i)
            # know the character has to be closing paren now
            elif not stack:
                # empty stack means invalid closing
                tobe_removed_chars.add(i)
            else:
                stack.pop()
        tobe_removed_chars.update(stack)
        return "".join(c for i, c in enumerate(s) if i not in tobe_removed_chars)

    def minRemoveToMakeValidTwoPass(self, s: str) -> str:
        """Return same as above with only two linear passes."""

        def make_balanced_parens(val: str, open_char: str, close_char: str) -> str:
            # use stringbuilder methodology
            string_builder = []
            # this is the numerical representation of the stack from before
            balance = 0
            for char in val:
                if char == open_char:
                    balance += 1
                if char == close_char:
                    if balance == 0:
                        continue
                    balance -= 1
                string_builder.append(char)
            return "".join(string_builder)

        no_invalid_close = make_balanced_parens(s, "(", ")")
        # note: reversed creates a generator which
        # is technically not allowed by static typings
        # to fix, loosen the typings of helper - which i dont need to at this time
        reversed_rv = make_balanced_parens(reversed(no_invalid_close), ")", "(")
        return "".join(reversed(reversed_rv))

    def minRemoveToMakeValidTwoPassSimple(self, s: str) -> str:
        """Return same as above but with no inner func."""
        # just like the above with `minRemoveToMakeValidTwoPass`
        # remove invalid close characters, but hard coded closing characters
        # use stringbuilder methodology
        first_string_builder = []
        # this is the numerical representation of the stack from before
        balance = open_seen = 0
        for char in s:
            if char == "(":
                balance += 1
                open_seen += 1
            if char == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_string_builder.append(char)
        # now filter out the right most open parens
        # as they made the balance positive which is invalid paren string
        result = []
        open_to_keep = open_seen - balance
        for char in first_string_builder:
            if char == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(char)
        return "".join(result)
