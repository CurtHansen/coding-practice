import sys
from typing import List, Tuple

def compute_boundary(points) -> List[Tuple[int, int]]:
    l, r, t, b = sys.maxsize, -1, sys.maxsize, -1
    for row, col in points:
        l, r, t, b = min(l, col), max(r, col), min(t, row), max(b, row)
    return [(t, l), (b, r)]
area = lambda x, y: abs(x[0] - y[0]) * abs(x[1] - y[1])
cover = lambda points: area(*compute_boundary(points))

def split_points(points, axis, val):
    above, below = [], []
    for point in points:
        below.append(point) if point[axis] <= val else above.append(point)
    return above, below


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        nrows,ncols = len(grid),len(grid[0])
        ones = [(r,c) for r in range(nrows) for c in range(ncols) if grid[r][c]==1]
        (t,l),(b,r) = compute_boundary(ones)
        result = sys.maxsize
        for

        return result

if __name__ == '__main__':
    g = [[1,0,1,0],[0,1,1,0,],[0,1,0,0]]
    sol = Solution()
    print(sol.minimumSum(g))