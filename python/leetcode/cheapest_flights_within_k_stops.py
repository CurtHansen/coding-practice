from queue import PriorityQueue
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):

        graph = defaultdict(dict)
        for s, e, p in flights:
            graph[s][e] = p

        myqueue = PriorityQueue()
        myqueue.put((0, (src, 0)))  # cost, node/stops

        while not myqueue.empty():
            total_cost, (node, nstops) = myqueue.get()
            if node == dst:
                return total_cost
            elif nstops <= K:
                for nb, cost in graph.get(node, dict()).items():
                    myqueue.put((total_cost + graph[node][nb], (nb, nstops + 1)))

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
