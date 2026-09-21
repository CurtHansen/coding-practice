import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 <= n2:
            small_array,n_small,large_array,n_large = nums1,n1,nums2,n2
        else:
            small_array,n_small,large_array,n_large = nums2,n2,nums1,n1
        required_left_group_size = (n_small + n_large + 1) // 2

        left, right = 0, n_small
        while True:
            size_left_group_small = (left + right) // 2
            size_right_group_small = n_small - size_left_group_small
            size_left_group_large = required_left_group_size - size_left_group_small
            size_right_group_large = n_large - size_left_group_large
            if size_left_group_small > 0 and size_right_group_large > 0 and \
                    small_array[size_left_group_small - 1] > large_array[size_left_group_large]:
                right -= 1
            elif size_left_group_large > 0 and size_right_group_small > 0 and \
                    large_array[size_left_group_large - 1] > small_array[size_left_group_small]:
                left += 1
            else:
                break

        result_left_group_small = -sys.maxsize if size_left_group_small == 0 else small_array[size_left_group_small - 1]
        result_left_group_large = -sys.maxsize if size_left_group_large == 0 else large_array[size_left_group_large - 1]
        result_right_group_small = sys.maxsize if size_right_group_small == 0 else small_array[size_left_group_small]
        result_right_group_large = sys.maxsize if size_right_group_large == 0 else nums2[size_left_group_small]
        result_left, result_right = max(result_left_group_small, result_left_group_large), min(result_right_group_small,
                                                                                               result_right_group_large)

        return result_left if (n_small + n_large) % 2 == 1 else (result_left + result_right) / 2


solution = Solution()
print(solution.findMedianSortedArrays([1,3],[2]))
print(solution.findMedianSortedArrays([1,2],[3,4]))
print(solution.findMedianSortedArrays([1,2,3],[3,4,5]))
print(solution.findMedianSortedArrays([1,2,3],[4,5,6]))
print(solution.findMedianSortedArrays([1,2,3,3,3,3,3,3],[4,5,6]))
print(solution.findMedianSortedArrays([2],[]))
print(solution.findMedianSortedArrays([],[2]))
print(solution.findMedianSortedArrays([2],[2]))
