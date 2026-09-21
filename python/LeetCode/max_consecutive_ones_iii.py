#
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        print(nums, k)
        n = len(nums)
        ptr1, ptr2 = -1, 0
        num0p1, num0p2 = 0, 0 if nums[ptr2] == 1 else 1
        answer = 0

        while ptr2 < n:
            num_zeros_in_window = num0p2 - num0p1
            if num_zeros_in_window <= k:
                answer = max(answer, ptr2-ptr1)
            if num_zeros_in_window <= k:
                ptr2 += 1
                if ptr2 < n and nums[ptr2] == 0:
                    num0p2 += 1
            if num_zeros_in_window > k:
                ptr1 += 1
                if nums[ptr1] == 0:
                    num0p1 += 1

        return answer


if __name__ == '__main__':
    sol = Solution()
    arr, k = [1,1,1,0,0,0,1,1,1,1,0], 2
    print(sol.longestOnes(arr, k))