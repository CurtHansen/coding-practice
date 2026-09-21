from typing import List
from collections import deque
from itertools import product
class Solution:
    def earliestAndLatest(self, n: int, p1: int, p2: int) -> List[int]:
        earliest,latest = 100,-1
        queue = deque()
        queue.append((1,tuple(range(1,n+1))))
        scheduled = {(1,tuple(range(1,n+1)))}
        while len(queue) > 0:
            niter,state = queue.popleft()
            l,r = 0,len(state)-1
            pairs = []
            match = False
            while not match and l<=r:
                temppair = [state[l],state[r]] if l<r else [state[l]]
                if p1 in temppair and p2 in temppair:
                    earliest = min(earliest,niter)
                    latest = max(latest,niter)
                    match = True
                elif p1 in temppair:
                    temppair = [p1]
                elif p2 in temppair:
                    temppair = [p2]
                pairs.append(temppair)
                l+=1
                r-=1
            if not match:
                for possibility in list(product(*pairs)):
                    possibility = sorted(possibility)
                    candidate = (niter+1,tuple(possibility))
                    if candidate not in scheduled:
                        queue.append(candidate)
                        scheduled.add(candidate)

        return [earliest,latest]


if __name__ == '__main__':
    sol = Solution()
    print(sol.earliestAndLatest(11,2,4))
    print(sol.earliestAndLatest(5,1,5))