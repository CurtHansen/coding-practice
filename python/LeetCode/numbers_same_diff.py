# Based on https://leetcode.com/problems/numbers-with-same-consecutive-differences/
from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        ans = []

        def find_nums(level, current_set, new_num):
            nonlocal ans
            if new_num < 0 or new_num > 9:
                return
            if level == N:
                ans.append(current_set + [new_num])
            else:
                find_nums(level + 1, current_set + [new_num], new_num - K)
                find_nums(level + 1, current_set + [new_num], new_num + K)

        for i in range(1, 10):
            find_nums(1, [], i)

        print(ans)
        ans = [int("".join(map(str, x))) for x in ans]

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numsSameConsecDiff(2,1))
