# based on https://leetcode.com/problems/check-array-formation-through-concatenation/

from collections import deque
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        n = len(arr)
        pieces_mapping = dict()
        for idx, piece in enumerate(pieces):
            pieces_mapping[piece[0]] = idx

        piece_queue = deque()
        idx_arr = 0
        while idx_arr < n:
            if len(piece_queue) > 0:
                next_elem = piece_queue.popleft()
                if next_elem != arr[idx_arr]:
                    return False
            else:
                if arr[idx_arr] not in pieces_mapping:
                    return False
                piece = pieces[pieces_mapping[arr[idx_arr]]]
                for elem in piece[1:]:
                    piece_queue.append(elem)

            idx_arr += 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFormArray([1,2,3,4,5],[[1,2,3,4,5]]))
