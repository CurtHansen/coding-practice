from collections import deque
from typing import List


class Solution:
    def consider_entry(self, val, position):
        lq = len(self.myqueue)

        if lq == 0:
            self.myqueue.append((val, position))
        if lq == 1:
            if val >= self.myqueue[0][0]:
                self.myqueue.appendleft((val, position))
            elif self.k > 1:
                self.myqueue.append((val, position))
        if lq == 2:
            if val >= self.myqueue[0][0]:
                self.myqueue.pop()
                self.myqueue.appendleft((val, position))
            elif val >= self.myqueue[1][0]:
                self.myqueue.pop()
                self.myqueue.append((val, position))

    def print_queue(self):
        result = "queue:"
        if len(self.myqueue) == 0:
            result += " empty"
        else:
            idx = 0
            while idx < len(self.myqueue):
                result += " " + str(self.myqueue[idx])
                idx += 1
        print(result)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        self.k = k

        if n == 1:
            return nums

        answer = []
        self.myqueue = deque(maxlen=min(3, self.k))
        for i in range(self.k):
            self.consider_entry(nums[i], i)
        for i in range(n - k + 1):
            print(f'\n{i}')
            self.print_queue()
            idx = 0
            while idx < len(self.myqueue):
                if self.myqueue.count() > idx and i - 1 == self.myqueue[idx][1]:
                    self.myqueue.rotate(self.myqueue.count() - idx - 1)
                    self.myqueue.pop()
                    self.myqueue.rotate()

            answer.append(self.myqueue[0][0])

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,1,2,0,5],3))
