class Solution:
    def findDuplicate(self, nums):

        n = len(nums) - 1
        beg, end = 0, n

        while beg < end:
            mid = (beg + end)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                beg = mid+1
            else:
                end = mid

        return end


if __name__ == '__main__':
    mylist = [2,2,2,2,20]
    sol = Solution()
    print(sol.findDuplicate(mylist))