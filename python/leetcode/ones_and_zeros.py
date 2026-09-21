from collections import Counter, defaultdict
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.configuration_counts = defaultdict(int)  # key: (num 0, num1): counts
        configurations = set()
        for string in strs:
            config = self.identify_configuration(string)
            configurations.add(config)
            self.configuration_counts[config] += 1

        self.answer = 0
        self.search(0, configurations, m, n)
        return self.answer

    def search(self, cumulative_total, remaining_configs, m, n):
        if len(remaining_configs) == 0 or (m == 0 and n == 0):
            return
#        print(f'cumulative_total/remaining_configs/m/n: {cumulative_total}/{remaining_configs}/{m}/{n}')
        for config in remaining_configs:
            if config[0] <= m and config[1] <= n:
#                print(f'cumulative_total/remaining_configs/m/n/config: {cumulative_total}/{remaining_configs}/{m}/{n}/{config}')
                number_used = min(m//config[0] if config[0] else float('inf'),
                                  n//config[1] if config[1] else float('inf'),
                                  self.configuration_counts[config])
                self.answer = max(self.answer, cumulative_total + number_used)
#                print(f'cumulative_total/remaining_configs/m/n/config/number_used/answer: {cumulative_total}/{remaining_configs}/{m}/{n}/{config}/{number_used}/{self.answer}')
                self.search(cumulative_total + number_used, remaining_configs-set([config]),
                            m - config[0] * number_used, n - config[1] * number_used)

    def identify_configuration(self, entry):
        counts = Counter(entry)
        return (counts['0'], counts['1'])


if __name__ == '__main__':
    sol = Solution()
    """
    print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], 4, 4))
    print(sol.findMaxForm(["0001", "111001", "1", "0"], 5, 5))
    print(sol.findMaxForm(["110101010", "010101001", "1110010101", "01011", "0101"], 2, 2))
    print(sol.findMaxForm(["0","0","1","1"],2,2))
    print(sol.findMaxForm(["0","0","1","1","0","1"], 2, 2))
    print(sol.findMaxForm(["0","0","1","1","0","1","1"], 2, 3))
    print(sol.findMaxForm(["0","0","1","1","0","1","1"], 10, 3))
    print(sol.findMaxForm(["0","0","1","1","0","1","1"], 12, 13))
    print(sol.findMaxForm(["111","1000","1000","1000"], 9, 3))
    """
    print(sol.findMaxForm(["11","11","0","0","10","1","1","0","11","1","0","111","11111000","0","11","000","1","1","0","00","1","101","001","000","0","00","0011","0","10000"],
                          90, 66))