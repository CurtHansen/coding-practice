from queue import Queue
from collections import namedtuple, defaultdict


class Solution:
    def findItinerary(self, tickets):

        nflights = len(tickets)
        solutions = list()
        myqueue = Queue()
        Route = namedtuple('Route', 'legs next_origin')

        def create_city_list(list_of_pairs):
            ans = list()
            ans.append(tickets[list_of_pairs[0]][0])
            ans.append(tickets[list_of_pairs[0]][1])
            for idx in range(1, len(list_of_pairs)):
                ans.append(tickets[list_of_pairs[idx]][1])
            return ans

        all_flights = defaultdict(list)
        for pos, flight in enumerate(tickets):
            all_flights[flight[0]].append(pos)

        myqueue.put(Route([], 'JFK'))

        while not myqueue.empty():
            entry = myqueue.get()
            if len(entry.legs) == nflights:
                solutions.append(entry.legs)
            else:
                available_legs = [x for x in all_flights[entry.next_origin] if x not in entry.legs]
                for leg in available_legs:
                    myqueue.put(Route(entry.legs + [leg], tickets[leg][1]))

        solutions = create_city_list(solutions[0])

        return solutions


if __name__ == '__main__':
    sol = Solution()
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    result = sol.findItinerary(tickets)
    print(result)