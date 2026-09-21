from typing import List
from collections import defaultdict
import sys
class Solution:
    def minimumTeachings(self, num_languages: int, user_languages: List[List[int]], user_connections: List[List[int]]) -> int:
        num_users = len(user_languages)
        user_languages = [set(x) for x in user_languages]
        faulty_connections = defaultdict(list)
        for u,connections in enumerate(user_connections):
            for c in connections:
                if len(user_languages[u] & user_languages[c]) == 0:
                    faulty_connections[min(u,c)].append(max(u,c))
        def check_language(l:int)->int:
            pass
        result = sys.maxsize
        for i in range(1,num_languages+1):
            result = min(result,check_language(i))
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTeachings(2,[[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))
    print(sol.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))


