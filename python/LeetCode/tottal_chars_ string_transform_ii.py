# leetcode 333
def multiply_matrices(mat1, mat2, modulus=10**9+7):
    nr1,nc1,nr2,nc2 = len(mat1),len(mat1[0]),len(mat2),len(mat2[0])
    if nc1!=nr2: raise ValueError('matrices incompatible')
    result = [[0]*nc2 for _ in range(nr1)]
    for r in range(nr1):
        for c in range(nc2):
            for k in range(nc1):
                result[r][c] += (mat1[r][k]*mat2[k][c]) % modulus
    return result

def matrix_exponentiation(matrix, exponent, modulus=10**9+7):
    nr,nc = len(matrix),len(matrix[0])
    if nr!=nc: raise ValueError('matrix must be square')
    if exponent==0:
        result = [[0]*nc for _ in range(nr)]
        for i in range(nr): result[i][i] = 1
    elif exponent==1:
        return matrix
    else:
        newexp = exponent//2
        temp = matrix_exponentiation(matrix,newexp,modulus)
        result = multiply_matrices(temp,temp,modulus)
        if exponent%2==1: result = multiply_matrices(result,matrix)
    return result

from typing import List
from collections import Counter
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9+7
        # set up initial vector
        counts,vector = Counter(s),[[0] for _ in range(26)]
        for i in range(26):
            vector[i][0] = counts[chr(97+i)]

        # set up transition matrix
        # row is to character, col is from character
        transition_matrix = [[0]*26 for _ in range(26)]
        for i in range(26):
            to_char_indices = [(i+j)%26 for j in range(1,nums[i]+1)]
            for idx in to_char_indices:
                transition_matrix[idx][i] = 1

        matrix_raised_to_power_t = matrix_exponentiation(transition_matrix,t,MOD)
        final_state = multiply_matrices(matrix_raised_to_power_t,vector,MOD)
        result = sum([final_state[i][0] for i in range(26)]) % MOD
        print(result)

        return result

if __name__ == '__main__':
    sol = Solution()
    sol.lengthAfterTransformations("abcyy",
                                   2,
                                   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
    sol.lengthAfterTransformations("azbk",
                                   1,
                                   [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
