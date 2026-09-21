# Based on https://leetcode.com/problems/queue-reconstruction-by-height/
from collections import defaultdict


class Solution:
    def reconstructQueue(self, people):

        n = len(people)
        ans = [None] * n
        available_spots = list(range(n))
        mydict = defaultdict(list)

        for height, value in people:
            mydict[height].append(value)

        unique_heights = sorted(mydict.keys())
        for height in unique_heights:
            indices_used = []
            for pos in mydict[height]:
                ans[available_spots[pos]] = [height, pos]
                indices_used.append(available_spots[pos])
            for pos in indices_used:
                available_spots.remove(pos)

        return ans


if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    sol = Solution()
    print(sol.reconstructQueue(people))