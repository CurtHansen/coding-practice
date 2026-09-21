from collections import deque
from typing import List
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        total, n = 0, len(status)
        possess, emptied, openbox = set(initialBoxes), set(), set([x for x in range(n) if status[x] == 1])
        queue = deque(list(possess & openbox))
        while len(queue) > 0:
            box = queue.pop()
            if status[box] == 0:
                possess.add(box)
            else:
                total += candies[box]
                emptied.add(box)
                for k in keys[box]:
                    pass

        return total
