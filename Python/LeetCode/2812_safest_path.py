import sys
from collections import deque
from typing import List
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n,result = len(grid),0
        if ((grid[0][0]==1) or (grid[n-1][n-1]==1)): return 0
        thieves = [(i,j) for i in range(n) for j in range(n) if grid[i][j]==1]
        mindistance = [[sys.maxsize]*n for _ in range(n)]
        manh_dist = lambda x,y: abs(x[0]-y[0]) + abs(x[1]-y[1])
        for t in thieves:
            for r in range(n):
                for c in range(n):
                    mindistance[r][c] = min(mindistance[r][c],manh_dist(t,[r,c]))

        def check_candidate(val):
            print(f"  {val=}")
            if val==0: return True
            queue,considered = deque([(0,0)]),{(0,0)}
            while queue:
                cell = queue.popleft()
                print(f"    {cell=}")
                if cell==(n-1,n-1):
                    return True
                for dv,dh in [(+1,0),(-1,0),(0,+1),(0,-1)]:
                    r,c = cell[0]+dv,cell[1]+dh
                    new_cell = (r,c)
                    print(f"      {new_cell=}")
                    if 0<=r<n and 0<=c<n and new_cell not in considered:
                        print("        passed 1", end="")
                        considered.add(new_cell)
                        if mindistance[r][c] >= val:
                            print(" and 2",end="")
                            queue.append(new_cell)
                        print("")
            return False

        l,h = 0,n #min(mindistance[0][0],mindistance[n-1][n-1])
        while l<h:
            midpoint = (l+h)//2
            print(f"\n{l,h,midpoint}")
            ok = check_candidate(midpoint)
            print(f"  {ok=}")
            if ok:
                if check_candidate(midpoint+1):
                    l = midpoint+1
                else:
                    return midpoint
            else:
                h = midpoint - 1
        return l


if __name__ == '__main__':
    sol = Solution()
    data = [[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,1,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    print(sol.maximumSafenessFactor(data))