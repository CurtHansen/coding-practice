# Based on 1042. Flower Planting With No Adjacent https://leetcode.com/problems/flower-planting-with-no-adjacent/

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # Nodes/gardens are 1-based, so need to make adjustments in code to handle indexing.

        neighbors = defaultdict(list)

        for path in paths:
            neighbors[path[0]-1].append(path[1]-1)
            neighbors[path[1]-1].append(path[0]-1)

        def isOK(existing_assignments, next_assignment):
            ncurrent_assignments = len(existing_assignments)
            for neighbor in neighbors[ncurrent_assignments]:
                if neighbor < ncurrent_assignments and existing_assignments[neighbor] == next_assignment:
                    return False
            return True

        def recursive(curr_idx, assignments):
            nonlocal ans
            if curr_idx == N:
                ans = assignments
                return True
            for color in range(1, 5):
                if isOK(assignments, color):
                    if recursive(curr_idx + 1, assignments + [color]) == True:
                        return True
            return False

        ans = None
        recursive(0, [])

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.gardenNoAdj(10000, []))
