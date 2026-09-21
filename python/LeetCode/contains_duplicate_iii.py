# Based on https://leetcode.com/problems/contains-duplicate-iii/

from sortedcontainers import SortedList
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        n = len(nums)
        if n <= 1 or k < 1 or t < 0:
            return False

        mylist = SortedList()  # an ordered list of up to the last k elements

        for idx, num in enumerate(nums):
            lower = mylist.bisect_left(num - t)
            upper = mylist.bisect_right(num + t)

            # If lower != upper, then there must be at least one digit in mylist in the interval [num-t,num+t].
            if lower != upper:
                return True

            mylist.add(num)
            if idx >= k:
                mylist.remove(nums[idx - k])

        return False


if __name__ == '__main__':
    sol = Solution()
    nums, k, t = [1,5,9,1,5,9], 2, 3
    print(sol.containsNearbyAlmostDuplicate(nums=nums, k=k, t=t))
