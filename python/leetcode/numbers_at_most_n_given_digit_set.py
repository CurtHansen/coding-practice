# Based on https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_as_list = [x for x in str(n)]
        len_n = len(n_as_list)
        len_d = len(digits)

        answer = 0

        # Counts using positkons back to and excluding first
        for i in range(1, len_n):
            answer += len_d ** i

        combos = [0] * len_n
        combos[len_n - 1] = len([x for x in digits if x <= n_as_list[len_n - 1]])
        for i in range(len_n - 2, -1, -1):
            temp = 0
            for d in digits:
                if d < n_as_list[i]:
                    temp += len_d ** (len_n - i - 1)
                elif d == n_as_list[i]:
                    temp += combos[i + 1]
            combos[i] = temp
        print(combos)

        answer += combos[0]

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.atMostNGivenDigitSet(["1","2","3","4","6","7","9"], 333))