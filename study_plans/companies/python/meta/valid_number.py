"""Meta Interview Question Practice List on LeetCode.

65. Valid Number on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = "0"
    >>> example_case_2 = "e"
    >>> example_case_3 = "."
    >>> test_case_1 = "0e"

Example 1:
    >>> sol.isNumber(example_case_1)
    True
    >>> sol.isNumberFSM(example_case_1)
    True

Example 2:
    >>> sol.isNumber(example_case_2)
    False
    >>> sol.isNumberFSM(example_case_2)
    False

Example 3:
    >>> sol.isNumber(example_case_3)
    False
    >>> sol.isNumberFSM(example_case_3)
    False

Test 1:
    >>> sol.isNumber(test_case_1)
    False
    >>> sol.isNumberFSM(test_case_1)
    False
"""


class Solution:  # noqa: D101
    def isNumber(self, s: str) -> bool:
        """Return whether the given string represents a valid number.

        Numbers can be negative/positive integers or decimals
        with optional exponents.

        Args:
            s (str): String possibly representing number

        Returns:
            bool: True if string is a valid number, otherwise False
        """
        seen_digit = seen_dot = seen_e = False
        for idx, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ("-", "+"):
                if idx != 0 and s[idx - 1].lower() != "e":
                    return False
            elif c == ".":
                # valid exponent values can't be decimals
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif c.lower() == "e":
                if not seen_digit or seen_e:
                    return False
                # exponents require a digit so we reset this
                seen_digit = False
                seen_e = True
            else:
                return False
        return seen_digit

    def isNumberFSM(self, s: str) -> bool:
        """Return same as above using Finite State Machine.

        DFA is a synonym to this.
        """
        # use array for indexing by state
        # There are 8 values possible for state
        current_state = 0
        # for each state, map the character choices to the next state
        states = [
            {"digit": 1, "dot": 2, "sign": 3},  # initial
            {"digit": 1, "dot": 4, "exp": 5},  # digit
            {"digit": 4},  # dot
            {"digit": 1, "dot": 2},  # sign
            {"digit": 4, "exp": 5},  # digit dot, notice digit path goes to itself
            {"digit": 7, "sign": 6},  # number exp
            {"digit": 7},  # exp sign
            {"digit": 7},  # exp number
        ]
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c == ".":
                group = "dot"
            elif c in ("e", "E"):
                group = "exp"
            elif c in ("-", "+"):
                group = "sign"
            else:
                return False

            if group not in states[current_state]:
                return False
            current_state = states[current_state][group]
        # only valid end states are digit, digit dot, exp number
        return current_state in (1, 4, 7)
