"""Meta Interview Question Practice List on LeetCode.

721. Accounts Merge on LeetCode.

====================================================

Setup:
    >>> sol = Solution()
    >>> example_case_1 = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    >>> example_case_2 = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

Example 1:
    >>> sol.accountsMerge(example_case_1)
    [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]
    >>> sol.accountsMergeDfsGraph(example_case_1)
    [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]
    >>> sol.accountsMergeDSU(example_case_1)
    [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]

Example 2:
    >>> sol.accountsMerge(example_case_2)
    [['Gabe', 'Gabe0@m.co', 'Gabe1@m.co', 'Gabe3@m.co'], ['Kevin', 'Kevin0@m.co', 'Kevin3@m.co', 'Kevin5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan4@m.co', 'Ethan5@m.co'], ['Hanzo', 'Hanzo0@m.co', 'Hanzo1@m.co', 'Hanzo3@m.co'], ['Fern', 'Fern0@m.co', 'Fern1@m.co', 'Fern5@m.co']]
    >>> sol.accountsMergeDfsGraph(example_case_2)
    [['Gabe', 'Gabe0@m.co', 'Gabe1@m.co', 'Gabe3@m.co'], ['Kevin', 'Kevin0@m.co', 'Kevin3@m.co', 'Kevin5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan4@m.co', 'Ethan5@m.co'], ['Hanzo', 'Hanzo0@m.co', 'Hanzo1@m.co', 'Hanzo3@m.co'], ['Fern', 'Fern0@m.co', 'Fern1@m.co', 'Fern5@m.co']]
    >>> sol.accountsMergeDSU(example_case_2)
    [['Gabe', 'Gabe0@m.co', 'Gabe1@m.co', 'Gabe3@m.co'], ['Kevin', 'Kevin0@m.co', 'Kevin3@m.co', 'Kevin5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan4@m.co', 'Ethan5@m.co'], ['Hanzo', 'Hanzo0@m.co', 'Hanzo1@m.co', 'Hanzo3@m.co'], ['Fern', 'Fern0@m.co', 'Fern1@m.co', 'Fern5@m.co']]
"""  # noqa: E501

# Standard Library
from collections import defaultdict


class Solution:  # noqa: D101
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """Return the merged account list from the given accounts.

        An account is a list of strings, first entry being a name and the rest emails.
        A pair of accounts should be merged if there are overlaps in emails.

        Args:
            accounts (list[list[str]]): Possibly unmerged accounts

        Returns:
            list[list[str]]: Merged accounts, emails for an account are in sorted order.
        """
        merged_idx = set()
        # store the name of account and their emails
        email_sets = [(acc[0], set(acc[1:])) for acc in accounts]
        n = len(email_sets)
        # for each account, try to pair with a later account
        # if there is email overlap, combine them and stop
        # can stop because later iteration will pickup the now combined set
        # accounts to be merged are guaranteed to have same name
        for i, (_, a_set) in enumerate(email_sets):
            for j in range(i + 1, n):
                _, b_set = email_sets[j]
                if b_set & a_set:
                    merged_idx.add(i)
                    b_set |= a_set
                    break
        return [
            [name, *sorted(email)]
            for i, (name, email) in enumerate(email_sets)
            if i not in merged_idx
        ]

    def accountsMergeDfsGraph(self, accounts: list[list[str]]) -> list[list[str]]:
        """Return same as above using Graphs and DFS."""
        adjacency_graph: dict[str, list[str]] = defaultdict(list)
        visited: set[str] = set()

        def dfs(curr_merge_account: list[str], email: str):
            curr_merge_account.append(email)
            visited.add(email)

            if email not in adjacency_graph:
                return
            for conn_email in adjacency_graph[email]:
                if conn_email not in visited:
                    dfs(curr_merge_account, conn_email)

        # initialize adjacency graph
        for acc in accounts:
            # make bidirectional pairings against the first email
            first_email = acc[1]
            for next_email in acc[2:]:
                adjacency_graph[first_email].append(next_email)
                adjacency_graph[next_email].append(first_email)

        rv = []
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            if first_email not in visited:
                merge_account: list[str] = []
                dfs(merge_account, first_email)
                rv.append([name, *sorted(merge_account)])
        return rv

    def accountsMergeDSU(  # noqa: C901
        self,
        accounts: list[list[str]],
    ) -> list[list[str]]:
        """Return same as above using disjoin set unions."""
        n = len(accounts)
        # set representative of each group to itself
        representatives = list(range(n))
        sizes = [1] * n

        def find_rep(x: int) -> int:
            if x == representatives[x]:
                return x

            representatives[x] = find_rep(representatives[x])
            return representatives[x]

        def union_merge(x: int, y: int) -> None:
            rep_x, rep_y = find_rep(x), find_rep(y)
            if rep_x == rep_y:
                # do nothing because already joined
                return
            size_x, size_y = sizes[rep_x], sizes[rep_y]
            if size_x >= size_y:
                sizes[size_x] += size_y
                representatives[rep_y] = rep_x
            else:
                sizes[size_y] += size_x
                representatives[rep_x] = rep_y

        emails_to_component: dict[str, int] = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in emails_to_component:
                    emails_to_component[email] = i
                else:
                    union_merge(i, emails_to_component[email])
        # for each rep, build list of its emails
        component_emails: defaultdict[int, list[str]] = defaultdict(list)
        for email, component in emails_to_component.items():
            rep = find_rep(component)
            component_emails[rep].append(email)
        # build output
        rv = []
        # reminder that every component maps back to an original account
        # which is where we get the name
        for component, emails in component_emails.items():
            rv.append([accounts[component][0], *sorted(emails)])
        return rv
