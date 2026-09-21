from typing import List


class Solution:
    def find_break(self, start_idx, end_idx):
        print(f'start_idx,end_idx: {start_idx, end_idx}')
        if self.nums[start_idx] < self.nums[end_idx] or start_idx >= end_idx:
            pass  # no break in this interval
        elif end_idx - start_idx == 1:
            if self.nums[end_idx] < self.nums[start_idx]:
                self.break_idx = end_idx
        else:
            midpoint = (start_idx + end_idx) // 2
            if self.nums[midpoint] < self.nums[midpoint - 1]:
                self.break_idx = midpoint
            else:
                self.find_break(start_idx, midpoint - 1)
                self.find_break(midpoint, end_idx)

    def search_value(self, start_idx, end_idx):
        while start_idx <= end_idx:
            #            print(f'start_idx, end_idx: {start_idx, end_idx}')
            if self.nums[start_idx] == self.target:
                return True
            else:
                midpoint = (start_idx + end_idx) // 2
                #                print(f'midpoint {midpoint}')
                if self.nums[midpoint] == self.target:
                    return True
                elif self.nums[start_idx] <= self.target <= self.nums[midpoint]:
                    end_idx = midpoint
                else:
                    start_idx = midpoint + 1

        return False

    def search(self, nums: List[int], target: int) -> bool:
        """
        Approach this in two steps:
        1) Identify the location in the array of the (leftmost) smallest element.
            This will be in one of two locations:
                a) 0th element: no rotation
                b) not 0th element: some rotation
        2) Search for the target using only the appropriate subarray.
            For case (a) above, use entire array.
            For case (b) above, use either left or right subarray depending on boundaries.
        """
        if len(nums) == 0:
            return False
        self.nums = nums
        self.target = target
        self.break_idx = None
        self.find_break(0, len(self.nums) - 1)
        if self.break_idx is None:
            self.break_idx = 0
        print(f'break_idx: {self.break_idx}')
        if self.nums[self.break_idx] <= self.target <= self.nums[len(self.nums) - 1]:
            found = self.search_value(self.break_idx, len(self.nums) - 1)
        else:
            found = self.search_value(0, self.break_idx - 1)

        return found


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([1,1,1,1,2,1,1,1,1,1,1,1],2))
