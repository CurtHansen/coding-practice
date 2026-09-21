# Based on https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:

        distances = dict()

        if X == Y:
            return 0

        if (X,Y) in distances:
            return distances[(X,Y)]
        else:
            if Y < X:
                distances[(X,Y)] = X-Y
            elif Y % 2 == 1:
                distances[(X,Y)] = 1 + self.brokenCalc(X, Y+1)
            else:
                distances[(X,Y)] = 1 + self.brokenCalc(X, Y//2)

            return distances[(X,Y)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.brokenCalc(1, 1_000_000_000))
