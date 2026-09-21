# Based on https://leetcode.com/problems/largest-rectangle-in-histogram/

from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        mystack, maxval = deque(), 0

        for idx, num in enumerate(heights + [0]):
            while mystack and heights[mystack[0]] > num:
                pos = mystack.popleft()
                width = idx if not mystack else idx - mystack[0] - 1
                maxval = max(maxval, heights[pos] * width)
            mystack.appendleft(idx)

        return maxval


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2,3,4,5,66,34,3,3,1,1]))