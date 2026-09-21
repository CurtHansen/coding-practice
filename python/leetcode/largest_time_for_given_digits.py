# See https://leetcode.com/articles/largest-time-for-given-digits/
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        ans = None
        valid_numbers = {0: [2, 1, 0], 1.2: [3, 2, 1, 0], 1.1: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                         2: [5, 4, 3, 2, 1, 0]}

        def search_possibilities(level, partial_solution, remaining_numbers):
            # level is base 0, so levels 0,1,2,3
            nonlocal ans

            if level == 3:
                # If at level 3, then only one number left, which will be acceptable given position.
                partial_solution.append(remaining_numbers[0])
                ans = partial_solution

            else:
                if level in [0, 2]:
                    possibilities = valid_numbers[level]
                else:
                    possibilities = valid_numbers[1.2] if partial_solution[0] == 2 else valid_numbers[1.1]
                possibilities = [x for x in possibilities if x in remaining_numbers]

                for val in possibilities:
                    if ans is not None:
                        break
                    else:
                        new_remaining_numbers = remaining_numbers.copy()
                        new_remaining_numbers.remove(val)
                        search_possibilities(level + 1, partial_solution + [val], new_remaining_numbers)

        search_possibilities(0, [], A)

        if ans is None:
            return ''
        else:
            return "".join([str(x) for x in ans[:2]]) + ':' + "".join([str(x) for x in ans[2:]])


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestTimeFromDigits([0,6,6,2]))