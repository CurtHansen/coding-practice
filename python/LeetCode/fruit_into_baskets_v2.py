from typing import List
from collections import deque
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        current_queue, revised_queue, current_fruits = deque(), deque(), set()
        for fruit in fruits:
            if fruit not in current_fruits:
                if len(current_fruits) < 2:
                    current_fruits.add(fruit)
                else:
                    retained_fruit = current_queue[-1]
                    revised_queue.clear()
                    while len(current_queue) > 0 and current_queue[-1]==retained_fruit:
                        popped_fruit = current_queue.pop()
                        revised_queue.append(popped_fruit)
                    current_queue.clear()
                    while revised_queue: current_queue.append(revised_queue.popleft())
                    current_fruits = {retained_fruit,fruit}
            current_queue.append(fruit)
            result = max(result,len(current_queue))

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.totalFruit([1,2,3,2,2,3,3,2,1,1,2,3,3,2,2,1,1,3]))