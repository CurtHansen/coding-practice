# Based on https://leetcode.com/problems/1-bit-and-2-bit-characters/
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        """
        Idea:   Can we construct string where last character is NOT one-bit?
                Answer to original question is opposite of this result.
        """

        n = len(bits)

        def recursive_build(start_idx, end_idx):

            if end_idx == -1:
                possible = True

            elif start_idx == end_idx:
                if bits[start_idx] != 0:
                    possible = False
                else:
                    possible = any([recursive_build(start_idx - 1, start_idx - 1),
                                    recursive_build(start_idx - 2, start_idx - 1)])

            else:
                if bits[start_idx:end_idx + 1] in [[1, 0], [1, 1]]:
                    possible = any([recursive_build(start_idx - 1, start_idx - 1),
                                    recursive_build(start_idx - 2, start_idx - 1)])
                else:
                    possible = False

            return possible

        if n == 1:
            alt_possible = False
        elif n >= 2:
            if bits[n-2] == 0:
                alt_possible = False
            else:
                alt_possible = any([recursive_build(n - 3, n - 3),
                                    recursive_build(n - 4, n - 3)])

        return not alt_possible


if __name__ == '__main__':
    sol = Solution()
    sequence = [0,1,0,1,0]
    print(sol.isOneBitCharacter(sequence))
