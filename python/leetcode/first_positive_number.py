from typing import List


class Solution:
    def partition_array(self, array):
        # Purpose is to move all strictly positive numbers to front of array and return cutoff
        #   location between positive numbers and negatives/zeros.
        swap_idx = 0
        for i in range(len(array)):
            if array[i] > 0:
                temp = array[swap_idx]
                array[swap_idx] = array[i]
                array[i] = temp
                swap_idx += 1

        return swap_idx

    def firstMissingPositive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 1
        cutoff = self.partition_array(nums)
        if cutoff == 0: return 1
        print(nums, cutoff)

        for i in range(cutoff):
            idx = abs(nums[i]) - 1
            if idx < cutoff and nums[idx] > 0:
                nums[idx] = -nums[idx]
        print(nums)

        for i in range(cutoff):
            if nums[i] > 0:
                return i + 1

        return cutoff + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstMissingPositive([0,9,10,-3,-1,2,0]))