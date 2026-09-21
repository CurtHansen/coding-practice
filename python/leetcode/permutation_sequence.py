import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        digits_remaining = list(range(1, n+1))
        total_rows = math.factorial(n)
        block_size = dict()
        block_size[0] = total_rows//n
        for i in range(1, n):
            block_size[i] = block_size[i-1]//(n-i)
        ans_list = []

        for i in range(n):
            block = (k-1)//block_size[i]
            ans_list.append(digits_remaining[block])
            digits_remaining.remove(digits_remaining[block])
            k = k-block*block_size[i]

        return "".join([str(x) for x in ans_list])


if __name__ == '__main__':
    sol = Solution()
    print(sol.getPermutation(3, 3))
    print(sol.getPermutation(4, 9))
