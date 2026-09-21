from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        def determine_bits(number):
            bitrep = bin(number)[2:]
            l = len(bitrep)
            return set([i for i in range(l) if bitrep[l-i-1] == '1'])

        n = len(nums)
        result = [0] * n
        lowest_index = [n-1 for i in range(32)]
        rightside_or = 0
        for i in range(n-1, -1, -1):
            current_bit_res = determine_bits(nums[i])
            for pos in current_bit_res: lowest_index[pos] = i
            maxor = rightside_or | nums[i]
            maxor_bit_rep = determine_bits(maxor)
            distances = [lowest_index[x]-i+1 for x in maxor_bit_rep]
            result[i] = max(distances) if len(distances)>0 else 1
            rightside_or = maxor
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestSubarrays([0]))
