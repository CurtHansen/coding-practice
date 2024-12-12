from collections import Counter,defaultdict
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts,n = Counter(s),len(s)
        if counts['a']<k or counts['b']<k or counts['c']<k:
            return -1
        nthinstance_fromleft,nthinstance_fromright = defaultdict(lambda: defaultdict(int)),defaultdict(lambda: defaultdict(int))
        cuml,cumr = defaultdict(int),defaultdict(int)
        for i in range(n):
            lidx=i,ridx=n-1-i
            nthinstance_fromleft[s[lidx]][cuml[s[lidx]+1]] = lidx
            cuml[s[lidx]] += 1
            nthinstance_fromright[s[ridx]][cuml[s[ridx]+1]] = ridx
            cuml[s[ridx]] += 1
        print('here')
        print(f'{nthinstance_fromleft=}')
        print(f'{nthinstance_fromright=}')
        return 0

if __name__ == '__main__':
    sol = Solution()
    sol.takeCharacters("aaabbcbcbba",3)