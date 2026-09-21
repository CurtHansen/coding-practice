# Based on 904. Fruit Into Baskets.
from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_fruits = 0
        start = 0
        fruit_counts = defaultdict(int)

        for idx, fruit in enumerate(tree):
            fruit_counts[fruit] += 1

            while len(fruit_counts) > 2:
                fruit_counts[tree[start]] -= 1
                if fruit_counts[tree[start]] == 0:
                    del fruit_counts[tree[start]]
                start += 1
            max_fruits = max(max_fruits, idx - start + 1)

        return max_fruits


if __name__ == '__main__':
    sol = Solution()
    print(sol.totalFruit([1,1,6,5,6,6,1,1,1,1]))
