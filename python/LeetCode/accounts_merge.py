from collections import deque, defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        raw_account_info = defaultdict(list)
        # key: name (str), value: list of lists (each inner list w/ email addresses)

        for account_info in accounts:
            name, email_addresses = account_info[0], account_info[1:]
            raw_account_info[name].append(list(set(email_addresses)))

        def process_name(name):
            """
            Process the key entry for 'name' in account_addresses.
            Steps:
                1) Get the list of lists for the name.
                2) Create map from unique email address to one or more groups.
                3) In each inner list, walk email addresses and update map entry
                    with group number.
                4) Initialize adjacency matrix for groups and create 'visited' for
                    all groups.
                5) Walk through map and update adjacency matrix with 1's for
                    groups with common email address.
                6) Walk through elements in 'visited' and do BFS until empty.
                7) For each connected component, add all email addresses to set.
                8) Convert sets to lists, sort each, and return.
            """

            name_results = []
            email_groups = raw_account_info[name]
            ngroups = len(email_groups)

            if ngroups == 1:
                name_results = [[name] + sorted(email_groups[0])]
            else:
                mapAddressToGroup = defaultdict(list)
                for groupid, entries in enumerate(email_groups):
                    for entry in entries:
                        mapAddressToGroup[entry].append(groupid)

                adj_matrix = [[0] * ngroups for _ in range(ngroups)]
                for address in mapAddressToGroup.keys():
                    groups = mapAddressToGroup[address]
                    numgroups = len(groups)
                    if numgroups > 1:
                        for i in range(numgroups - 1):
                            f, t = groups[i:i + 2]
                            adj_matrix[f][t] = 1
                            adj_matrix[t][f] = 1

                remaining = list(range(ngroups))
                myqueue = deque()
                while len(remaining) > 0:
                    email_members = set()
                    myqueue.clear()
                    myqueue.append(remaining[0])
                    while len(myqueue) > 0:
                        currgroup = myqueue.popleft()
                        if currgroup in remaining:
                            remaining.remove(currgroup)
                            email_members = email_members.union(set(email_groups[currgroup]))
                            for newgroup in range(ngroups):
                                if adj_matrix[currgroup][newgroup] == 1:
                                    myqueue.append(newgroup)
                    name_results.append([name] + sorted(email_members))

            return name_results

        results = []
        for name in raw_account_info.keys():
            results += process_name(name)

        return results


if __name__ == '__main__':
    sol = Solution()
    inputdata = [["David","David0@m.co","David4@m.co","David3@m.co"],
                 ["David","David5@m.co","David5@m.co","David0@m.co"],
                 ["David","David1@m.co","David4@m.co","David0@m.co"],
                 ["David","David0@m.co","David1@m.co","David3@m.co"],
                 ["David","David4@m.co","David1@m.co","David3@m.co"]]
    print(sol.accountsMerge(inputdata))