"""
Based on LeetCode 1035.
"""


def maxUncrossedLines(A, B):
    na, nb = len(A), len(B)
    dp = [[0] * (nb + 1) for _ in range(na + 1)]
    calculated = [[False] * (nb + 1) for _ in range(na + 1)]

    def recur(aindex, bindex):
        if aindex == 0 or bindex == 0:
            return 0
        if calculated[aindex][bindex]:
            return dp[aindex][bindex]

        best = 0
        best = max(best, recur(aindex, bindex - 1))
        best = max(best, recur(aindex - 1, bindex))

        if A[aindex - 1] == B[bindex - 1]:
            best = max(best, recur(aindex - 1, bindex - 1) + 1)

        dp[aindex][bindex] = best
        calculated[aindex][bindex] = True
        return best

    ans = recur(na, nb)
    return ans


if __name__ == '__main__':
    inA = [1,4,2]
    inB = [1,2,4]
    print(maxUncrossedLines(inA, inB))