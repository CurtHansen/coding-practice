from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        nrows, ncols = len(grid), len(grid[0])
        rotten_tobe_processed = []
        num_fresh = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    rotten_tobe_processed.append((i, j))

        if num_fresh == 0:
            return 0

        def process_direction(orange, direction):
            vert, horiz = direction
            row, col = orange[0] + vert, orange[1] + horiz
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                return None
            if grid[row][col] in [0, 2]:
                return None
            else:
                grid[row][col] = 2
                nonlocal num_fresh
                num_fresh -= 1
                return (row, col)

        def process_rotten_orange(orange):
            results = []
            for direction in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                result = process_direction(orange, direction)
                if result:
                    results.append(result)
            return results

        num_iterations = 0
        while len(rotten_tobe_processed) > 0 and num_fresh > 0:
            num_iterations += 1
            new_rotten = []
            while len(rotten_tobe_processed) > 0:
                next_orange = rotten_tobe_processed.pop()
                new_rotten = new_rotten + process_rotten_orange(next_orange)
            if num_fresh == 0:
                return num_iterations
            rotten_tobe_processed = new_rotten

        return -1


if __name__ == '__main__':
    sol = Solution()
    mygrid = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting(mygrid))
