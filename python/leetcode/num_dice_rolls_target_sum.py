# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        numways = dict()

        def compute_num_ways(numdice, numfaces, goal):
            if (numdice, numfaces, goal) in numways:
                return numways[(numdice, numfaces, goal)]

            if numdice == 1:
                if 1 <= goal <= numfaces:
                    return 1
                else:
                    return 0

            sumtotal = 0
            for roll in range(1, numfaces + 1):
                sumtotal += compute_num_ways(numdice - 1, numfaces, goal - roll)
            sumtotal = sumtotal % (10 ** 9 + 7)

            numways[(numdice, numfaces, goal)] = sumtotal
            return sumtotal

        return compute_num_ways(d, f, target)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numRollsToTarget(2,6,7))