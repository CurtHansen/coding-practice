from typing import List
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        for tr,lc,br,rc in queries:
            for r in range(tr,br+1):
                result[r][lc] += 1
                if rc+1<n:
                    result[r][rc+1] -= 1
        for r in range(n):
            prev = 0
            for c in range(n):
                result[r][c] = prev+result[r][c]
                prev = result[r][c]
        print(result)
        return result

if __name__ == '__main__':
    sol = Solution()
    n = 3; queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
    sol.rangeAddQueries(n,queries)
    n = 2; queries = [[0, 0, 1, 1]]
    sol.rangeAddQueries(n,queries)