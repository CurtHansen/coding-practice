class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        n = len(cost)

        if n == 1:
            return cost[0]
        if n == 2:
            return cost[1]

        if n > 2:
            mincosts = [None] * (n + 1)
            mincosts[0] = cost[0]
            mincosts[1] = cost[1]
            for idx in range(2, n):
                mincosts[idx] = min(mincosts[idx - 1], mincosts[idx - 2]) + cost[idx]
            mincosts[n] = min(mincosts[n - 1], mincosts[n - 2])

            return mincosts[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20]))
